# This Project Was Build By @Hero4Dev On Github#
# ---------------------------------------------#

# Importing Needed Modules
import time
from colorama import Fore, Back, Style
from datetime import datetime
import random
from color_settings import *

#defining Some Unnecessary Variabeles
x = '-'
Task = []
get_time = datetime.now()

#Making The Core Program
while True:
    print(x*25)
    print("Welcome To Our To-Do App")
    print(x*25)
    print(" 1.Add A Task\n 2.Mark A Task As Completed\n 3.See All Current Tasks \n 4.Delete Task \n 5.Settings \n 6.Projects Credits \n 7.Quit")
    print(x*25)
    User_input = input("Choose An Option : ")


#The Add Function To Add A Task To Our 'Task' List
    def add():
            print(x*25)
            add_task = input("Add A Task To Start : ")
            Adding = Task.append(add_task)
            print(x*25)
            print('Task Added Succsesfully ! ')
            print(x*25)
            check_added_task = input('Do You Want To Check Your Just Added Task ? y/n ')
            check_added_task.lower
            print(x*25)
            if check_added_task == 'y':
                 print("Here Is Your Current Going Tasks - " + str(Task) + " Added Time : " + Fore.GREEN ,str(get_time) + Style.RESET_ALL )
            elif check_added_task == 'n':
                print("Alright, Going Back To Home Page ! ")
            else:
                 ("An Error Occured Going Back ! ")
            time.sleep(1)
    
    
    def Mark_as_completed():
        print(x*25)
        choose_task = str(input("Choose A Task To Mark : "))
        if choose_task in Task:
            print(x*25)
            print("Task : " + str(choose_task) + Fore.RED ,' - Not Completed ' + Style.RESET_ALL + str(get_time))
            print(x*25)
            ask_user_to_mark_task = input("Do You Want To Mark This Task As Completed? y/n : ")
            if ask_user_to_mark_task == 'y':
                print(x*25)
                Completed_tasks = print("Task : " + str(choose_task) + Fore.GREEN ,' - Completed ' + Style.RESET_ALL + str(get_time))
                Task.remove(choose_task)
            elif ask_user_to_mark_task == 'n':
                print("Alright, Going Back To Home Page ")
            else:
                pass
        else:
             print(x*25)
             print('There Is No Such A Task With That Name : ' + Fore.RED + choose_task , Style.RESET_ALL )  
        pass


    def see_all_current_tasks():
         print(x*25)
         if not Task:
              print("No Tasks Are Currently Available ! ")
         else:
            for element in Task :
             print("Task : " " " + Fore.GREEN + str(element) + Style.RESET_ALL + " - " + "Current Task Time : " + str(get_time))

    def delete_task():
        print(x*25)
        choose_task_to_delete = input("Enter A Task To Delete  : ")
        print(x*25)
        if choose_task_to_delete in Task:
            Task.remove(choose_task_to_delete)
            print("Task Was Deleted Succsesfully ! ")
        else:
            pass
                
    #1.Add A Task
    if User_input == '1' :
        add()

    #2.Mark A Task As Completed
    elif User_input == '2':
        Mark_as_completed()

    #3.see all current tasks
    elif User_input == '3':
        see_all_current_tasks() 
             
    #4.Delete A Task
    elif User_input == '4':
        delete_task()

    #5.Settings
    elif User_input == '5':
        print(" 1.Clear All Task \n 2.Change App Color \n 3.How To Use Our App \n 4.Quit Settings ")
        print(x*25)
        settings_input = input("Choose An Option : ")

        if settings_input == '1':
            clear_task = input("Are You Sure You Want To Clear All Current Tasks ? y/n : ")
            if clear_task == 'y':
                Task.clear
                print(x*25)
                print("Tasks Are Cleared Succssesfully ! ")
            elif clear_task == 'n':
                print(x*25)
                print("Going Back To Home Page ! ")
            
            Task.clear
        elif settings_input == '2':
            print(x*25)
            print("Available Colors : \n 1.Red \n 2.Green \n 3.Blue \n 4.Yellow \n 5.Reset Colors \n 6.Quit")
            print(x*25)
            color_input = input("Choose A color : ") 
            print(x*25)
            if color_input == '1':
                call_red()
            elif color_input == '2':
                call_green()
            elif color_input == '3':
                call_blue()
            elif color_input == '4':
                call_yellow()
            elif color_input == '5':
                style_reset()
            elif color_input == '6':
                ...
            else:
                print(x*25)
                print("Invalid Choice !")
        
        elif settings_input == '3':
            print(x*50)
            print(" Warning ! \n This App Is On Demo Version And You May stumble appon Some Bugs\n if You Do, Please Make Sure To Contact Us As Soon As Possible.  ")
            print(x*50)
            print("How To Use Our App ? \n  1.Add Task : In Here You Can Add Tasks To Your Tasks List They \n  Will Be Marked As Not Completed As Default \n  2.Mark A Task As Completed : In Here You Can Choose A Task , note that if you did not type the exact Task Name \n  written before it may not work and also If You Set A Task As Completed It Will Be Deleted From The Tasks List.\n  3.See All Current Tasks : In Here You Can See All Your Added Tasks With Their Added Time. \n  4.Delete Task : In Here You Can Delete Any Task You Added Before.  ")
        elif settings_input == '4':
            pass
        
        else:
            print(x*25)
            print("Invalid Choice ")

        
    #6.Credits
    elif User_input == '6':
         print(x*25)
         print(Fore.GREEN + 'This Program Is Made By @Hero4Dev On Github' , Style.RESET_ALL)

    #7.Quit
    elif User_input == '7':
        print(x*25)
        check_if_want_to_exit = input("Do You Really Want To Exit Our App Your Current Tasks Will Be Gone. y/n : ")
        print(x*25)
        if check_if_want_to_exit == 'y':
            print("Thank You For Using Our App !")
            break
        elif check_if_want_to_exit == 'n':
             print("Alright Going Back ! ")
             pass
        else : 
             print(x*25)
             print("Returning To Home Page ! ")
             print(x*25)
             
    else:
         print(x*25)
         print("Invalid Option , Please Choose A valid Option")