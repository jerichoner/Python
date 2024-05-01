
#!/usr/bin/env python3
#/bin/python3 "/home/user/Рабочий стол/Practice/Lect/lesons18.1.py"

import tkinter as tk

def closeWindow():
    window.destroy()

window = tk.Tk()
window.title("First window")
window.geometry("800x600")

button = tk.Button(window, text="Push me", command=closeWindow)
label = tk.Label(window, text="Go away!")

button.pack()
label.pack()

window.mainloop()
