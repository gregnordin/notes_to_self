# Log

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
