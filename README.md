# Telegram AI Assistant

A Python-based Telegram bot that receives and stores Telegram messages and can generate AI-based responses using a local Large Language Model (LLM).

The project combines Telegram, a lightweight local database, and a locally running language model through Ollama.

When a message is received, its information is stored in a local TinyDB database. When the message receives a 👍 reaction, the bot retrieves the stored message, sends its text to the local LLM, and sends the generated response back to Telegram.

---

## Features

- Telegram bot built with Python
- `/start` and `/help` commands
- Automatic storage of received messages
- Local message database using TinyDB
- Reaction-based AI processing
- 👍 reaction as the AI trigger
- Local LLM execution using Ollama
- Gemma 3 12B model
- Persian-language responses
- Custom System Prompt for controlling AI responses
- Environment variable support using `.env`

---

## Architecture

The project consists of three main parts:

### 1. Telegram Bot

The Telegram bot is responsible for:

- Receiving messages
- Receiving reactions
- Handling `/start` and `/help`
- Storing message information
- Retrieving stored messages
- Sending AI-generated responses
- Running the Telegram polling process

The project uses PyTelegramBotAPI (TeleBot) to communicate with Telegram.

### 2. Database

TinyDB is used as a lightweight local database.

Received Telegram messages are stored in:

`message_db.json`

The database allows the bot to retrieve a previously stored message using its message ID.

### 3. Local LLM

The project uses Ollama to run a language model locally.

The model used in this project is:

`gemma3:12b`

The stored message text is sent to the model, and the model generates a response according to the System Prompt defined in the project.

---

## Workflow

The main workflow of the project is:

```text
User sends a message
        ↓
Telegram Bot receives the message
        ↓
Message information is stored in TinyDB
        ↓
User adds a 👍 reaction
        ↓
Bot receives the reaction
        ↓
Bot checks the reaction
        ↓
Stored message is retrieved from the database
        ↓
Message text is extracted
        ↓
Text is sent to Ollama
        ↓
Gemma 3 12B generates a response
        ↓
Bot sends the response back to Telegram