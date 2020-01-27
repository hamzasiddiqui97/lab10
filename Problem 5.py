import tkinter
window = tkinter.Tk()
window.title("Binding Functions")

def say_Assalam_o_Alekum():
    tkinter.Label(window, text ="Assalam O Alekum").pack()
    
tkinter.Button(window, text = "Click Me!", command = say_Assalam_o_Alekum).pack()
window.mainloop()
