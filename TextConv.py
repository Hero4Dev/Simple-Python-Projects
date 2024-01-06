print("Welcome To Our Text Converter ! ")
ceperate = "-"
print(ceperate*30)
Text = input("Enter The Text You Want To Convert : ")
print(ceperate*10)
print("Choose A Methode : \n 1.Lenght Of Your Text\n 2.Capitalaze \n 3.find letter in text\n 4.uppercase Your Text \n 5.LowerCase your text \n 6.Check if Digit \n 7.Check is alpha \n 8.Count Letters in a text \n 9.replace Words In A text\n 10.Quit")
print(ceperate*10)
methode = int(input("Choose A Methode : "))
print(ceperate*10)


def Lenght():
    print("Your Text Has : " + str(len(Text)) + " Letters")

def Capit():
    print("Your Text Is Capitalized : " + str(Text.capitalize()))

def find():
    print("Here Is What Our System Found : " + str(Text.find(findtext)))

def upperc():
    print("Your Text Is Now UpperCased :  " + str(Text.upper()))

def lowerc():
    print("Your Text Is Now LowerCased  : " + str(Text.lower()))

def ifdigit():
    print("Is Digit : " + str(Text.isdigit()))

def ifalpha():
    print("Is Alpha : " + str(Text.isalpha()))

def countletters():
    print("Here Is What Our System Found : " + str(Text.count(CountL)) + " letter ")

def replace():
    print("Here is your replaced Text :  " + Text.replace(replacement , replaced))

def quit():
    print("See You Later !")
    pass

def error():
    print("invalid methode")

if methode == 1:
    Lenght()

if methode == 2 :
    Capit()

if methode == 3 :
    findtext = input("Enter The Letter You Want To Find : ")
    find()

if methode == 4 :
    upperc()

if methode == 5 :
    lowerc()

if methode == 6 :
    ifdigit()

if methode == 7 : 
    ifalpha()

if methode == 8 :
    CountL  = input("Enter The Letter You Want To Find In Your Text : ")
    countletters()

if methode == 9 : 
    replacement =  input("Enter The Letter You Want To Replace :  ")
    replaced = input("Enter The Letter You Want To Be Replaced With :  ")
    replace()

if methode == 10 : 
    quit()

