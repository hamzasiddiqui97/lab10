import tkinter
window = tkinter.Tk()
window.title("Image Or Logo GUI")

icon = tkinter.PhotoImage(file ="Python.png")
label = tkinter.Label(window, image = icon)
label.pack()

window.mainloop()
