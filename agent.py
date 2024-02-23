from config import key
import task
import requests


def parse_function_response(message):
    function_call = message[0].get("functionCall")
    function_name = function_call["name"]
    print("Gemini: call function ", function_name)
    try :
        arguments = function_call.get("args",)
        print("Gemini: arguments are ", arguments)
        if arguments:
            d = getattr(task,function_name)
            print("function is",d) 
            function_response = d(**arguments)
        else:
            function_response = "No arguments are present"
    

    except Exception as e :
        print(e)
        function_responce = "Invalid Function"
    return function_response   

def run_conversation(user_message):
    messages = []
    print(user_message)

    system_message = '''You're an AI that can do everything using function call.
    When you are asked to do something, use the function call you have available
    and then respond with message.''' # first instruction

    message = { "role" : "user",
               "parts" : [{"text": system_message +"\n "+user_message}]}
    messages.append(message)

    data = { "contents": [messages],
            "tools" :
            [{ "functionDeclarations" : task.definitions
              }]
            }
    
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="+key
    response = requests.post(url, json=data)

    if response.status_code != 200:
        print(response.text)

    t1 = response.json()
    if "content" not in t1.get("candidates")[0]:
        print("Error: No content in response")

    message = t1.get("candidates")[0].get("content").get("parts")
    print("message ###############:",message)
    if 'functionCall' in message[0] :
        resp1 = parse_function_response(message)
        return resp1
    else:
        print("no function call")
    

if __name__== "__main__":
    user_message = " "
    print(run_conversation(user_message))

