from colorama import init, Fore, Style
import csv
import os

List=[]
FILENAME = "todoList.csv"
init(autoreset=True) 


#========================================================================
#========================================================================



def SHOW():
    with open(FILENAME, mode='r', newline='', encoding='utf-8') as file: 
        todo = list(csv.DictReader(file))

        if not todo:
            print(Fore.CYAN+"Empty list\n")
        else:
            for i,x in enumerate(todo, 1):
                status_color = Fore.GREEN if x['Status'].lower() == "done" else Fore.YELLOW + Style.NORMAL
                print(f"{Fore.LIGHTBLUE_EX}{i}.{Style.RESET_ALL} {x['Task']},\t\t\t Status: {status_color}{x['Status']}{Style.RESET_ALL}")
    

def ADD(thing, status):
    fieldnames = ["Task", "Status"]
    with open(FILENAME, mode='a', newline='') as file:
        csv.DictWriter(file, fieldnames=fieldnames).writerow({"Task":thing , "Status":status})
        return True
    

def DELETE(number):
     with open(FILENAME, mode='r', newline='') as file: 
        todo = list(csv.reader(file))
        if 1 <= number <= len(todo):
            try:
                removed = todo.pop(number )
                print(f"deleted {removed[0]}")
                with open(FILENAME, mode='w', newline='') as file:
                    csv.writer(file).writerows(todo)
            except:
                print(Fore.RED+"could not delete it\n")
        else:
            print(Fore.RED+"invalid input\n")

def change_status(number, new_status):
    with open(FILENAME, mode='r', newline='', encoding="utf-8") as file:
        todo = list(csv.reader(file))

        if 1 <= number <= len(todo):
            try:
                todo[number][1] = new_status
                print(f"Updated '{todo[number][0]}' to status '{new_status}'")

                with open(FILENAME, mode='w', newline='', encoding="utf-8") as file:
                    csv.writer(file).writerows(todo)

            except Exception as e:
                print(Fore.RED+"Could not update it\n", e)
        else:
            print(Fore.RED+"Invalid input\n")

def CHECK(any):
    found = False
    with open(FILENAME, mode='r', newline='', encoding='utf-8') as file: 
        reader = csv.DictReader(file)
        for row in reader:
            if any.lower() in row["Task"].lower():
                status_color = Fore.GREEN if row['Status'].lower() == "done" else Fore.YELLOW + Style.NORMAL
                print(f"{Fore.CYAN}*  {Style.RESET_ALL}{row['Task']}\t\t Status: {status_color}{row['Status']}{Style.RESET_ALL}")
                found = True
    if not found:
        print("No matching tasks found.")



def SHOW_SOME(too):
    found = False
    with open(FILENAME, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Status"].lower() == too.lower():
                status_color = Fore.GREEN if row['Status'].lower() == "done" else Fore.YELLOW + Style.NORMAL
                print(f"{Fore.CYAN}*  {Style.RESET_ALL}{row['Task']}\t\t Status: {status_color}{row['Status']}{Style.RESET_ALL}")
                found = True
    if not found:
        print(f"No tasks found with status '{too}'.")


#========================================================================



# Check if file exists, if not create an empty one
if not os.path.exists(FILENAME):
    print(f"\n{Fore.BLUE} creating file csv")
    with open(FILENAME, mode='w', newline='') as file:
        fieldnames = ["Task", "Status"]
        csv.DictWriter(file , fieldnames=fieldnames).writeheader()


#========================================================================

print(f"{Fore.LIGHTBLUE_EX + Style.BRIGHT}\nWELCOME TO TODO LIST PROGRAM\n {Style.RESET_ALL}")
print(f"{Fore.LIGHTBLUE_EX}1.{Style.RESET_ALL} Show list\n{Fore.LIGHTBLUE_EX}2. {Style.RESET_ALL}Add to list\n{Fore.LIGHTBLUE_EX}3. {Style.RESET_ALL}Delete from list\n{Fore.LIGHTBLUE_EX}4. {Style.RESET_ALL}Mark Done\n{Fore.LIGHTBLUE_EX}5. {Style.RESET_ALL}Search? \n{Fore.LIGHTBLUE_EX}6. {Style.RESET_ALL}devide tasks: \n{Fore.LIGHTBLUE_EX}0. {Style.RESET_ALL}Exit")

while True:    
    try:
        print(Fore.LIGHTBLUE_EX+"***********************************************")
        x = int(input(f"{Fore.GREEN+Style.BRIGHT}  \nChoose one: {Style.RESET_ALL}"))
    except ValueError:
        print(Fore.RED+"Please enter a valid number (1–6).\n")
        continue
    if x == 1:
        print("\n")
        SHOW()
        with open(FILENAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            row_count = sum(1 for _ in reader ) -1
            print(f"{Fore.CYAN + Style.BRIGHT}\nNumber of todo:{Style.RESET_ALL}", row_count)

    elif x == 2:
        add = input(Fore.CYAN + Style.BRIGHT +f"enter what you want to add:{Style.RESET_ALL} ")
        ADD(add, "in progress")

    elif x == 3:
        SHOW()
        y=int(input(Fore.CYAN + Style.BRIGHT +f"\nchose the one you want to delete:{Style.RESET_ALL}"))
        DELETE(y)
    elif x == 4:
        SHOW()
        G = int(input(Fore.CYAN + Style.BRIGHT +f"\nchose the one you want to mark as Done:{Style.RESET_ALL}"))
        change_status(G , 'Done')
    elif x == 5:
        hi = input(Fore.CYAN + Style.BRIGHT +f"\nSearch::{Style.RESET_ALL}")
        CHECK(hi)
    elif x == 6:
        hoo = int(input(Fore.CYAN + Style.BRIGHT +f"\n0 for 'Done' - 1 for on 'on progress':{Style.RESET_ALL}"))
        if hoo == 0:
            soso = "Done"
        elif hoo ==1:
            soso = "in progress"
        else:
            print(Fore.RED +"invalied input\n")
        SHOW_SOME(soso)

    elif x == 0:
        print(f"{Style.RESET_ALL}Goodbye!\n")
        break
    else:
        print(Fore.RED +"invalied input\n")