import yaml
import requests
import os

api_url = ""
model_name = ""
api_key = ""

# conversation is a list of dicts
def reply(conversation: list) -> str:
    global api_url, model_name, api_key

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + api_key
    }
    
    data = {
        "model": model_name,
        "messages": conversation
    }

    response = requests.post(api_url + "/chat/completions", json=data, headers=headers)
    try:
        response_json = response.json()
    except:
        print("Error: ", response.text)
        return "Error"
    return response_json["choices"][0]["message"]["content"]


def main():
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    global api_url, model_name, api_key
    api_url = config['api']['endpoint']
    model_name = config['api']['model']
    api_key = config['api']['api_token']
    if api_key.startswith("$"):
        try:
            api_key = os.environ[api_key[1:]]
        except:
            print("Error: API Key not found in environment variables")
            return
    print("API URL: ", api_url)
    print("Model Name: ", model_name)
    conversation = [
        {
            "role": "system",
            "content": "You are an AI in a conversation"
        }
    ]

    prompt = input("What is the prompt for this self-conversation? Write it as if it is the first message.\n    ")

    conversation.append({
        "role": "user",
        "content": prompt
    })

    while True:
        response = reply(conversation)
        print("LLM 2: ", response)
        conversation.append({
            "role": "assistant",
            "content": response
        })

        # now get LLM 1 response
        response = reply(conversation)
        print("LLM 1: ", response)
        conversation.append({
            "role": "assistant",
            "content": response
        }) 

if __name__ == '__main__':
    main()