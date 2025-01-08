# Customer Support Chat Application

This is a simple customer support chat application built using FastAPI and WebSockets. The application allows multiple users to connect to a chat room, send messages, and see messages from other users in real-time. The chat history is also saved to a text file with timestamps.

## Features

- Real-time chat using WebSockets
- User connection and disconnection notifications
- Chat history saved to a text file with timestamps
- User-friendly UI with message input and display

## Requirements

- Python 3.7+
- FastAPI
- WebSockets

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/customer-support-chat.git
    cd customer-support-chat
    ```

2. Install the required dependencies:
    ```bash
    pip install fastapi uvicorn
    ```

## Running the Application

1. Start the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

2. Open your web browser and navigate to `http://127.0.0.1:8000` to access the chat application.

## Usage

1. Enter your name in the input field at the top right corner and click "Set Name".
2. Type your message in the message input field at the bottom and click "Send" to send the message.
3. You will see messages from other users in real-time as they are sent.

## File Structure

- `main.py`: The main FastAPI application file that handles WebSocket connections and message broadcasting.
- `index.html`: The HTML file for the chat application's UI.

