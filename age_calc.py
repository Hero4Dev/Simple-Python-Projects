import time

def year_to_Hours(age):
    return "Your age in Hours is : " + str(age*356*24) + " Hours" 
def year_to_days(age):
    return "Your age in days is : " + str(age*356) + " days"

def methods():
    print("1.Days")
    print("2.Hours")

age_get = int(input("Enter Your Age : "))
methods()
choose = input("Choose A Methode (Choose With Numbers) : ") 
   
if choose == '1' :
    print(year_to_days(age_get))

if choose == '2' :
    print(year_to_Hours(age_get))

    






