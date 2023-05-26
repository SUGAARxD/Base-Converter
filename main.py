from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os

# Logo
current_directory = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_directory, "Files", "Logo.ico")

root = Tk()
root.title("Base Converter")
root.iconbitmap(icon_path)
root.configure(bg="tan1")
root.geometry("920x700")

# Title
myTitle = Label(root, text="Base Converter", font=("Arial", 30, "underline"))
myTitle.configure(bg="tan1")
myTitle.grid(row=0, column=3, sticky="nsew")

# First Text
Label0 = Label(root, text="Initial Number", font=("Arial", 20))
Label0.configure(bg="tan1")
Label0.grid(row=1, column=3, sticky="nsew")

# Copy for initial number


def copy_text(event):
    root.clipboard_clear()
    root.clipboard_append(initial_number.get())


# The Initial Number
initial_number = Entry(root, borderwidth=3, font=("Arial", 15), bg="tan2")
initial_number.insert(0, "Enter the number")
initial_number.grid(row=2, column=3, sticky="nsew")
initial_number.bind("<Control-c>", copy_text)

# Buttons Functionality


def update_combobox2():
    selected_option = combobox1.get()
    combobox2['values'] = [option for option in options if option != selected_option]


def update_combobox1():
    selected_option = combobox2.get()
    combobox1['values'] = [option for option in options if option != selected_option]


# Design Buttons
options = [str(i) + " (binary)" if i == 2 else
           str(i) + " (octal)" if i == 8 else
           str(i) + " (decimal)" if i == 10 else
           str(i) + " (hex)" if i == 16 else
           str(i) for i in range(2, 37)]
root.option_add("*TCombobox*Listbox*Background", 'orange')
root.option_add('*TCombobox*Listbox.font', ('Arial', 15))
ttk.Style().layout('combostyleO.TCombobox')
ttk.Style().configure('combostyleO.TCombobox', selectforeground='black', selectbackground='orange', background='orange',
                      foreground='orange', padding=4)
style = ttk.Style()
style.theme_create("Orange", parent="alt", settings={
 "TCombobox": {
        "configure": {"selectbackground": "orange", "fieldbackground": "orange", "foreground": "black",
                      "selectforeground": "black"},
        "map": {"background": [("readonly", "orange")]}
 },
 "TComboboxListbox": {
         "configure": {"highlightbackground": "orange"}
 }
})
style.theme_use("Orange")
style.configure('TCombobox', font=('Arial', 15))
style.configure('my.TCombobox', arrowsize=30)
style.configure('TScrollbar', background='orange')
style.configure('TScrollbar', troughcolor='orange')

# buttonFrom
Label1 = Label(root, text="From  Base", font=("Arial", 15))
Label1.configure(bg="tan1")
Label1.grid(row=3, column=1, sticky="nsew")
option1 = StringVar()
combobox1 = ttk.Combobox(root, font=('Arial', 15), textvariable=option1, style="combostyleO.TCombobox", values=options,
                         state="readonly")
combobox1.grid(row=4, column=1, sticky="nsew")

# buttonTo
Label2 = Label(root, text="   To  Base   ", font=("Arial", 15))
Label2.configure(bg="tan1")
Label2.grid(row=3, column=5, sticky="nsew")
option2 = StringVar()
combobox2 = ttk.Combobox(root, font=('Arial', 15), textvariable=option2, style="combostyleO.TCombobox", values=options,
                         state="readonly")
combobox2.grid(row=4, column=5, sticky="nsew")

# choiceRestrictions
combobox1.bind('<<ComboboxSelected>>', lambda event: update_combobox2())
combobox2.bind('<<ComboboxSelected>>', lambda event: update_combobox1())

# buttonConverter
buttonConverter = Button(root, text="Convert", font=("Arial", 15), bg="medium sea green")
buttonConverter.grid(row=4, column=3, sticky="nsew")

# Second Text
Label3 = Label(root, text="Result Number", font=("Arial", 20))
Label3.configure(bg="tan1")
Label3.grid(row=5, column=3, sticky="nsew")

# Copy for result number


def copy_text(event):
    root.clipboard_clear()
    root.clipboard_append(result_number.get())


# The Result Number
result_number = Entry(root, borderwidth=3, font=("Arial", 15), bg="tan2")
number2 = 13
result_number.insert(END, str(number2))
result_number.grid(row=6, column=3, sticky="nsew")
result_number.bind("<Control-c>", copy_text)

# The second window


def open_second_window():
     second_window = Toplevel(root)
     second_window.title('Base Converter - Credits')
     second_window.iconbitmap(icon_path)
     second_window.geometry('860x400')
     second_window.configure(bg='tan1')

     #The Title
     myTitle2= Label(second_window, text="Our Team", font=("Arial", 30, "underline"))
     myTitle2.configure(bg="tan1")
     myTitle2.grid(row=0, column=3, sticky="nsew")

     # First Member
     photo1 = ImageTk.PhotoImage(Image.open("Files/Photo1.png"))
     Label4 = Label(second_window, image=photo1, bg='tan1')
     Label4.image = photo1
     Label4.grid(row=3, column=2, sticky="nsew")
     Label5 = Label(second_window, text="David Raluca", font=("Arial", 20), bg='tan1')
     Label5.grid(row=4, column=2, sticky="nsew")

     # The Second Member
     photo2 = ImageTk.PhotoImage(Image.open("Files/Photo2.png"))
     Label6 = Label(second_window, image=photo2, bg='tan1')
     Label6.image = photo2
     Label6.grid(row=3, column=4, sticky="nsew")
     Label7 = Label(second_window, text="Frîncu Marian", font=("Arial", 20), bg='tan1')
     Label7.grid(row=4, column=4, sticky="nsew")


# buttonCredits
buttonCredits = Button(root, text="Credits", bg='medium sea green', command=open_second_window)
buttonCredits.grid(padx=5, pady=1)

# Configuration
Grid.rowconfigure(root, 0, weight=0)
Grid.rowconfigure(root, 1, weight=1)
Grid.rowconfigure(root, 2, weight=1)
Grid.rowconfigure(root, 3, weight=1)
Grid.rowconfigure(root, 4, weight=1)
Grid.rowconfigure(root, 5, weight=1)
Grid.rowconfigure(root, 6, weight=1)
Grid.rowconfigure(root, 7, weight=1)
Grid.columnconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 2, weight=2)
Grid.columnconfigure(root, 3, weight=1)
Grid.columnconfigure(root, 4, weight=2)
Grid.columnconfigure(root, 5, weight=1)
Grid.columnconfigure(root, 6, weight=10)

root.mainloop()
