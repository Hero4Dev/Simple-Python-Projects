number1 = int(input("Enter First Number : "))
operator = input("Enter An Operator : ")
number2 = int(input("Enter Second Number : "))

def add():
    print(number1 + number2)

def minus():
    print(number1 - number2)

def multiply():
    print(number1 * number2)

def subtract():
    print(number1 / number2)


if operator == '+' or operator == 'Add' or operator == 'add' : 
    add()

elif operator == '-' or operator == 'Minus' or operator == 'minus' : 
    minus()

elif operator == '*' or operator == 'multiply' or operator == 'Multiply' : 
    multiply()

elif operator == '/' or operator == 'subtract' or operator == 'Subtract' : 
    subtract()

else: 
    print("An error has occured please try again later")
