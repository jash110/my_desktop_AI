from playsound import playsound
import eel

# ply intro sound

@eel.expose                                                     ## can use this in main.js as we have exposed it
def playIntro():
    music_dir ="front\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)
