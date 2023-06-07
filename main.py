from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
from converterCode import converter


bgcolor = "lemon chiffon"
choseboxcolor = "cornsilk"
scrollcolor = "cornsilk2"
buttoncolor = "medium spring green"
creditscolor = "lime green"
textcolor = "gray18"
result = ""
steps = ""
baseB = ""
baseH = ""

# Logo
current_directory = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_directory, "Files", "Logo.ico")

root = Tk()
root.title("Base Converter")
root.iconbitmap(icon_path)
root.configure(bg=bgcolor)
root.geometry("1000x700")

# Title
myTitle = Label(root, text="Base Converter", font=("Arial", 30, "underline"), foreground=textcolor)
myTitle.configure(bg=bgcolor)
myTitle.grid(row=0, column=3, sticky="nsew")

# First Text
Label0 = Label(root, text="Initial Number", font=("Arial", 20), foreground=textcolor)
Label0.configure(bg=bgcolor)
Label0.grid(row=1, column=3, sticky="nsew")


# Copy for initial number

def on_entry_click(event):
    if initial_number.get() == "Enter the number":
        initial_number.delete(0, END)
        initial_number.configure(foreground=textcolor)


def copy_text(event):
    root.clipboard_clear()
    root.clipboard_append(initial_number.get())


# The Initial Number
initial_number = Entry(root, borderwidth=3, bg="cornsilk", font=("Arial", 15), foreground=textcolor)
initial_number.insert(0, "Enter the number")
initial_number.grid(row=2, column=3, sticky="nsew")
initial_number.bind("<FocusIn>", on_entry_click)
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
           str(i) + " " for i in range(2, 37)]
root.option_add("*TCombobox*Listbox*Background", choseboxcolor)
root.option_add('*TCombobox*Listbox.font', ('Arial', 15))
root.option_add('*TCombobox*Listbox.foreground', textcolor)
ttk.Style().layout('combostyleO.TCombobox')
ttk.Style().configure('combostyleO.TCombobox', selectforeground=textcolor, selectbackground=choseboxcolor,
                      background=choseboxcolor, foreground=textcolor, padding=4)
style = ttk.Style()
style.theme_create("Theme", parent="alt", settings={
    "TCombobox": {
        "configure": {"selectbackground": choseboxcolor, "fieldbackground": choseboxcolor, "foreground": textcolor,
                      "selectforeground": textcolor},
        "map": {"background": [("readonly", scrollcolor)]}
    },
    "TComboboxListbox": {
        "configure": {"highlightbackground": scrollcolor}
    }
})
style.theme_use("Theme")
style.configure('TCombobox', font=('Arial', 15))
style.configure('my.TCombobox', arrowsize=30)
style.configure('TScrollbar', background=scrollcolor)
style.configure('TScrollbar', troughcolor=scrollcolor)

# buttonFrom
Label1 = Label(root, text="From  Base", font=("Arial", 15), foreground=textcolor)
Label1.configure(bg=bgcolor)
Label1.grid(row=3, column=1, sticky="nsew")
option1 = StringVar()
combobox1 = ttk.Combobox(root, font=('Arial', 15), textvariable=option1, style="combostyleO.TCombobox", values=options,
                         state="readonly", foreground=textcolor)
combobox1.grid(row=4, column=1, sticky="nsew")

# buttonTo
Label2 = Label(root, text="   To  Base   ", font=("Arial", 15), foreground=textcolor)
Label2.configure(bg=bgcolor)
Label2.grid(row=3, column=5, sticky="nsew")
option2 = StringVar()
combobox2 = ttk.Combobox(root, font=('Arial', 15), textvariable=option2, style="combostyleO.TCombobox", values=options,
                         state="readonly", foreground=textcolor)
combobox2.grid(row=4, column=5, sticky="nsew")

# choiceRestrictions
combobox1.bind('<<ComboboxSelected>>', lambda event: update_combobox2())
combobox2.bind('<<ComboboxSelected>>', lambda event: update_combobox1())


def convert():
    global result, steps, baseB, baseH

    # Get the initial number
    numberToConvert = str(initial_number.get())

    # Get the Base from
    baseB = str(combobox1.get())
    baseB = baseB[:2]

    # Get the Base to
    baseH = str(combobox2.get())
    baseH = baseH[:2]

    if baseB != "" and baseH != "":
        result, steps = converter(numberToConvert, int(baseB), int(baseH))
        result_number.configure(state='normal')
        result_number.delete(0, END)
        result_number.insert(0, result)
        result_number.configure(state='readonly')


# buttonConverter
buttonConverter = Button(root, text="Convert", font=("Arial", 15), bg=buttoncolor, foreground=textcolor,
                         command=convert)
buttonConverter.grid(row=4, column=3, sticky="nsew")

# Second Text
Label3 = Label(root, text="Result Number", font=("Arial", 20), foreground=textcolor)
Label3.configure(bg=bgcolor)
Label3.grid(row=5, column=3, sticky="nsew")


# Copy for result number
def copy_text(event):
    root.clipboard_clear()
    root.clipboard_append(result_number.get())


# The Result Number
result_number = Entry(root, borderwidth=3, font=("Arial", 15), foreground=textcolor, readonlybackground="cornsilk")
result_number.insert(0, result)
result_number.grid(row=6, column=3, sticky="nsew")
result_number.bind("<Control-c>", copy_text)
result_number.configure(state='readonly')


# The second window


def open_second_window():
    second_window = Toplevel(root)
    second_window.title('Base Converter - Credits')
    second_window.iconbitmap(icon_path)
    second_window.geometry('860x400')
    second_window.configure(bg=bgcolor)

    # The Title
    myTitle2 = Label(second_window, text="Our Team", font=("Arial", 30, "underline"), foreground=textcolor)
    myTitle2.configure(bg=bgcolor)
    myTitle2.grid(row=0, column=3, sticky="nsew")

    # First Member
    photo1 = ImageTk.PhotoImage(Image.open("Files/Photo1.png"))
    Label4 = Label(second_window, image=photo1, bg=bgcolor)
    Label4.image = photo1
    Label4.grid(row=3, column=2, sticky="nsew")
    Label5 = Label(second_window, text="David Raluca", font=("Arial", 20), bg=bgcolor, foreground=textcolor)
    Label5.grid(row=4, column=2, sticky="nsew")

    # The Second Member
    photo2 = ImageTk.PhotoImage(Image.open("Files/Photo2.png"))
    Label6 = Label(second_window, image=photo2, bg=bgcolor)
    Label6.image = photo2
    Label6.grid(row=3, column=4, sticky="nsew")
    Label7 = Label(second_window, text="Frîncu Marian", font=("Arial", 20), bg=bgcolor, foreground=textcolor)
    Label7.grid(row=4, column=4, sticky="nsew")


# buttonCredits
buttonCredits = Button(root, text="Credits", bg=creditscolor, command=open_second_window, foreground=textcolor)
buttonCredits.grid(padx=5, pady=1, column=0, row=7)

# The third window


def open_third_window():
    global steps
    third_window = Toplevel(root)
    third_window.title('Base Converter - Steps')
    third_window.iconbitmap(icon_path)
    third_window.geometry('1000x500')
    third_window.configure(bg=bgcolor)

    steps_text = Text(third_window, font=("Arial", 20), wrap="word", bg=bgcolor, foreground=textcolor)
    steps_text.grid(row=0, column=0, sticky="nsew")
    steps_text.insert(END, steps)
    steps_text.configure(state="disabled")

    third_window.grid_rowconfigure(0, weight=1)
    third_window.grid_columnconfigure(0, weight=1)


# buttonSteps
buttonSteps = Button(root, text="Steps", bg=creditscolor, command=open_third_window, foreground=textcolor)
buttonSteps.grid(padx=10, pady=1, column=6, row=7)

# Configuration
Grid.rowconfigure(root, 0, weight=1)
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
Grid.columnconfigure(root, 6, weight=1)

root.mainloop()
