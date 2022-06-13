import tkinter as tk
import speech

def but(button_press):
    speech.mix(1)

def but1(button_press):
    speech.mix(2)

def but2(button_press):
    speech.mix(3)

def first():
    m = tk.Tk()

    Labell = tk.label = tk.Label(m,text="Select the below choices",fg="white",bg='black',font=50)
    Labell.place(x=200,y=10)

    button1 = tk.Button(m, text = 'Learn Words', fg ='red',font=100,command=lambda k='':but(k))
    button1.place(x=250,y=100)

    button2 = tk.Button(m, text = 'Learn Spellings', fg ='red',font=100,command=lambda k='':but1(k))
    button2.place(x=250,y=200)

    button3 = tk.Button(m, text = 'Say Sentences', fg ='red',font=100,command=lambda k='':but2(k))
    button3.place(x=250,y=300)

    button4 = tk.Button(m, text = 'Back', fg ='red',font=100,command=m.destroy)
    button4.place(x=500,y=400)

    m.geometry("600x500")
    m.mainloop()