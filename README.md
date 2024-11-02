# ChatGenie: Chat Interaction Automator

## Overview
This project is an auto-reply chatbot that analyzes chat history and generates contextual responses in both Hindi and English. The chatbot automates messaging interactions, providing seamless communication and engagement.

## Features
- **Bilingual Responses**: Communicates effectively in Hindi and English.
- **Chat History Analysis**: Analyzes previous messages to generate contextually relevant replies.
- **Automated Interaction**: Uses screen automation techniques to monitor chat logs and respond in real-time.

## Libraries Used
- OpenAI: For natural language processing and generating responses.
- pyautogui: For automating mouse and keyboard actions.
- pyperclip: For clipboard management (copying and pasting text).
- time: For adding delays and managing timing in the script.

## Requirements
Install the required libraries by running:
```bash
pip install openai pyautogui pyperclip
```

## Project Structure
```bash
auto-reply-chatbot/
│
├── ai.py                   # Script for generating responses using OpenAI
├── chat_bot.py             # Main script for monitoring chat and automating replies
├── get_cursor.py           # Script for getting cursor position (for debugging)
├── temp.py                 # Temporary script for testing clipboard functionality
├── musicLib.py             # (If applicable) Library for managing music links
│
├── README.md               # Project documentation
├── requirements.txt        # List of required libraries (if applicable)
│
└── .gitignore              # Git ignore file for excluding unnecessary files
```


## Usage
1. Set your OpenAI API key in the code.
2. Run `chat_bot.py` to start the chatbot.
3. The bot will monitor your chat and respond automatically based on the conversation context.

