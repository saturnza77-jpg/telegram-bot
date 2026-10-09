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
- Gemma 3:12b model
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
Gemma 3:12b generates a response
        ↓
Bot sends the response back to Telegram

```

## How does it work

1. When a Telegram message is received, the bot stores the    message data in the local database.

2. when the message later receives a 👍 reaction, the bot uses  the message ID to find the stored message.

3. If the message exists in he database, its text is extracted and sent to the local LLM theough Ollama.

4. The model generates a response.

5. The bot firs sends a temporary message:
لطفا کمی صبر کنید...

6. After the LLM finishes processing, message changed to:
جواب حاظر است   

7. The genetated AI response is then sent as a new Telegram message.

--------------------------------------------------------------
# AI Model

he project uses:

Gemma 3:12b

The model runs locally through Ollama.

The project does not send the message directly to an external AI service. The Telegram bot communicates with the local Ollama instance running on the computer.

The model is instructed through a System Prompt to:

1. Respond in Persian
2. Use simple and readable text
3. Avoid Markdown formatting
4. Avoid `*` and `_` formatting
5. Avoid Markdown headings
6. Put separate items on separate lines
7. Use normal numbering when needed

This System Prompt is used to make the AI responses more consistent and suitable for the Telegram chat.

--------------------------------------------------------------
# Technology Stack

The main technologies used in this project are:
1. Python
2. PyTelegramBotAPI (TeleBot)
3. Ollama
4. Gemma 3:12b
5. TinyDB
6. python-dotenv

### Python:

Python is the main programming language used to develop the project.

### PyTelegramBotAPI:

PyTelegramBotAPI provides the interface between the Python application and Telegram.

It is used for:

1. Message handlers
2. Reaction handlers
3. Sending messages
4. Replying to messages
5. Telegram polling

### TinyDB:

TinyDB is used as a lightweight local database for storing Telegram messages.

### Ollama:

Ollama is used to run the local language model.

### python-dotenv:

python-dotenv is used to load environment variables from the 
`.env` file.

--------------------------------------------------------------
# Project Structure

```
Bot_Telegram_Project/
│
├── src/
│   ├── bot.py
│   ├── llm.py
│   ├── db.py
│   ├── messages.py

├── images/
│   └── bot.png.png
├── .env
├── message_db.json
├── .gitignore
└── README.md
```

# File Description

```src/bot.py```

This is the main file of the Telegram bot.

It is responsible for:

Creating the Telegram bot
Creating the database handler
Handling ```/start``` and ```/help```
Receiving messages
Storing message data
Handling reactions
Retrieving messages from the database
Calling the LLM
Sending AI responses
Starting Telegram polling

```src/db.py```
This file contains the database handler.

It uses TinyDB to:

Store messages
Retrieve a message by message ID
Retrieve all stored messages
Delete messages
Close the database

```src/llm.py```
This file is responsible for communication with Ollama.

It:

1. Selects the language model
2. Sends the System Prompt
3. Sends the user's message
4. Receives the model response
5. Returns the generated text

The default model is:

```gemma3:12b```

```src/messages.py```

This file stores the static messages used by the bot.

For example:

1. Welcome message
2. Bot running message

Keeping these messages in a separate file makes them easier to update.

--------------------------------------------------------------
# Requirements

Before running the project, make sure the following are installed:

- Python 3.10 or newer
- PyTelegramBotAPI for Telegram Bot integration
- Ollama for running the local language model
- Gemma 3:12b language model
- TinyDB for local message storage
- python-dotenv for loading environment variables


## Installation

### 1. Install Python

Download and install Python from the official website:

https://www.python.org/downloads/

Verify the installation:

```bash
python --version
```

### 2. Install Python Dependencies

Run the following command in the project environment:

```bash
python -m pip install pyTelegramBotAPI ollama tinydb python-dotenv
```

These packages provide Telegram integration, communication with Ollama, local database storage, and environment configuration.

### 3. Install Ollama

Download and install Ollama for your operating system:

https://ollama.com/download

Check the installation:

```bash
ollama --version
```

### 4. Download the Required AI Model

This project uses the Gemma 3:12b language model.

Download the model with:

```bash
ollama pull gemma3:12b
```

Check the installed models:

```bash
ollama list
```

To test the model manually, run:

```bash
ollama run gemma3:12b
```

### 5. Configure the Telegram Bot

Create a Telegram bot using BotFather:

https://t.me/BotFather

Copy the bot token provided by BotFather.

Create a `.env` file in the project root directory:

```env
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
ADMINS_USER_ID=YOUR_ADMIN_USER_ID
VALID_CHATS=YOUR_VALID_CHAT_USERNAME
```

Replace the example values with your own configuration.

`BOT_TOKEN` is required to connect the application to Telegram.

The supervisorand valid-chat settings are defined in the current code, but their validation function is not currently used by the active handlers.

**Security note:** Never upload your real `.env` file or Telegram Bot Token to GitHub. Add `.env` to `.gitignore`.

### 6. Run the Project

From the project root directory, run:

```bash
python -m src.bot
```

Make sure Ollama is installed, the `gemma3:12b` model is available, and the `.env` file contains a valid Telegram Bot Token before starting the bot.

## Additional Notes

### Downloading Ollama

In some regions, you may not be able to download Ollama directly from its official website.

If the official website is inaccessible, you can search Google for "Ollama Soft98" and look for the installer on the Soft98 website.

Whenever possible, downloading from the official Ollama website is recommended. If you use a third-party download website, verify the downloaded file before installing it.

After installing Ollama, download the required language model through the terminal.

For example, to download Gemma 3 12B, run:

```bash
ollama pull gemma3:12b
```

### VPN Requirement

Depending on your network, you may need to connect to a VPN for the bot to communicate with Telegram.