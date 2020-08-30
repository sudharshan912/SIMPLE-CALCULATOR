

from tkinter import *
root = Tk()
root.title("MY CALCULATOR")

Number = Entry(root, width=60,  borderwidth=5)
Number.grid(row=0, column=0, columnspan=4)
Doneby = Label(root, text="Done by :R M Sudharshan", pady=30)

# FUNCTIONS

value = 0  # internal calculation value

final = 0  # equal to value

process = 0
# process=0 ==> add
# process=1 ==> subtract
# process=2 ==> multiply
# process=3 ==> divide

point = 0  # decimal place exist in number or not


def buttonPressed(number):
    crnt = Number.get()
    Clear(1)
    Number.insert(0, str(crnt)+str(number))


def backspacePressed():
    crnt = Number.get()
    crnt = crnt[: -1]
    Clear(1)
    Number.insert(0, str(crnt))


def dotPressed():
    global point
    crnt = Number.get()
    Clear(1)
    if(point != 1):
        Number.insert(0, str(crnt)+".")
    if(point == 1):
        Number.insert(0, str(crnt))

    point = 1
    # if(point == 0):
    #     point = 1
    #     Number.insert(0, str(crnt)+".")


def Process(numbers):
    global point
    point = 0
    global process
    global value
    process = numbers
    if (numbers == 0):  # add
        value = value+float(Number.get())
        Clear(1)
        # Number.insert(0, value)
        print(value)
    if (numbers == 1):  # subtract
        if(value != 0):
            value = value-float(Number.get())
        if(value == 0):
            value = value+float(Number.get())
        Clear(1)
        # Number.insert(0, value)
        print(value)
    if (numbers == 2):  # multiply
        if(value != 0):
            value = value*float(Number.get())
        if(value == 0):
            value = value+float(Number.get())
        Clear(1)
        # Number.insert(0, value)
        print(value)
    if (numbers == 3):  # multiply
        if(value != 0):
            value = value/float(Number.get())
        if(value == 0):
            value = float(Number.get())
        Clear(1)
        # Number.insert(0, value)
        print(value)


def Equal():
    global point
    point = 0
    global process
    global value
    global final
    if (process == 0):
        final = value+float(Number.get())
        value = 0
        Clear(1)
        Number.insert(0, final)
        print("value = "+value)
    if (process == 1):
        final = value-float(Number.get())
        value = 0
        Clear(1)
        Number.insert(0, final)
        print("value = "+final)
    if (process == 2):
        final = value*float(Number.get())
        value = 0
        Clear(1)
        Number.insert(0, final)
        print("value = "+final)
    if (process == 3):
        final = value/float(Number.get())
        value = 0
        Clear(1)
        Number.insert(0, final)
        print("value = "+final)


def Clear(num):
    global value
    Number.delete(0, END)
    print(num)
    if(num == 0):
        value = 0


    # create buttons
button_0 = Button(root, text="0", padx=60, pady=20,
                  command=lambda: buttonPressed(0))
button_1 = Button(root, text="1", padx=60, pady=20,
                  command=lambda: buttonPressed(1))
button_2 = Button(root, text="2", padx=60, pady=20,
                  command=lambda: buttonPressed(2))
button_3 = Button(root, text="3", padx=60, pady=20,
                  command=lambda: buttonPressed(3))
button_4 = Button(root, text="4", padx=60, pady=20,
                  command=lambda: buttonPressed(4))
button_5 = Button(root, text="5", padx=60, pady=20,
                  command=lambda: buttonPressed(5))
button_6 = Button(root, text="6", padx=60, pady=20,
                  command=lambda: buttonPressed(6))
button_7 = Button(root, text="7", padx=60, pady=20,
                  command=lambda: buttonPressed(7))
button_8 = Button(root, text="8", padx=60, pady=20,
                  command=lambda: buttonPressed(8))
button_9 = Button(root, text="9", padx=60, pady=20,
                  command=lambda: buttonPressed(9))

button_point = Button(root, text=".", padx=62, pady=20,
                      command=dotPressed)
button_c = Button(root, text="C", padx=60, pady=20, command=lambda: Clear(0))
button_multiply = Button(root, text="X", padx=21, pady=20,
                         command=lambda: Process(2))
button_add = Button(root, text="+", padx=20, pady=20,
                    command=lambda: Process(0))
button_subtract = Button(root, text="-", padx=22, pady=20,
                         command=lambda: Process(1))
button_equal = Button(root, text="=", padx=60, pady=20, command=Equal)
button_backspace = Button(root, text="BACKSPACE",
                          padx=60, pady=20, command=backspacePressed)
button_divide = Button(root, text="/", padx=20, pady=20,
                       command=lambda: Process(3))


# display button
Doneby.grid(row=6, column=0, columnspan=2)
button_0.grid(row=4, column=1)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_point.grid(row=4, column=0)
button_c.grid(row=4, column=2)
button_multiply.grid(row=1, column=3)
button_add.grid(row=2, column=3)
button_subtract.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_equal.grid(row=5, column=0, columnspan=4)
button_backspace.grid(row=6, column=2, columnspan=2)


root.mainloop()
