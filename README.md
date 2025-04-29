# Ollama Discord Bot

This is a Discord bot that integrates the Ollama AI models for chat-based interactions. It utilizes the Discord API with the `discord.py` library and supports multiple AI models for responding to user messages.

## Features

- Uses different AI models for generating responses (`deepseek-r1`, `Qwen2:0.5B`, `sroecker/sauerkrautlm-7b-hero`, etc.).
- Automatically processes user messages and generates responses.
- Implements a message length restriction to ensure responses fit within Discord's character limit.
- Protects against accidental message flooding.

## Requirements

- Python 3.8+
- `discord.py` library (`pip install discord`)
- `ollama` library for AI chat integration (`pip install ollama`)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/QCrafter/Ollama-Discord-Bot.git
   cd Ollama-Discord-Bot
    ```
2. Replace "InsertYourTokenHere" in BOT_TOKEN with your actual Discord bot token.
3. Run
   ```sh
   python3 main.py
    ```
