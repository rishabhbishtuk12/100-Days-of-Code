import tkinter as tk

window= tk.Tk()
window.title("Calculator")
window.geometry("400x200")

answer= 0
lastNumber = 0
operator = None

def typeAnswer(value):
    global answer
    answer = f"{answer}{value}"
    answer = int(answer)
    calculation["text"] = answer

def calcAnswer(thisOp):
    global answer, lastNumber,operator
    lastNumber = answer
    answer = 0
    if thisOp == "+":
        operator = "+"
    elif thisOp == "-":
        operator = "-"
    elif thisOp == "*":
        operator = "*"
    elif thisOp == "/":
        operator = "/"
    
    calculation["text"] = answer

    
def calc():
    global answer, lastNumber,operator
    if operator == "+" :
        total=  lastNumber + answer
    elif operator == "-" :
        total=  lastNumber - answer
    elif operator == "*" :
        total=  lastNumber * answer
    elif operator == "/" :
        total=  lastNumber / answer
    answer = total
    calculation["text"]= answer

calculation = tk.Label(text=answer)
calculation.grid(row=0,column=0)

one = tk.Button(text="1",height= 1,width=2, command=lambda: typeAnswer(1))
one.grid(row=1,column=0)

two = tk.Button(text="2",height= 1,width=2, command=lambda: typeAnswer(2))
two.grid(row=1,column=1)

three = tk.Button(text="3",height= 1,width=2, command=lambda: typeAnswer(3))
three.grid(row=1,column=2)

four = tk.Button(text="4",height= 1,width=2, command=lambda: typeAnswer(4))
four.grid(row=2,column=0)

five = tk.Button(text="5",height= 1,width=2, command=lambda: typeAnswer(5))
five.grid(row=2,column=1)

six = tk.Button(text="6",height= 1,width=2, command=lambda: typeAnswer(6))
six.grid(row=2,column=2)

seven = tk.Button(text="7",height= 1,width=2, command=lambda: typeAnswer(7))
seven.grid(row=3,column=0)

eight = tk.Button(text="8",height= 1,width=2, command=lambda: typeAnswer(8))
eight.grid(row=3,column=1)

nine = tk.Button(text="9",height= 1,width=2, command=lambda: typeAnswer(9))
nine.grid(row=3,column=2)

zero = tk.Button(text="0",height= 1,width=2, command=lambda: typeAnswer(0))
zero.grid(row=4,column=1)

add = tk.Button(text="+",height= 1,width=2, command=lambda: calcAnswer("+"))
add.grid(row=1,column=3)

sub = tk.Button(text="-",height= 1,width=2, command=lambda: calcAnswer("-"))
sub.grid(row=1,column=4)

multi = tk.Button(text="*",height= 1,width=2, command=lambda: calcAnswer("*"))
multi.grid(row=2,column=3)

div = tk.Button(text="/",height= 1,width=2, command=lambda: calcAnswer("/"))
div.grid(row=2,column=4)

equals = tk.Button(text="=",height= 1,width=2, command=calc)
equals.grid(row=4,column=3)



tk.mainloop()