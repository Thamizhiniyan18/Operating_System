# Importing multiprocessing library and math library
import multiprocessing
import math

# Initialising an empty list with global scope
result = []


# Function to calculate the square root of all the elements in the given list
def calculate_square_root(numbers_list):
    print("Process p1 Successfully Created !!!!")
    global result

    # Appending the squares of the numbers in the given list to the global result list
    for number in numbers_list:
        result.append(round(math.sqrt(number), 4))

    # printing the result list inside the process p1
    print("\nThe value of global result list inside the process p1 : {}\n".format(result[:]))


# Initialising a list of data type integer
number_list = [1, 2, 3, 4, 5]

# Creating a process p1
p1 = multiprocessing.Process(target=calculate_square_root, args=(number_list,))

# Starting the process p1
p1.start()

# Waiting for the process p1 to complete
p1.join()

print("The process p1 is Successfully completed its execution!!!!\n")

print("The value of global result list in the main function is : {}".format(result[:]))
