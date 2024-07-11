from pipes import quote
import subprocess
from playsound import playsound
import eel
import os
from engine.config import *
from engine.command import *
from engine.helper import *
import pywhatkit as kit
import sqlite3
import webbrowser
from engine.helper import extract_yt_term
import pvporcupine
import pyaudio
import struct
import time
import pyautogui
from hugchat import hugchat

con = sqlite3.connect("myai.db")
cursor = con.cursor()

# ply intro sound

@eel.expose                                                     ## can use this in main.js as we have exposed it
def playIntro():
    music_dir ="front\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

def openCommand(query):
    query=query.replace(ASSISTANT_NAME, "")
    query=query.replace("open", "")
    query.lower()

    app_name = query.strip()

    if app_name != "":

        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speech("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speech("Opening"+query)
                    webbrowser.open(results[0][0])

                else:
                    speech("Opening"+query)
                    try:
                        os.system('start '+query)
                    except:
                        speech("not found")
        except:
            speech("some thing went wrong")

def PlayYoutube(query):
    find= extract_yt_term(query)
    speech("Playing "+find+" on youtube")
    kit.playonyt(find)

def hotword():
    porcupine = None
    paud = None
    audio_stream = None
    try:
        # Your access key from the Picovoice Console
        

        # Load custom wake word model
        keyword_path = "C:\\Users\\jash1\\OneDrive\\Desktop\\JPS\\front\\assets\\hotwords\\athena.ppn"
        
        porcupine = pvporcupine.create(
            # access_key=access_key,
            keyword_paths=[keyword_path]
        )

        paud = pyaudio.PyAudio()
        audio_stream = paud.open(rate=porcupine.sample_rate, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=porcupine.frame_length)

        # Loop for streaming
        while True:
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)

            # Processing keyword from mic 
            keyword_index = porcupine.process(keyword)

            # Checking if keyword detected
            if keyword_index >= 0:
                print("Hotword 'athena' detected")

                # Pressing shortcut key win+j
                pyautogui.keyDown("win")
                pyautogui.press("j")
                time.sleep(2)
                pyautogui.keyUp("win")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()


# Load custom wake word model
        #porcupine = pvporcupine.create(
        #    keywords=["hey google"]
        #)


def findContact(query):
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'whatsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        
        if results:
            mobile_number_str = str(results[0][0])
            
            if not mobile_number_str.startswith('+91'):
                mobile_number_str = '+91' + mobile_number_str
            
            print(mobile_number_str)
            return mobile_number_str, query
        else:
            print("Contact not found in database")
            return "Contact not found", query
        
    except Exception as e:
        print(f"An error occurred: {e}")
        speech('not exist in contacts')
        return "Error", query
    
# whatsapp
def whatsapp(mobile_no,message,flag,name):

    if flag=='message':
        target_tab = 12
        athena_message = "message sent succesfully to"+name
    
    elif flag=='whatsapp call':
        target_tab = 7
        message=""
        athena_message = "calling" +name
    
    else:
        target_tab = 6
        message=""
        athena_message = "starting video call with"+name

    # encode message for url
    encoded_message = quote(message)                                                    # hi how are you , so in google also it breaks so url is needed so use quote to make url

    #construct url
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    #full command
    full_command= f'start "" "{whatsapp_url}"'

    # open whatsapp with made url using cmd.exe
    subprocess.run(full_command, shell=True)                # shell=True so not visible in cmd; doing twice because it opens whatsapp and doesnt send message so doing twice for safeside.
    time.sleep(5)
    subprocess.run(full_command, shell=True)

    pyautogui.hotkey('ctrl','f')                    # to search when not on search line

    for i in range(1,target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speech(athena_message)

# chatbot
def chatbot(query):
    user_input=query.lower()                                              # only small letters no capital letters
    chatbot=hugchat.ChatBot(cookie_path="engine\cookies.json")            
    id=chatbot.new_conversation()                                         
    chatbot.change_conversation(id)
    response=chatbot.chat(user_input)
    return response

    

    


