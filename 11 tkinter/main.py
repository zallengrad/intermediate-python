from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width="500", height="300")
window.config(padx=100, pady=100)


# label
my_label = Label(text="This Is Label", font=("Arial", 25, "bold"))
my_label.grid(column=0, row=0)
my_label.config(pady=20, padx=20)

# my_label["text"] = "new text"
# my_label.config(text="new text")

# button
def clicked_button ():
    print("button clicked")
    # my_label.config(text="button clicked")
    get = entry.get()
    my_label.config(text=get)

btn = Button(text="click me!", command=clicked_button)
btn.grid(column=1, row=1)
btn.config(pady=20, padx=20)

# new_button
def clicked_button ():
    print("button clicked")
    # my_label.config(text="button clicked")
    get = entry.get()
    my_label.config(text=get)

btn = Button(text="new button", command=clicked_button)
btn.grid(column=2, row=0)
btn.config(pady=20, padx=20)

# entry
entry = Entry(width="20")
entry.grid(column=3, row=3)
# entry.config(pady=20, padx=20)






window.mainloop()