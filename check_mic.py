
index = 1
import speech_recognition as sr

print(sr.Microphone.list_microphone_names())

index = 0
for name in sr.Microphone.list_microphone_names():
    print(index," : ", name)
    #print("Microphone with name\"{1}\" found for `Microphone(deice_index = {0})`".format(index, name))
    index = index + 1