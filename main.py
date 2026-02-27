# Import requests library for HTTP calls
import requests

# Ollama chat API endpoint
url = "http://localhost:11434/api/chat"

# Request payload with model and conversation messages
data = {
    "model" : "smollm2:135m",
    "stream": False,
    "messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Please write 500 words about the fall of rome"},
    ],
}

# Send POST request to Ollama
response = requests.post(url, json=data)
# Raise exception if request failed
response.raise_for_status()

# Print model's reply
print(response.json()["message"]["content"])
