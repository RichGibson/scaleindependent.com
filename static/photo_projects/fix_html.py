# fix_html.py - walk all of the html files and add meta tags
# so that pelican can display them.

# Step 1: save the file dates in case I mess up.

# find . | xargs ls -oAHd | grep html > file_dates.txt

# <meta name="category" content='About' />
# <meta name="name" content='About' />
# <meta name="date" content='October 5, 2023' />
# <meta name="tags" content='tag,tag,tag' />

import re
import os
from bs4 import BeautifulSoup as bs
import pdb

category="Photo"
# name? do I need that, I don't think so
# date - from file_info
# tags - directory name, photo, ?

# load the dates

file_info = {}
with open('file_dates.txt') as infile:
    for line in infile.readlines():
        line=line.strip()
        date=line[37:49]
        filename=line[50:]
        file_dir=line[52:]
        #match=re.match('(.*?)/',file_dir)
        #if match:
            #file_dir=match.group(0)
            #file_dir=file_dir[0:-1]
        #else:
            #print(f"no match {line}")

        file_dir=file_dir[0:-1]
        #print(line)
        #print(date)
        #print(filename)
        #print(match)
        tags=f'photo,{file_dir}'

        meta_st = f"""
        <meta name="category" content='{category}' />
        <meta name="date" content='{date}' />
        <meta name="tags" content='{tags}' />
        """
        file_info[filename]=meta_st

# try one file

def check_file(foo):
    """ do we have a head and a title? """
    with open(foo) as infile:
        soup = bs(infile,features="lxml")
    print(soup.title)
    # Are 'Keywords' being used as tags? Yes.
    # Do all pages have them?
    foo=soup.find_all("meta", attrs={'name':"Keywords"})
    print(foo)
    print()
    #pdb.set_trace()




def fix_file(foo):
    """ make the file work for Pelican

    - check for title
    - check for head
    - insert file_info[file]
    """
   
    st=file_info[foo]
    print(file_info[foo])

    # Does file have a head and title?
    check_file(foo)
    return


#fix_file('./von_robotern/index.html')

for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
       if name[-4:].lower()=='html' and name[0:3] != 'IMG' and name[5:6] != '_':
            print(f'files: {os.path.join(root, name)}')
            filename=os.path.join(root,name)

            if re.search('photos',name):
                pdb.set_trace()
                print('foo')
                continue
            fix_file(filename)
            print("..............................")

        # skip index_n
            
   #for name in dirs:
      #print(os.path.join(root, name))


pdb.set_trace()
