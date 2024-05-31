import tkinter as tk

class ChatbotApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Oceaneyes Chatbot")
        
        #chat history display
        self.display = tk.Text(self.root, height=20, width=80)
        self.display.pack()

        # input field
        self.user_input = tk.Entry(self.root, width=40)
        self.user_input.pack()

        # send button
        self.send_button = tk.Button(self.root, text="Send", command=self.process_user_input)
        self.send_button.pack()

        
        self.display.insert(tk.END, "Chatbot: Hello! How can I assist you today?\n")

    def process_user_input(self):
        user_message = self.user_input.get()
        self.display.insert(tk.END, f"User: {user_message}\n")
        chatbot_response = self.get_chatbot_response(user_message)
        self.display.insert(tk.END, f"Chatbot: {chatbot_response}\n")
        self.user_input.delete(0, tk.END)  # Clear input field

    def get_chatbot_response(self, user_input):
        
        if "hello" in user_input.lower():
            return "Hello! How can I assist you today?"
        if "what is your name" in user_input.lower():
            return "myself Chatbot."
        if "write a joke" in user_input.lower():
            return "Today, I asked my phone “Siri, why am I still single?” and it activated the front camera."
        if "describe yourself" in user_input.lower():
            return "Im a chatbot created by Pabitra Sahoo for CodeSoft Internship"
        elif "bye" in user_input.lower():
            return "Goodbye! Have a great day!"
        else:
            return "sorry, I didn't understand. Could you please rephrase your query?"

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ChatbotApp()
    app.run()
