# A conversation between 2 LLMs

Allows you to set a prompt, which sets the tone/guide for the rest of the conversation. 

This was inspired by LLaMA 3 8B, being misconfigured locally, and talking to itself, generating both assistant and human roles. It was able to weave conversation and not get stuck, which was very impressive.

Relies on:
- OpenAI compatible API

Configs:
- "api_base_url" - What is the base url with 'v1' at the end, or where can I attach /chat and get a valid response. Defaults to openai api.
- "model_name" - Defaults to gpt-3.5-turbo as do some API compatible providers.
- "api_token" - If you'd like. Defaults to ""