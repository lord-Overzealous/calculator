import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there['text'] = 'hello world\n(click me)'
        self.hi_there['command'] = self.say_hi
        self.hi_there.pack(side='top')

        self.quit = tk.Button(self, text="quit", fg="red", command=self.master.destroy)

        self.quit.pack(side='bottom')

    def say_hi(self):
        print('hi there, everyone!')

### this is the hello world programme for tkinter delete the ' # ' of the three comment below to see it.
## root = tk.Tk()
## app = Application(master=root)
## app.mainloop()

def retrieve():
    print(str(calculator_entry_1.get() + calculator_entry_2.get()))

# will create a new window with the response 
def response_window():
    window = tk.Toplevel()
    window.geometry('250x250')
    opreation_label = tk.Label(window, text = 'the operation you made whas sucessfull')
    opreation_label.pack()

# variable to hold the operation - and result
operation = None # declare variable with no value
result = None

# just to see if it work
var1 = 1
var2 = 4

# function for each of the operation
def add():
    global operation
    operation = "+"
    print("add-work")

    return operation

def sub():
    global operation
    operation = "-"
    print("sub-work")

    return operation

def div():
    global operation
    operation = "/"
    print("div-work")

    return operation

def multi():
    global operation
    operation = "*"
    print('multi-work')

    return operation

# function for the response
def response():
    global var1, var2
    global result
    global operation

    if operation == "+":
        result = var1 + var2
    elif operation == "-":
        result = var1 - var2
    elif operation == "*":
        result = var1 * var2
    elif operation == "/":
        result = var1 / var2
    else:
        result = None
    
    print(result)

    # will make a new window with the result
    def response_window():
        window = tk.Toplevel()
        window.geometry('200x50')
        opreation_label = tk.Label(window, text = 'the result of the operation {0} {1} {2} is {3}\n in other word {0} {1} {2} = {3}'.format(var1, operation, var2, result))
        opreation_label.pack()
    
    response_window()

    return

# create the root ?
root = tk.Tk()
root.geometry('300x250')

# create the frame
frame = tk.Frame(root)
frame.pack() # what does the pack do !

####### resolve the entry problem

resolve_entry = tk.Entry(frame, width = 40)
resolve_entry.insert()
resolve_entry.pack()

resolve_entry_value = resolve_entry.get()

def entry_stop():
    global resolve_entry_value
    print(resolve_entry_value)




##### resolve the entry probleme




# create the user input
calculator_entry_1 = tk.Entry(frame, width = 40)
calculator_entry_1.insert(0,"type your number here: ")
calculator_entry_1.pack(padx = 5, pady = 5)

calculator_entry_2 = tk.Entry(frame, width = 40)
calculator_entry_2.insert(0, 'type number here: ')
calculator_entry_2.pack(padx = 5, pady = 5)

# creart the button for the operation
addition_button = tk.Button(frame, text = 'add', width = 20, command = add)
addition_button.pack(padx = 2.5, pady = 2.5)
soustraction_button = tk.Button(frame, text = 'substract', width = 20, command = sub)
soustraction_button.pack(padx = 2.5, pady = 2.5)

multiplication_button = tk.Button(frame, text = 'multiply', width = 20, command = multi)
multiplication_button.pack(padx = 2.5, pady = 2.5)
division_button = tk.Button(frame, text = 'divide', width = 20, command = div)
division_button.pack(padx = 2.5, pady = 2.5)

# create the submit to give the response
button_submit = tk.Button(frame, text = "submit", width = 30, command = entry_stop)
button_submit.pack(padx = 5, pady = 5)

root.mainloop()
