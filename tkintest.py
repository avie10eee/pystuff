import tkinter as tk
import os



root =tk.Tk()

canvas = tk.Canvas(root, height=500, width=500, bg="#263d42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

def writedoge():
    print("doge")


writedoge = tk.Button(root, text="write doge", padx=10, pady=5, fg="white", bg="#263d42", command=writedoge)
writedoge.pack()

root.mainloop()
