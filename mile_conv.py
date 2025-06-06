#simple mile to kilometer converter
from tkinter import *
km = 0
def calculate_distance():
    try:
        km = float(mile_input.get()) * 1.60934
        km = round(km)
        km_num.config(text=km)
    except ValueError:
        km_num.config(text="Numbers only")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width= 300, height=100)
window.config(padx=20, pady=20)

mile_input = Entry(width= 10)
mile_input.grid(row=0, column=1 )

mile_label = Label(text= "Miles", font =("Arial", 15))
mile_label.grid(row=0, column= 2)

equal_label = Label(text= "Is equal to", font =("Arial", 15))
equal_label.grid(row=1, column=0)

km_num = Label(text= "0", font =("Arial", 15),pady=10)
km_num.grid(row=1, column=1)

km_label = Label(text="Km", font =("Arial", 15))
km_label.grid(row= 1, column=2)

button = Button(text="Calculate", command=calculate_distance )
button.grid(row=2, column=1)












window.mainloop()