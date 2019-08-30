from gtts import gTTS
import os

print("Enter Your Name :")
name = input()
greeting = "We humbly welcome you to this wonderful family " + name
#print (greeting)

language = "en"

audio = gTTS(text = greeting, lang = language, slow = False)

audio.save("welcome.mp3")
os.system("mpg321 welcome.mp3")