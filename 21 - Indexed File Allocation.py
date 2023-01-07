# Initialising an Objects list
objects = []


# Defining a class Sequence
class File(object):
    # Defining a constructor
    def __init__(self, name, size):
        self.name = name  # Class Members
        self.size = size  # Class Members
        self.allocated = []

        for i in range(10):
            self.allocated.append(self.size / 10)


# Function for Creating a File
def create(variable):
    switch = True  # Temporary Variable
    switch_1 = True  # Temporary Variable
    name = None  # Initialising an empty variable

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

    try:
        size = int(input("Enter the size : "))
    except ValueError:
        print("Enter a Valid Size")
        size = int(input("Enter the size : "))

    objects.append(File(
        name,
        size
    ))
    variable += 1


# Function for Deleting a File
def delete(variable):
    variable -= 1
    objects.remove(objects[variable])


# Function for Displaying all the files
def display():
    print("".center(100, '-'))
    print(
        "|",
        "File Name".center(20),
        "|",
        "Size".center(20),
        "|",
        "Pointer".center(20),
        "|",
        "Allocated Memory Address".center(27),
        "|",
        end="\n"
    )
    print("".center(100, '-'))
    for obj in objects:
        print("".center(100, '-'))
        print(
            "|",
            f"{obj.name} ".center(20),
            "|",
            f"{obj.size} MB".center(20),
            "|",
            f"{id(obj.allocated)}".center(20),
            "|",
            f"{id(obj.allocated[0])}".center(27),
            "|"
        )
        for i in range(1, len(obj.allocated)):
            print(
                "|",
                "".center(20),
                "|",
                "".center(20),
                "|",
                "".center(20),
                "|",
                end=''
            )
            print(f" {id(obj.allocated[i])}".center(28), "|")
        print("".center(100, '-'))


# Main Function
def main():
    variable = 0
    while True:
        print("""\nIndexed File Allocation
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
