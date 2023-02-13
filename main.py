import tkinter
window = tkinter.Tk()

window.title("Test 1")
window.minsize(300, 100)

## Label
my_label = tkinter.Label(text="I am a label.", font=("Courier", 20, "bold"))
my_label.pack()







window.mainloop()
