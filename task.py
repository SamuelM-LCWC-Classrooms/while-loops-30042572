import time

def task_1():
    password = "Password123"

    # Enter your code here
    guess = ""
    while (guess != password):
        guess = input("Enter the password: ")

    print("Guessed it correctly!")

def task_2(): # Times table
    # Enter your code here
    timesNumber = int(input("Enter your times number: "))
    amount = int(input("How far do you want to go: "))
    counter = 0
    while (counter <= amount):
        counter += 1
        print(timesNumber * counter)

def task_3(): # Count mississippis
    counter = 0
    while counter <= 6:
        counter += 1
        print(str(counter) + " mississippi")
        time.sleep(1)
    return

task_3()