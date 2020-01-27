import tkinter
window = tkinter.Tk()
window.title("My GUI with Menu")
def function():
    pass
root_menu = tkinter.Menu(window)
window.config(menu = root_menu)

file_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label ="File", menu = file_menu)
file_menu.add_command(label = "New file....",command = function)
file_menu.add_command(label = "Open files", command = function)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = window.quit)

edit_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Undo", command = function)
edit_menu.add_command(label = "Redo", command = function)

window.mainloop()
