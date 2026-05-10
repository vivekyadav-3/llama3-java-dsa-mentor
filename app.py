import gradio as gr
from llama_cpp import Llama
from huggingface_hub import hf_hub_download

# Download the model
repo_id = "vivek387t8238rbhe/llama-3-java-dsa-mentor-gguf"
filename = "unsloth.Q4_K_M.gguf" # update if your filename is different
model_path = hf_hub_download(repo_id=repo_id, filename=filename)

# Load the model
llm = Llama(
    model_path=model_path,
    n_ctx=2048,
    n_threads=2,
)

def respond(message, history):
    prompt = f"Below is a DSA question. Answer it clearly in Java.\n\n### Question:\n{message}\n\n### Answer:\n"
    response = llm(
        prompt,
        max_tokens=512,
        temperature=0.7,
        stop=["### Question:", "<|end_of_text|>", "<|eot_id|>"],
        echo=False
    )
    return response['choices'][0]['text']

demo = gr.ChatInterface(
    respond,
    title="🤖 Llama-3 Java DSA Mentor",
    description="Ask any DSA or Java interview question! (May take 30-60 sec on free CPU)"
)

if __name__ == "__main__":
    demo.launch()
