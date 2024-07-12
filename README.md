# Chatbot
This is a simple chatbot application created using Python and the `tkinter` library. The chatbot can respond to basic greetings and questions. It serves as an example of how to create a basic GUI application with a chatbot feature.

## Features

- Text area for chat history
- Input field for user messages
- Send button to send messages
- Simple responses from the chatbot
- Warning message if user input is empty

## Requirements

- Python 3.x
- `tkinter` library (usually included with standard Python installations)

## How to Run

1. **Clone the repository or download the script**:
   ```bash
   git clone <repository-url>
   ```
   or simply download the script file.

2. **Navigate to the directory**:
   ```bash
   cd <directory>
   ```

3. **Run the script**:
   ```bash
   python chatbot.py
   ```

## Code Overview

### Imports

```python
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox as mb
```

### ChatbotApp Class

The `ChatbotApp` class initializes the GUI components and handles user interactions.

- **__init__ method**: Sets up the main window, chat history area, input entry, and send button.
- **send_message method**: Retrieves the user message, updates the chat history, and gets a response from the chatbot.
- **send_message_enter method**: Binds the Enter key to send the message.
- **get_response method**: Simple logic to generate responses based on user messages.

### Main Function

```python
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
```

This block of code creates the main window and runs the application.

## Example Usage

1. **Open the application**: Run the script to open the chatbot window.
2. **Send a message**: Type a message in the input field and click "Send" or press Enter.
3. **Receive a response**: The chatbot will respond with a predefined message based on the input.


