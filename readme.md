# RULE BASED CHATBOT
Rule-Based Command-Line Chatbot
A simple, interactive command-line chatbot built with Python. This chatbot uses a predefined set of rules and regular expressions to understand and respond to user input in a conversational manner.


# Features
Rule-Based Logic: Responds to user input based on a dictionary of regex patterns.

Basic Conversation: Handles common greetings, questions, and farewells.

Dynamic Responses: Can provide the current date and time.

Fallback Mechanism: Provides a default response if the input is not understood.

Easy to Extend: New rules and responses can be easily added to the script.

Lightweight: Runs directly in the terminal with minimal dependencies.

# How It Works
The chatbot's logic is centered around a Python dictionary called rules.

Rules Dictionary: Each key in the dictionary is a regular expression (regex) pattern representing a type of user input (e.g., r"hello|hi|hey"). The corresponding value is a list of possible string responses.

Input Matching: When a user enters a message, the script converts it to lowercase and iterates through the rules dictionary. It uses Python's re.search() function to find the first pattern that matches the user's input.

Response Generation: Once a match is found, the chatbot selects a random response from the list associated with that pattern.

Special Cases: The script has special logic to detect keywords like "date" or "time". If found, it fetches the current date or time from the datetime module and formats it into the response string.

Default Response: If no rules match the input, the chatbot returns a random response from the "default" list, indicating that it didn't understand.

# Technology Stack
Python 3.10

NLTK (Natural Language Toolkit): Used to ensure the punkt tokenizer data is available, a common prerequisite for NLP tasks.

Standard Libraries:

re: For regular expression matching.

datetime: To fetch the current date and time.

random: To choose a random response from a list.

Getting Started
Follow these steps to get the chatbot running on your local machine.

Prerequisites
Python 3.6 or newer. You can download it from python.org.

Installation
Clone the repository (or save the script):
If this were a Git repository, you would clone it. For now, just save the Python script as chatbot.py.

Navigate to the project directory:

cd path/to/your/project

Install the required Python package:
The script uses NLTK. You can install it using pip.

pip install nltk

NLTK Data Download:
The first time you run the script, it will check if the punkt tokenizer models are downloaded. If not, it will automatically download them for you. This only needs to be done once.

#Usage
To start the chatbot, run the script from your terminal:

python chatbot.py

The chatbot will greet you, and you can start typing your messages.

#Example Interaction:

ChatBot: Hello! How can I assist you today?
You: hi
ChatBot: Hey! What can I do for you today?
You: what is your name
ChatBot: You can call me ChatBot.
You: what is the current date?
ChatBot: Today's date is 2023-10-27.
You: what can you do
ChatBot: I can answer simple questions and have conversations based on predefined rules.
You: bye
ChatBot: Goodbye!

To exit the chat, simply type bye or goodbye.

#How to Customize
You can easily extend the chatbot's knowledge by adding new key-value pairs to the rules dictionary in the script.

For example, to teach the chatbot how to respond to questions about the weather, you could add the following line to the rules dictionary:

rules = {
    # ... existing rules
    r"weather": ["I'm sorry, I am not connected to a weather service.", "I can't check the weather yet, but it's always sunny in the cloud!"],
    r"who made you|who created you": ["I was created by a developer using Python.", "I am a product of code."]
    # ... rest of the rules
}
