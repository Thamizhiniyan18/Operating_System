# Program to calculate the sum of cube of all the numbers in a given list

# Importing the multiprocessing library
import multiprocessing


def calculate_cube(given_number_list, result_object, sum_of_cubes):
    print("\nEntered the process 1 !!!! \n")
    for index, n in enumerate(given_number_list):
        result_object[index] = int(n) * int(n) * int(n)

    sum_of_cubes.value = sum(result_object)

    print("The value of result inside the thread/process p1 : {}".format(result_object[:]))
    print("The value of sum_of_cubes inside the thread/process p1 : {}".format(sum_of_cubes.value))


number_list_string = input("Enter the elements of the list : ")
number_list = number_list_string.split()

# Creating an Array of data type int of size 5
result = multiprocessing.Array('i', 5)

# Creating Value of data type int of size 1
cube_sum = multiprocessing.Value('i')

# Creating the Process p1
p1 = multiprocessing.Process(target=calculate_cube, args=(number_list, result, cube_sum))

# Starting the process p1
p1.start()

# Waiting for the process p1 to finish
p1.join()

print("\nThe Process executed Successfully !!!\n")

print("The value of result inside the Main/parent function : {}".format(result[:]))
print("The value of sum_of_cubes inside the Main/parent function : {}".format(cube_sum.value))
