#Tkinter 
from tkinter import *

def button_clicked():
    my_label.config(text= input.get())
    print("I Got Clicked")
window = Tk()
window.title("My First GUI Program")
window.minsize(500,300)

#Label
my_label =Label(text = "I am a label", font= ("Arial", 24, "italic"))
# my_label.place(x= 100, y=200) How to use .place 
my_label.grid(row= 0, column= 0)

#Buttons 
    
    
button = Button(text= "Click Me", command= button_clicked)
button.grid(column=1, row=1)

new_button = Button(text= "Dont CLick", )
new_button.grid(row=0, column= 2)


#Entry
input = Entry(width= 10)
input.insert(END, "Write anything you want")#add dummy text to input fields
input.grid(column=3, row=3)


window.mainloop()