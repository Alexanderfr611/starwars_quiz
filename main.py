import tkinter as gui

# Creating a Gui where you can do the quiz
window = gui.Tk()
greeting = gui.Label(text="Herzlich Willkommen bei dem Star Wars Quiz \n" +
    "Du erhältst nun 10 Fragen zu dem Star Wars Universum, am Ende siehst du wie Mächtig du wirklich bist. \n" +
    "Zuerst beginnen wir mit ein paar Grundlegenden Sachen.",
    bg="black",
    fg="red",
    width=100,
    height=25,
    font=("Arial", 14)
)
greeting.pack()
window.mainloop()





