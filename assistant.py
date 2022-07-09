from flask import render_template
from googlesearch import search 
from bs4 import BeautifulSoup
import requests
import webbrowser
import os
import time
import gtts #pip install gTTS in cmd
from playsound import playsound #pip install playsound in cmd
import speech_recognition as sr

print("py Assistant \n")

def play(text):
    file = "sound.mp3"
    tts = gtts.gTTS(text)
    tts.save(file) 
    playsound(file)
    os.remove(file)


def ask():
    print("Listning")
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    try:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print(command)
            return command
    except :
        play("No Voice detected")
        novoice="novoice"
        return novoice
        


def query(q):
    try:
        
        user_query=q
                
        if user_query=='what is your name':
            return "my name is py assistant and i am developed by mihir anam"
           
        elif user_query=='hello':
            return "Hello user, how are you"
           

            
        URL="https://www.google.co.in/search?q=" + user_query

        headers = {
            'User-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
        }
        page=requests.get(URL,headers=headers)
        soup=BeautifulSoup(page.content,'html.parser')
        result=soup.find(class_='Z0LcW CfV8xf').get_text()
        play(result)
        return result
        
    except AttributeError:
        try:
            result=soup.find(class_='Z0LcW').get_text()
            play(result)
            return result
            
        except AttributeError:
            try:
                result=soup.find(class_='hgKElc').get_text()
                play("getting result for your search")
                return result
                
            except AttributeError:
                try:
                    result=soup.find(class_='IsqQVc NprOob wT3VGc').get_text()
                    play(result)
                    return result
                    
                except AttributeError:
                    play("Getting results for your search:")
                    for i in search(user_query):
                        webbrowser.open(i)
                        return i
                    #     user=input(" Enter 'y' to visit this Website \n Enter 'n' to view another Website \n Enter 's' to search another Question: ")
                    #     if user=="y":
                    #         webbrowser.open(i)
                    #     elif user=="n":
                    #         continue
                    #     else:
                    #         break
                    # query()