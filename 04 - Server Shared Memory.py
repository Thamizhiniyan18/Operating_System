# Importing the multiprocessing library
import multiprocessing


# Function to add new student to the student table
def add_student(student, student_list):
    print("Process p1 created ! \n")
    student_list.append(student)
    print("New Student added ! \n")


def print_student_table(student_table):
    print("Process p2 created! \n")
    for student in student_table:
        print("Student Name: {}\nStudent Mark: {} \n".format(student[0], student[1]))


with multiprocessing.Manager() as manager:
    # Creating a list named students_table in the servers memory
    students_table = manager.list([('Joe', 10), ('Doe', 20), ('Foe', 30)])
    # New student to be added to the students_table
    new_student = ('John', 40)

    # Creating the processes p1, p2
    p1 = multiprocessing.Process(target=add_student, args=(new_student, students_table))
    p2 = multiprocessing.Process(target=print_student_table, args=(students_table, ))

    # Starting the process p1
    p1.start()

    # Waiting for the process p1 to complete
    p1.join()

    print("The Process p1 is successfully Executed ! \n")

    # Starting the process p2
    p2.start()

    # Waiting for the process p2 to complete
    p2.join()

    print("The Process p2 is successfully Executed !\n")


