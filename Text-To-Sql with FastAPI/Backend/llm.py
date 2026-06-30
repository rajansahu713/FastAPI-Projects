import requests


OLLAMA_URL = "http://host.docker.internal:11434/api/generate"
MODEL_NAME = "llama3.1"

def call_llm(prompt):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
        },
    )

    response.raise_for_status()

    return response.json()["response"].strip()