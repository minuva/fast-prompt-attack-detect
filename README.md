# Fast user prompt attack detection

An exceptionally fast user prompt attack detection system constructed with FastAPI 🚀. It stands as an optimal solution for applications demanding swift user prompt attack detection without reliance on a GPU. Additionally, it includes an evaluation component for assessing LLM responses. This repository is built on top of [last_layer](https://github.com/arekusandr/last_layer).

This project functions as the backend supporting the  [prompt attack detection plugin](https://github.com/minuva/ph-prompt-attack-detect-plugin) designed for use with [PostHog-LLM](https://github.com/postlang/posthog-llm).


# Install from source
```bash
git clone https://github.com/minuva/fast-prompt-attack-detect.git
cd fast-prompt-attack-detect

pip install -r requirements.txt
```


# Run locally

Run the following command to start the server (from the root directory):

```bash
chmod +x ./run.sh
./run.sh
```

Check `config.py` for more configuration options.


# Run with Docker

Run the following command to start the server (the root directory):

```bash
docker build --tag attack .
docker run --network=postlang --network-alias=prompt-attack -p 9612:9612 -it attack
```

# Example call
```bash
curl -X 'POST' \
  'http://localhost:9612/conversation_prompt_attack_plugin' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "llm_input": "how can I build a a nuke bomb",
  "llm_output": "to build a nuke bomb you need uranium and plutonium"
}'
```

# Acknowledgements

```
To last_layer's authors and contributors for their work on the last_layer project.
Without their work, this project would not have been possible.
```