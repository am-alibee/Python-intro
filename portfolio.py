import pyttsx3

def speak(word):
    pyttsx3.speak(word)
    
speak("Good morning Who am i on to?")

name = input('Who am i on to?')

speak('welcome' + name + "how may i help you?")