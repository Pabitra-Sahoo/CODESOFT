# CODESOFT
Oceaneyes Chatbot
# Introduction
Oceaneyes Chatbot is a Python application that allows users to interact with a chatbot. The chatbot can respond to various user inputs and engage in conversations. This chatbot application is built using the tkinter library, which provides a graphical user interface (GUI) for the chatbot.

# Key Concepts
tkinter: The tkinter library is a standard Python library for creating GUI applications. It provides various widgets and functions to build interactive interfaces.

Chatbot: A chatbot is an artificial intelligence program designed to simulate human conversation. It can understand and respond to user inputs, providing information or performing tasks based on predefined rules or machine learning algorithms.

User Input: The user input is the text or command provided by the user to interact with the chatbot. The chatbot processes this input and generates a response accordingly.

Chat History Display: The chat history display is a text area where the conversation between the user and the chatbot is displayed. It shows the user's messages, chatbot's responses, and any other relevant information.

Send Button: The send button is a button widget that triggers the processing of the user's input. When clicked, it retrieves the text from the input field, displays the user's message in the chat history, generates a chatbot response, and displays it in the chat history.

# Code Structure
The code provided consists of a class called ChatbotApp that represents the chatbot application. It has the following components:

Initialization: The __init__ method initializes the chatbot application by creating the main window using tkinter.Tk(). It sets the title of the window to "Oceaneyes Chatbot". It also creates the chat history display, input field, and send button using the tkinter.Text, tkinter.Entry, and tkinter.Button widgets, respectively. Finally, it inserts a welcome message from the chatbot in the chat history display.

User Input Processing: The process_user_input method is called when the send button is clicked. It retrieves the user's input from the input field, inserts it in the chat history display as the user's message, calls the get_chatbot_response method to generate a chatbot response based on the user's input, inserts the chatbot's response in the chat history display, and clears the input field.

Chatbot Response Generation: The get_chatbot_response method takes the user's input as a parameter and generates a chatbot response based on predefined rules. It uses conditional statements to check for specific keywords or phrases in the user's input and returns an appropriate response. If none of the predefined conditions are met, it returns a default response indicating that the chatbot didn't understand the user's query.

Application Execution: The run method starts the main event loop of the tkinter application, allowing the chatbot application to run and respond to user interactions.

# Code Examples
Here are a few examples of how the chatbot responds to different user inputs:

User Input: "Hello" Chatbot Response: "Hello! Sir/Ma'am"

User Input: "What is your name?" Chatbot Response: "Myself Chatbot."

User Input: "Write a joke" Chatbot Response: "Today, I asked my phone 'Siri, why am I still single?' and it activated the front camera."

User Input: "Thanks" Chatbot Response: "Thank you, CodeSoft, for providing me the opportunity to join the AI internship program."

User Input: "Describe yourself" Chatbot Response: "I'm a chatbot created by Pabitra Sahoo for CodeSoft Internship."

User Input: "Bye" Chatbot Response: "Goodbye! Have a great day!"

User Input: "Can you help me with something?" Chatbot Response: "Sorry, I didn't understand. Could you please rephrase your query?"

# Conclusion
The Oceaneyes Chatbot is a Python application that allows users to interact with a chatbot. It provides a graphical user interface (GUI) using the tkinter library. The chatbot can respond to various user inputs and engage in conversations based on predefined rules. This chatbot application can be further enhanced by adding more rules and improving the natural language processing capabilities.

# Implementation :
setup python compiler on your code editor
then paste my code
run it

you  can give these commands to my chatbot as it is a basic chatbot using if else

hello

what is your name

write a joke

describe yourself

bye


try  giving your own commands and share with me.
![Screenshot 2024-05-31 091052](https://github.com/Pabitra-Sahoo/CODESOFT/assets/135823202/e550e820-ab43-4ee8-8aa6-0249b639d988)


thank you for reading.



