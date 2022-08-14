import speech_recognition as sr
import pyttsx3
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    print(" you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init()
 
# say method on the engine that passing input text to be spoken
engine.say("you said "+r.recognize_google(audio))

# run and wait method, it processes the voice commands.
engine.runAndWait()    