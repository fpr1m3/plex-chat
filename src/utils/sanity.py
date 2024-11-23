import os
from ollama import Client

def CheckEnvironment(default_model: str) -> bool:
    client = Client(host=os.getenv("SERVER_URL"))
    try:
        models = client.list()
        llama_exists = any(
            model["name"] == default_model
            for model in models["models"]
        )
        if not llama_exists:
            print(f"{default_model} model not found")
            return False
        return True
    except Exception as e:
        print(e)

