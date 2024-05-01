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