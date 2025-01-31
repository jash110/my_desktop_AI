import pyttsx3                                          # used to make pc speak
import speech_recognition as sr
import eel                                              # used to link backend ( javascript ) to frontend
import time

def speech(text):
    to_speak=pyttsx3.init('sapi5')
    voices=to_speak.getProperty('voices')
    to_speak.setProperty('voice',voices[1].id)
    to_speak.setProperty('rate',174)                    # standard human is 174
    eel.DisplayMessage(text)
    to_speak.say(text)
    eel.receiverText(text)
    to_speak.runAndWait()

def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening.......')
        eel.DisplayMessage('Listening.......')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source,10,6)                # we can speak till 10 sec it will wait , but if i am speaking take note of 6 sec
    
    try:
        print('Recognizing')
        eel.DisplayMessage('Recognizing')
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)

    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose
def allCommands(message=1):

    if message == 1:
        query=takecommand()
        print(query)
        eel.senderText(query)

    else:
        query = message
        eel.senderText(query)

    try:
                         # using open as imp word
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)

        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)

        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact,whatsapp
            message = ""
            contact_no,name=findContact(query)
            if (contact_no !=0):

                if "send message" in query:
                    message='message'
                    speech("What message to send ?")
                    query=takecommand()
                
                elif "phone call" in query:
                    message='whatsapp call'

                else:
                    message='video call'
                
                whatsapp(contact_no,query,message,name)

        else:
            print("not run")
    except:
        print("error")

    eel.ShowHood()

# text = takecommand()
# speech(text)