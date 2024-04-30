# 4/30/24

## Setup

Follow this twitter thread: [Let's build an AI Coding assistant with Llama3](https://twitter.com/paulabartabajo_/status/1785006589277077656?s=43).

Create `Modelfile`:

```
# ./Modelfile

FROM llama3

# temperature is between 0 and 1
# 0 -> more conservative
# 1 -> more creative
PARAMETER temperature 0

# set the system message
SYSTEM """
You are a Python coding assistant. Help me autocomplete my Python code.
"""
```

Run `ollama create my-python-assistant -f ./Modelfile`

Confirm the new model is available:

```
$ ollama ls
NAME                      	ID          	SIZE  	MODIFIED
codellama:latest          	8fdf8f752f6e	3.8 GB	6 days ago    	
llama2:latest             	78e26419b446	3.8 GB	8 days ago    	
llama3:70b                	bcfb190ca3a7	39 GB 	8 days ago    	
llama3:latest             	71a106a91016	4.7 GB	8 days ago    	
my-python-assistant:latest	c25cd560bdc2	4.7 GB	34 seconds ago	
```

In `VS Code` install `Continue v0.8.25` extension.

Move from left to right sidebar so it doesn't cover file explorer. If you close the right sidebar, it can be re-opened with `Cmd + L`.

>Most important shortcuts
>
>If you'd prefer different keys, these shortcuts can be customized in VS Code settings.
>
>Cmd/Ctrl + L = Select code
>
>Cmd/Ctrl + Shift + L = Select code for follow-up
>
>Cmd/Ctrl + I = Quick edit
>
>Cmd/Ctrl + Shift + R = Automatically debug terminal

Click and examine each of the 3 boxed elements. The `Continue` button at the bottom is inactive. After quite awhile it somehow became active. Clicking on it brings up `continue_tutorial.py` which is helpful to go through.

## Use `ollama` 

- At bottom of `Continue` pane there is a pop-up menu that says `Claude 3 Sonnet (Free trial)` and just to the right of it is a plus sign.
- Click the plus sign.
- Choose `Ollama`.
  - Choose `Autodetect`.

- Now all of the models that have been installed with `Ollama` are available to select in the pop-up menu.

## Suggest code

- Start a line in the python file with a `#` character and in the resulting comment say something like `write a function that ...`



