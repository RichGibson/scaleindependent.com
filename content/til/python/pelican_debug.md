---
title: Pelican .html in output causes problems.
date: 2024-08-06
draft: false
categories:
  - TIL
tags:
  - til
  - web
  - debugging
  - pelican
---

For some reason my personal Pelican site won't properly serve localhost:8080

Chrome treats it as a file and downloads it. localhost:8080/index.html works 
fine. 

I hit my head on the wall for a hot minute before I remembered telnet.

    telnet localhost 8080
    get / HTTP/1.1

And it found I was getting a wrong Content-type.

    Content-type: application/octet-stream

Getting the full /index.html works fine.

    telnet localhost 8080
    GET /index.html HTTP/1.1


    Content-type: text/html

This took a while to debug, and was quite a learning opportunity.

## Takeaways
- a file named '.html' in the output directory caused this.
- No, I don't know how I got that file with just an extension, but it is a legal file name.
- Using the logger didn't give me what I wanted
- console.print() is imported in pelican and works fine.
- Pelican initalization code is in /Users/richgibson/anaconda3/lib/python3.11/site-packages/pelican/__init__.py 
- Pelican server code is in /Users/richgibson/anaconda3/lib/python3.11/site-packages/pelican/server.py 
- The issue was the order of SUFFIXES. 
    get_path_that_exists() looks for a file adding each of the SUFFIXES. '.html' Matches the first 
    suffix, so it is returned. 

I changed the order of suffixes and everything is better.

    SUFFIXES = [".html", "/index.html", "/", ""]

I submitted a pull request, which is sort of cool.

## Logging

I wanted every request to show up. So I modified the do_GET and do_POST methods in server.py

They created class ComplexHTTPRequestHandler as a custom request handler to pass to httpd.server


For do_Get I just added the logging.info() line.

    def do_GET(self):
            logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
            # cut off a query string
            original_path = self.path.split("?", 1)[0]
            # try to find file
            self.path = self.get_path_that_exists(original_path)

            if not self.path:
                return

        server.SimpleHTTPRequestHandler.do_GET(self)

for do_POST I grabbed additional information about the request to add to the message.
This might turn out to be a mistake, but I am not using post requests right now.

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n", str(self.path), str(self.headers), post_data.decode('utf-8'))
        logging.info(post_data.decode('utf-8'))
        server.SimpleHTTPRequestHandler.do_POST(self)


