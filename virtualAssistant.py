import subprocess as sp
import sys

##install modules##

def CallWin() :  
    sp.call('pip install gTTS')
    pyAudioFile = open('PyAudio-0.2.11-cp39-cp39-win_amd64.whl', 'r')
    sp.call('pip install '+pyAudioFile.name)
    sp.call('pip install SpeechRecognition')
    sp.call('pip install wikipedia')



#CallWin()


## import modules ##

from gtts import gTTS
import pyaudio, wikipedia as wiki, os, datetime, calendar, warnings
import speech_recognition as speech
from io import BytesIO

warnings.filterwarnings('ignore')

def getAudioTT():
    r = speech.Recognizer()

    with speech.Microphone() as source :
        print('say something')
        audio = r.listen(source)
    text  = r.recognize_google(audio)

    # try catch I'll put it later

    return text

#this is just a test function so .. & it works fine

def convertTTS():  
    text = getAudioTT()
    print('you said : '+text)
    audioPlay = BytesIO()
    tts = gTTS(text, lang='bn', slow=False)
    tts.save('convertedAudio.mp3')
    os.system('start convertedAudio.mp3')


convertTTS()