from tkinter import *
window = Tk()
FONT = ("Courier", 8, "bold")

window.title("Converter")
window.minsize(100, 100)
window.config(padx=20, pady=20)

label1 = Label(text="Unit", font=FONT)
label1.grid(row=2, column=2)

input1 = Entry(width=7)
input1.grid(row=2, column=1)

label2 = Label(text="is equal to", font=FONT)
label2.grid(row=3, column=0)

label3 = Label(text="0", font=FONT, width=7)
label3.grid(row=3, column=1)

label4 = Label(text="Unit", font=FONT)
label4.grid(row=3, column=2)


def calculate():
    in_1 = input1.get()
    if radio_state.get() == 1:
        label1.config(text="Miles")
        label4.config(text="Km")
        miles_to_km = round(float(in_1) * 1.609344, 2)
        label3.config(text= miles_to_km)
    elif radio_state.get() == 2:
        label1.config(text="Km")
        label4.config(text="Miles")
        km_to_miles = round(float(in_1) * 0.62137119, 2)
        label3.config(text=km_to_miles)


button1 = Button(text="Calculate", command=calculate, font=FONT)
button1.grid(row=4, column=1)

radio_state = IntVar()
radiobutton_Miles_To_Km = Radiobutton(text="Miles to KM", value=1, variable=radio_state, command=calculate)
radiobutton_Miles_To_Km.grid(row=0, column=1, rowspan=1, columnspan=2, sticky="nwse")
radiobutton_Km_To_Miles = Radiobutton(text="Km to Miles", value=2, variable=radio_state, command=calculate)
radiobutton_Km_To_Miles.grid(row=1, column=1, rowspan=1, columnspan=2, sticky="nwse")



window.mainloop()
