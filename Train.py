#!/usr/bin/env python3
# (c)J~Net 2022
#
# python CASPA.py
#
## Binding Functions To Requests
from neuralintents import GenericAssistant
from datetime import datetime
import speech_recognition
import pyttsx3 as tts
import sys

recognizer=speech_recognition.Recognizer()

speaker=tts.init()

speaker.setProperty('rate', 150)

todo_list=['go shopping', 'clean room', 'record video']

def add_todo():
    global recognizer
    print("Create a new Note")
    speacker.say("What you want to add?")
    # Some action you want to take
    speaker.runAndWait()
    
    done=false
    while not done:
        try:
        
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio=recognizer.listen(mic)
                
                item=recognizer.recognize_google(audio)
                item=item.lower()

                todo_list.append(item)
                done-True
                
                speaker.say("Added to your to do list")
                speaker.runAndWait()
                
                
        except speech_recognition.UnknownValueError:
            recognizer=speech_recognition.Recognizer()
            speaker.say("Dont understand what you meant, try again...")
            speaker.runAndWait()

def show_todos():
    speaker.say("Herezs your to do list")
    speaker.runAndWait()
    for item in todo_list:
        speaker.say(item)
    speaker.runAndWait()


def create_note():
    global recognizer
    print("Create a new Note")
    speacker.say("What you want to put in your note?")
    # Some action you want to take
    speaker.runAndWait()
    
    done=false
    while not done:
        try:
        
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio=recognizer.listen(mic)
                note=recognizer.recognize_google(audio)
                note=note.lower()  
                speaker.say("Choose filename")
                speaker.runAndWait()
                
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio=recognizer.listen(mic)
                filename=recognizer.recognize_google(audio)
                filename=filename.lower()
            
            with open(filename, 'w') as f:
                f.write(note)
                done=True
                speaker.say(f"Wrote note Succseffully created note {filename}")
                speaker.runAndWait()
                
        except speech_recognition.UnknownValueError:
            recognizer=speech_recognition.Recognizer()
            speaker.say("Dont understand what you meant, try again...")
            speaker.runAndWait()
            
                

def function_exit():
    print("Goodbye my friend, Please come back soon!")
    exit(0)
    # Some action you want to take

def function_time():
    print("the time is ")
    now=datetime.now()
    print(now)
    # Some action you want to take

def function_for_greetings():
    print("You triggered the greetings intent!")
    # Some action you want to take

def function_for_stocks():
    print("You triggered the stocks intent!")
    # Some action you want to take

mappings={
'greeting' : function_for_greetings,
'create_note' : create_note,
'add_todo' : add_todo,
'show_todos' : show_todos,
'stocks' : function_for_stocks,
'time' : function_time,
'exit' : function_exit
}

assistant=GenericAssistant('test-intents.json', intent_methods=mappings ,model_name="test_model")
assistant.train_model()
assistant.save_model()

done=False

while True:

    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio=recognizer.listen(mic)
            
            message=recognizer.recognize_google(audio)
            message=message.lower()

        assistant.request(message)
        
    except speech_recognition.UnknownValueError:
        recognizer=speech_recognition.Recognizer()