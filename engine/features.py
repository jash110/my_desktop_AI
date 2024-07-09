from playsound import playsound
import eel
import os
from engine.config import *
from engine.command import *
import pywhatkit as kit
import re
import sqlite3
import webbrowser

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
                    speech("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speech("Opening "+query)
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

def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'                 # regular expression to capture song name
    match = re.search(pattern,command,re.IGNORECASE)         # using search to find match in command
    return match.group(1)                                    # if match found - return song name ; otherwise - return None
