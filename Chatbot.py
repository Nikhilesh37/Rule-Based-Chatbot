import nltk
from nltk.tokenize import word_tokenize
import re
import random
import datetime

try:
    nltk.data.find('tokenizers/punkt')
except nltk.downloader.DownloadError:
    nltk.download('punkt')

rules = {
    r"hello|hi|hey": ["Hello!", "Hi there!", "Hey! What can I do for you today?"],
    r"how are you": ["I'm just a bot, but I'm here and ready to help!", "I'm doing well, thank you!"],
    r"what is your name": ["I am a rule-based chatbot.", "You can call me ChatBot."],
    r"bye|goodbye": ["Goodbye!", "See you later!", "Have a great day!"],
    r"who are you": ["I am a Rule-Based Chatbot here to Assist you"],
    r"thank you|thanks": ["You're welcome!", "No problem!", "Glad I could help!"],
    r"what can you do": ["I can answer simple questions and have conversations based on predefined rules."],
    r"date|today|current date": ["Today's date is {date}."],
    r"time|current time": ["The current time is {time}."],
    r"default": ["I'm sorry, I didn't understand that.", "Could you please rephrase that?",
                 "I'm not sure what you mean."]
}


def tokenize(text):
    return text.split()


def match_rule(rules, user_input):
    user_input = user_input.lower()

    if re.search(r"\b(date|today|current date)\b", user_input):
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        for pattern, responses in rules.items():
            if re.search(r"date|today|current date", pattern):
                 return random.choice(responses).format(date=current_date)

    if re.search(r"\b(time|current time)\b", user_input):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        for pattern, responses in rules.items():
            if re.search(r"time|current time", pattern):
                return random.choice(responses).format(time=current_time)

    for pattern, responses in rules.items():
        if pattern == "default" or "date" in pattern or "time" in pattern:
            continue
        if re.search(pattern, user_input):
            return random.choice(responses)

    return random.choice(rules["default"])


def chatbot_response(user_input):
    response = match_rule(rules, user_input)
    return response


if __name__ == "__main__":
    print("ChatBot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if re.search(r"\b(bye|goodbye)\b", user_input.lower()):
            print("ChatBot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"ChatBot: {response}")