# Initialising an Objects list
objects = []


# Defining a class Sequence
class File(object):
    # Defining a constructor
    def __init__(self, name, size, starting_memory_block):
        self.name = name  # Class Members
        self.size = size  # Class Members
        self.starting_memory_block = starting_memory_block  # Class Members
        self.ending_memory_block = self.starting_memory_block + self.size  # Class Members


# Function for Creating a File
def create(variable):
    switch = True  # Temporary Variable
    switch_1 = True  # Temporary Variable
    name = None  # Initialising an empty variable
    starting_allocated_location = None  # Initialising an empty variable

    while switch:
        name = input("Enter the File Name : ")
        for i in range(len(objects)):
            # Checking whether the entered file name already exists
            if name == objects[i].name:
                print("File name already exists, please enter another name")
                switch_1 = False
                break
            switch_1 = True

        if switch_1:
            switch = False

    switch_2 = True  # Temporary Variable
    switch_3 = True  # Temporary Variable

    while switch_2:
        starting_allocated_location = int(input("Enter the Starting Memory Location : "))
        for i in range(len(objects)):
            # Checking whether the entered file name already exists
            if objects[i].starting_memory_block <= starting_allocated_location <= objects[i].ending_memory_block:
                print("The entered memory location is already allocated, please enter another memory location")
                switch_3 = False
                break
            switch_3 = True

        if switch_3:
            switch_2 = False

    try:
        size = int(input("Enter the size : "))
    except ValueError:
        print("Enter a Valid Size")
        size = int(input("Enter the size : "))

    objects.append(File(
        name,
        size,
        starting_allocated_location
    ))
    variable += 1


# Function for Deleting a File
def delete(variable):
    variable -= 1
    objects.remove(objects[variable])


# Function for Displaying all the files
def display():
    print("".center(70, '-'))
    print("|", "File Name".center(20), "|", "Size".center(20), "|", "Allocated Memory".center(20), "|", end="\n")
    print("".center(70, '-'))
    for obj in objects:
        print("".center(70, '-'))
        print(
            "|",
            f"{obj.name} ".center(20),
            "|",
            f"{obj.size} MB".center(20),
            "|",
            f"{obj.starting_memory_block} - {obj.ending_memory_block}".center(20),
            "|"
        )
        print("".center(70, '-'))


# Main Function
def main():
    variable = 0
    while True:
        print("""\nSequential File Allocation
            1. Creation
            2. Delete
            3. Display
            4. Exit
        """)
        try:
            option = int(input("Enter the Option : "))

        except ValueError:
            print("Enter a Valid Option")
            option = int(input("Enter the Option : "))

        if option == 1:
            create(variable)
        elif option == 2:
            delete(variable)
        elif option == 3:
            display()
        elif option == 4:
            exit()
        else:
            print("Wrong Option")


if __name__ == "__main__":
    main()
