# Importing Multiprocessing Library and OS library
import multiprocessing
import os


# Function for calculating the square of a number
def square(number):
    print("\nParent Process ID After the First Process is created : {}".format(os.getppid()))
    print("Child Process ID After the First Process is created : {}".format(os.getpid()))
    print("=\nThe Square of the given number is : {}\n".format(number * number))
    print("The First Process is Completed!!!!\n")


# Function for calculating the cube of a number
def cube(number):
    print("\nParent Process ID After the Second Process is created : {}".format(os.getppid()))
    print("Child Process ID After the Second Process is created : {}".format(os.getpid()))
    print("\nThe Cube of the given number is : {}\n".format(number * number * number))
    print("The Second Process is Completed!!!!\n")


# Getting the number from the user
print("Parent Process ID Before the Processes are created : {}".format(os.getppid()))
print("Child Process ID Before the Processes are created : {}".format(os.getpid()))
n = int(input("\nEnter a number to calculate its Square and Cube : "))


# Creating processes
p1 = multiprocessing.Process(target=square, args=(n, ))
p2 = multiprocessing.Process(target=cube, args=(n, ))


# Starting the processes
p1.start()
p2.start()


# Waiting for the process until it finishes and returns
p1.join()
p2.join()

print("\nThe processes are executed Successfully")

