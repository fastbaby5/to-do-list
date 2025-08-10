# sdhfasdfsdf
import csv
import os

List=[]
FILENAME = "todoList.csv"


#========================================================================
#========================================================================



def SHOW():
    with open(FILENAME, mode='r', newline='') as file: 
        todo = list(csv.reader(file))
        if not todo:
            print("Empty list\n")
        else:
            for i,x in enumerate(todo, 1):
                print(f"{i}.{x[0]}")

def ADD(thing):
    with open(FILENAME, mode='a', newline='') as file:
        csv.writer(file).writerow([thing])
        return True
    
def DELETE(number):
     with open(FILENAME, mode='r', newline='') as file: 
        todo = list(csv.reader(file))
        if 1 <= number <= len(todo):
            try:
                removed = todo.pop(number - 1)
                print(f"deleted {removed[0]}")
                with open(FILENAME, mode='w', newline='') as file:
                    csv.writer(file).writerows(todo)
            except:
                print("invalid input\n")
    

#========================================================================



# Check if file exists, if not create an empty one
if not os.path.exists(FILENAME):
    print("creating file csv")
    with open(FILENAME, mode='w', newline='') as file:
        pass  # creates an empty file


#========================================================================


print("\nWELCOME TO TODO LIST PROGRAM\n")
print("1. Show list\n2. Add to list\n3. Delete from list\n0. Exit")

while True:    
    try:
        print("***********************************************")
        x = int(input("\nChoose one: "))
    except ValueError:
        print("Please enter a valid number (1–4).\n")
        continue
    if x == 1:
        SHOW()

    elif x == 2:
        add = input("enter what you want to add: ")
        ADD(add)

    elif x == 3:
        SHOW()
        y=int(input("chose the one you want to delete\n"))
        DELETE(y)
    elif x == 0:
        print("Goodbye!\n")
        break
    else:
        print("invalied input\n")