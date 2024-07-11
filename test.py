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

con = sqlite3.connect("myai.db")
cursor = con.cursor()

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

    
findContact("prsnI")