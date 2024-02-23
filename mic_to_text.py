
import speech_recognition as sr

recognizer = sr.Recognizer()
def mic1():
    with sr.Microphone(device_index=1) as source :
        print ("say something: ")
        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)
        print("Recognizing....")
        text = recognizer.recognize_google(audio)
        print("you said",text)
        return text
    
if __name__=="__main__":   
    mic1()

