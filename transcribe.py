import speech_recognition as sr
from os import path
from pydub import AudioSegment
'''
# convert mp3 file to wav                                                       
sound = AudioSegment.from_mp3("gitaudio2.mp3")
sound.export("gitaudio2.wav", format="wav")
'''

# transcribe audio file                                                         
#AUDIO_FILE = "../gitaudio2.wav"
#Insert audio location here
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "ans_50.wav")


# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  

        print("Transcription: " + r.recognize_google(audio))
       