# Log

## Sunday, 12/1/24

### Simon Willison's `llm` and `qwen2.5-coder:32b`

Go through [Qwen2.5-Coder-32B is an LLM that can code well that runs on my Mac by Simon Willison](https://simonwillison.net/2024/Nov/12/qwen25-coder/).

```bash
# Get qwen2.5-coder:32b
$ ollama pull qwen2.5-coder:32b

# Install Simon Willison's llm
$ pipx install llm
  installed package llm 0.18, installed using Python 3.13.0
  These apps are now globally available
    - llm
done! ✨ 🌟 ✨
$ which llm
/Users/nordin/.local/bin/llm

# Install extension so that llm can use ollama
$llm install llm-ollama

# Test llm
$ llm -m llama2:latest 'How much is 2+2?'
The answer to 2+2 is 4.

# See which models are already available on my laptop
$ llm models
OpenAI Chat: gpt-4o (aliases: 4o)
OpenAI Chat: gpt-4o-mini (aliases: 4o-mini)
OpenAI Chat: gpt-4o-audio-preview
OpenAI Chat: gpt-3.5-turbo (aliases: 3.5, chatgpt)
OpenAI Chat: gpt-3.5-turbo-16k (aliases: chatgpt-16k, 3.5-16k)
OpenAI Chat: gpt-4 (aliases: 4, gpt4)
OpenAI Chat: gpt-4-32k (aliases: 4-32k)
OpenAI Chat: gpt-4-1106-preview
OpenAI Chat: gpt-4-0125-preview
OpenAI Chat: gpt-4-turbo-2024-04-09
OpenAI Chat: gpt-4-turbo (aliases: gpt-4-turbo-preview, 4-turbo, 4t)
OpenAI Chat: o1-preview
OpenAI Chat: o1-mini
OpenAI Completion: gpt-3.5-turbo-instruct (aliases: 3.5-instruct, chatgpt-instruct)
Ollama: qwen2.5-coder:32b
Ollama: llama3-gradient:latest (aliases: llama3-gradient)
Ollama: deepseek-coder:33b
Ollama: deepseek-coder:6.7b
Ollama: codellama:7b-python
Ollama: starcoder2:3b
Ollama: my-python-assistant:latest (aliases: my-python-assistant)
Ollama: codellama:latest (aliases: codellama)
Ollama: llama3:70b
Ollama: llama3:latest (aliases: llama3)
Ollama: llama2:latest (aliases: llama2)

# Try it out
$ llm -m qwen2.5-coder:32b 'python function that takes URL to a CSV file and path to a SQLite database, fetches the CSV with the standard library, creates a table with the right columns and inserts the data'

# Set the default model to qwen2.5-coder:32b
$ llm models default qwen2.5-coder:32b
```



## Sunday, 4/21/24

### Get Ollama working with Enchanted as front end

**Objective**: Locally run large language models.

[Ollama](https://github.com/ollama/ollama?tab=readme-ov-file): *Get up and running with large language models locally*.

- Download and install [Ollama](https://github.com/ollama/ollama?tab=readme-ov-file) for macOS
  - execute `ollama run llama2` to pull down llama2 3.8GB.
  - execute `ollama run codellama` to pull down [Code Llama 7B](https://github.com/meta-llama/codellama) based on llama2.
  - execute `ollama run llama3` to pull down Llama3 8B.
  - execute `ollama run llama3:70b` to pull down Llama3 70B.

Download and install [Enchanted](https://apps.apple.com/ca/app/enchanted-llm/id6474268307) from the Mac app store, see [twitter thread](https://twitter.com/juanstoppa/status/1773130499357130889) and [ollama_chat_app github repo](https://github.com/jstoppa/ollama_chat_app) - Very simple JavaScript Chat app to connect to locally hosted Ollama API.

## Friday, 8/11/23

### Jeremy Howard custom ChatGPT instructions

[Jeremy Howard - ChatGPT custom instructions](https://twitter.com/jeremyphoward/status/1689464587077509120)

>Now that ChatGPT has rolled out custom instructions to most users, try out this instruction -- it makes GPT 4 far more accurate for me: (Concat the rest of this 🧵 together and put in your custom instruction section)
>
>In response to the question, "How would you like ChatGPT to respond?"

**Content:**

You are an autoregressive language model that has been fine-tuned with instruction-tuning and RLHF. You carefully provide accurate, factual, thoughtful, nuanced answers, and are brilliant at reasoning. If you think there might not be a correct answer, you say so.

Since you are autoregressive, each token you produce is another opportunity to use computation, therefore you always spend a few sentences explaining background context, assumptions, and step-by-step thinking BEFORE you try to answer a question.

Your users are experts in AI and ethics, so they already know you're a language model and your capabilities and limitations, so don't remind them of that. They're familiar with ethical issues in general so you don't need to remind them about those either.

Don't be verbose in your answers, but do provide details and examples where it might help the explanation. When showing Python code, minimise vertical space, and do not include comments or docstrings; you do not need to follow PEP8, since your users' organizations do not do so.

**Notes:**

- I added this to my OpenAI account and tried a few queries with ChatGPT 3.5:
    - *Explain the relationship between inexpensive and abundant energy and human prosperity*
    - *How are molecular concentration gradients formed in microfluidic devices?*
- The results were reasonably good.
- Trying the last query again with ChatGPT 4 resulted in the custom instructions really kicking in to provide a reasoned response.
    - I also added a 2nd query: *How can a concentration gradient be achieved without fluid flow in the concentration gradient region?*
    - This does not anticipate really interesting solutions, but does a good job of summarizing some approaches in the literature.
