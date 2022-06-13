import pyttsx3
import tkinter as tk
import speech_recognition as sr

t = 1

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand(entry):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        entry.config(text="")
        entry.config(text="Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        entry.config(text="")
        entry.config(text="Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        entry.config(text="")
        entry.config(text="User said:")
        entry.config(text="")
        entry.config(text=query)

    except Exception as e:
        entry.config(text="")
        speak("sir please Say that again...")
        entry.config(text="sir please Say that again...")
        return "None"
    return query

def mixx(p,tmpp,entry):
    if p == 1:
        i = 0
        f = open("E:/word.txt", "r")
        words = f.read()
        words_list = words.split(",")
        while i <= 10:
            entry.config(text="")
            speak("say " + words_list[i])
            print(words_list[i])
            entry.config(text="say " + words_list[i])
            q = takeCommand(entry).lower()
            print(q)
            if q == 'stop':
                break
            if words_list[i] in q:
                entry.config(text="")
                speak("very good")
                entry.config(text="very good")
            else:
                entry.config(text="")
                speak("go again")
                entry.config(text="go again")
                i = i - 1
            i = i + 1

    elif p == 2:
        i = 0
        f = open("E:/word.txt", "r")
        words = f.read()
        words_list = words.split(",")
        while i <= 10:
            entry.config(text="")
            speak("say " + words_list[i])
            entry.config(text="say " + words_list[i])
            q = takeCommand(entry).lower()
            if q == 'stop':
                break
            flag = 0
            j = 0
            k = 0
            while j < len(words_list[i]):
                if q[k] != words_list[i][j] and q[k] != ' ':
                    flag = 1
                    break
                elif q[k] == ' ':
                    k = k + 1
                else:
                    j = j + 1
                    k = k + 1

            if flag == 0:
                entry.config(text="")
                speak("very good")
                entry.config(text="very good")
            else:
                entry.config(text="")
                speak("go again")
                entry.config(text="go again")
                i = i - 1
            i = i + 1

    else:
        i = 0
        f = open("E:/sentence.txt", "r")
        words = f.read()
        words_list = words.split(",")
        while i <= 10:
            entry.config(text="")
            speak("say " + words_list[i])
            entry.config(text="say " + words_list[i])
            q = takeCommand(entry).lower()
            if q == 'stop':
                break
            flag = 0
            j = 0
            while j < len(words_list[i]):
                if q[j] != words_list[i][j]:
                    flag = 1
                    break
                j = j + 1

            if flag == 0:
                entry.config(text="")
                speak("very good")
                entry.config(text="very good")
            else:
                entry.config(text="")
                speak("go again")
                entry.config(text="go again")
                i = i - 1
            i = i + 1

def mix(p):
    m = tk.Tk()

    entry = tk.Label(m, fg="black", font=50)
    entry.place(x=200, y=100)

    button1 = tk.Button(m, text='Start', fg='red', font=100, command=lambda k='':mixx(p,k,entry))
    button1.place(x=200, y=200)

    m.geometry("500x400")
    m.mainloop()
