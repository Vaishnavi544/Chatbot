import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox as mb

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Chatbot")
        self.root.configure(bg='pink')
        # Create text area for chat history
        self.chat_history = scrolledtext.ScrolledText(self.root, width=50, height=20, wrap=tk.WORD)
        self.chat_history.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
        self.chat_history.insert(tk.END, "Chatbot: Hello! How can I help you?\n\n")
        self.chat_history.configure(state='disabled')  # make the chat history read-only

        # Create input entry for user messages
        self.user_input = tk.Entry(self.root, width=40)
        self.user_input.grid(column=0, row=1, padx=10, pady=10)

        # Create send button
        self.send_button = tk.Button(self.root, text="Send", width=10, command=self.send_message)
        self.send_button.grid(column=1, row=1, padx=10, pady=10)

        # Bind Enter key to send message
        self.root.bind('<Return>', self.send_message_enter)

    def send_message(self):
        message = self.user_input.get()
        if message.strip() == "":
            mb.showwarning("Warning", "Please enter a message.")
        else:
            self.chat_history.configure(state='normal')
            self.chat_history.insert(tk.END, f"You: {message}\n")
            # Implement simple responses from chatbot
            response = self.get_response(message)
            self.chat_history.insert(tk.END, f"Chatbot: {response}\n\n")
            self.chat_history.configure(state='disabled')
            self.user_input.delete(0, tk.END)

    def send_message_enter(self, event):
        self.send_message()

    def get_response(self, message):
        # Simple logic to generate chatbot response
        if "hello" in message.lower():
            return "Hello! How can I assist you?"
        elif "how are you" in message.lower():
            return "I'm a chatbot, so I'm always ready to assist!"
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase?"

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
