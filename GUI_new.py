# try:
import tkinter as tk
import GUI_new_2
import pattern
import canvas

m = tk.Tk()

def but(button_press):
    GUI_new_2.first()

def but1(button_press):
    pattern.puzzle()

def but2(button_press):
    canvas.canva()

Labell = tk.Label(m,text="Smart Tutor",fg="white",bg='black',font=50)
Labell.place(x=200,y=10)

button1 = tk.Button(m, text = 'Speech', fg ='red',font=100,command=lambda k='':but(k))
button1.place(x=200,y=100)

button2 = tk.Button(m, text = 'Puzzle', fg ='red',font=100,command=lambda k='':but1(k))
button2.place(x=200,y=200)

button3 = tk.Button(m, text = 'Canvas', fg ='red',font=100,command=lambda k='':but2(k))
button3.place(x=200,y=300)

button4 = tk.Button(m, text = 'Exit', fg ='red',font=100,command=m.destroy)
button4.place(x=400,y=400)

m.geometry("600x500")
m.mainloop()
# except:
#     pass
#     print("fu")    