import tkinter
import tkinter.messagebox
window = tkinter.Tk()
window.title("Alert Message GUI")

tkinter.messagebox.showinfo("Alert Message", "This is just a alert message!")
response = tkinter.messagebox.askquestion("Simple Question","Do you love Python?")
if response == "Yes":
    tkinter.Label(window, text = "You love Python!").pack()
else:
    tkinter.Label(window, text = "You don't love Python!").pack()
    

window.mainloop()
