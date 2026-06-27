# PYTHON AI VOICE AND CHAT ASSISTANT-Python-based AI assistant that supports voice commands , chat interactions .
#python AI Assistant 
# pip install pyttsx3
#importing necessary libraries

import pyttsx3
from datetime import datetime

#initialize the text-to-speech engine 
engine =pyttsx3.init()

#define a function to speak text 
def speak(text):
    print("AI Bot:", text)
    engine.say(text)
    engine.runAndWait()

#greet
print("Oliver: hello! I am ai assistant. type'exit' to end.\n")

#start chatting loop
while True:
    user_input = input("You: ").lower()

# if user says hello or hi , the bot replies.
    if user_input in ["hello", "hi"]:
        speak("Hello! How can I assist you today?")
# how are you 
    if "how are you" in user_input:
        speak("I am just a program, but I'm functioning as expected! How about you?")

#name
    elif "what is your name" in user_input:
        speak("I am Oliver, your AI assistant. How can I help you today?")

#time
    elif "time" in user_input:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")

# calculate
    elif "calculate" in user_input:
        try:
            result=eval(user_input.replace("calculate", ""))
            speak(f"The result is {result}")
        except Exception as e:
            speak("Sorry, I couldn't calculate that. Please make sure to provide a valid expression.")
         

    
