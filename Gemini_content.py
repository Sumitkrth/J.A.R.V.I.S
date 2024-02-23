from config import key
import requests #requesting imformation from web
import json
from mic_to_text import mic1

def chat1(chat):
    messages = [] # list of all messages

    system_message = "Hey Sumit, I am J.A.R.V.I.s: " # first instruction
    message = { "role" : "user",
               "parts" : [{"text": system_message +" "+ chat }]}
    messages.append(message)
    data = { "contents": messages }
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="+key
    response = requests.post(url, json=data)

    t1 = response.json()
    #print(t1)
    t2 = t1.get("candidates")[0].get("content").get("parts")[0].get("text")
    print(t2)

chat = mic1()
#chat = input("how can i help you?\n")
chat1(chat)

  


