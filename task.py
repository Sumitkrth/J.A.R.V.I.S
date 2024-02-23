import requests
import socket
from config import key

def get_ip(host):
    try :
        result = socket.getaddrinfo("google.com",None)
    except Exception as e :
        result = f"Error in finding IP, {e}"
    return result 

def temp_room(room):
    result ="NO device to measure temperature"
    return result 

def temp_city(city):
     
    url = "https://yahoo-weather5.p.rapidapi.com/weather" #endpoint
    
    querystring = {"location":city,"format":"json","u":"f"}
    
    headers = {
    	"X-RapidAPI-Key": "fffdccfaf5msha30d30cfb030554p11d9dcjsn7bffe1b94ef9",
    	"X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    
    d1 = (response.json())
    #print(d1)
    d1 = d1.get("current_observation")
    hum = d1.get('atmosphere').get('humidity')
    temp = d1.get('condition').get('temperature')
    temp = round(((temp-32)*5)/9,2)
    return (f"Humidity: {hum}, Tmeperature: {temp}C ")


def chat1(chat):
    messages = [] # list of all messages

    system_message = f"Hey,you are J.A.R.V.I.s:, Find the content related to the query give the responce in beautiful manner: " # first instruction
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
    return t2


definitions = [

           {
           "name": "temp_city",
           "description": "find weather, temperature of a city",
           "parameters":
           {    
           "type": "object",
           "properties": {
               "city" :{
                   "type" : "string",
                   "description" : "City to find weather"
                   }
                        }
            }
           },

           {
           "name": "temp_room",
           "description": "find temperature of my room or my home ",
           "parameters":{    
           "type": "object",
           "properties": {
               "room" :{
                   "type" : "string",
                   "description" : "room or home to find temperaure"
                   }
                        }
              }
           },

           {
           "name": "get_ip",
           "description": "find the ip address of given domain name or url ",
           "parameters":{    
           "type": "object",
           "properties": {
               "host" :{
                   "type" : "string",
                   "description" : "grt the url or domain name"
                   }
                        }
              }
           },
           {
           "name": "chat1",
           "description": "hi hello how are you i'm ",
           "parameters":{    
           "type": "object",
           "properties": {
               "chat" :{
                   "type" : "string",
                   "description" : "full query asked by user"
                   }
                        }
              }
           }
]

if __name__=="__main__":
    print(temp_city(''))    