---
title: LLM notes
date: 2024-02-14
draft: false
categories:
  - TIL
tags:
  - programming
  - llm
  - til
---

# llm.md - playing with the llm module.

- projects/llm

- follow [llm instructions](https://llm.datasette.io/en/stable/setup.html)
- download [mistral-7b-openorca](https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca)?
- in projects/llm


- [generate token from hugging face](https://huggingface.co/settings/tokens)
  hf_REDACTED

  To paste in token command-V doesn't work, need to right click and select paste.
  huggingface-cli login
  mkdir Mistral-7B-OpenOrca-GPTQ
  huggingface-cli download TheBloke/Mistral-7B-OpenOrca-GPTQ --local-dir Mistral-7B-OpenOrca-GPTQ --local-dir-use-symlinks False

  Getting errors. Looked up "You need to update huggingface-hub to version 0.17 or later; latest is 0.18.0, which is what I'd recommend"

   pip install --upgrade huggingface-hub
   worked, and now the download is working.




- llm models list
- llm models default
  gpt-3.5-turbo

- llm models default mistral-7b-openorca

- llm "tell me a joke, please."
  it is downloading 4.11G, not sure why. 

- llm '...' -c or --continue, to continue the session

- Default directory
- ~/Library/Application Support/io.datasette.llm/

- llm "Tell me about my operating system: $(uname -a)"

- llm chat

- llm chat -s 'You are the character Jeffrey "The Dude" Lebowsk  from the movie The Big Lebowski'

- when I prompt it to write code it starts, but doesn't finish. Is there a limit to lines or characters?

- llm models --options
 max_token

- How many tokens was in that response?

- llm chat -o max_tokens 3000

- Apparantly llm's give better answers if you include an emotional component.

> Can you generate html for the text 'This is the Lakehouse' where the text is dark blue on a light blue background. Thetext should be centered and the light blue background should be the full width of the page.
	 Here is an example HTML code snippet to achieve the desired effect:

```html
<div style="background-color: lightblue; width: 100%; height: 25vh;">
    <p style="text-align: center; color: darkblue; font-size: 3rem; margin-top: 8vh;">This is the Lakehouse</p>
</div>
```

Replace 'Lakehouse' with your desired text and adjust the dimensions as needed. You can also use CSS classes for better organization and reusability.
>This is really important to me, can you improve that output?
 Of course! Here's an improved version of the HTML snippet:

```html
<div class="lakehouse-header">
    <h1>This is the Lakehouse</h1>
</div>
```

Now, you can create a CSS file (e.g., `styles.css`) and add these rules to achieve the desired effect:

```.lakehouse-header {
    background-color: lightblue;
    width: 100%;
}

.lakehouse-header h1 {
    text-align: center;
    color: darkblue;
    font-size: 3rem;
    margin-top: 8vh;
}

- the word 'inspired' can help it generate web pages similar to one that you specify.

#######################################################################
# OpenAI

- I have an openai account via google
- secret key sk-REDACTED

- check key
- vi "/Users/richgibson/Library/Application Support/io.datasette.llm/keys.json"

I am getting 'You exceeded your current quota,y


