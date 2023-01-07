def single_level(users, directories):
    print("\nSingle Level File Organization Scheme : ", end='\n\n')
    print("Root Directory : ")
    for i in range(len(users)):
        for j in range(len(directories[i])):
            print(f"\t--> {directories[i][j]} [ User : {users[i]} ]")


def two_level(users, directories):
    print("\nTwo Level File Organization Scheme : ", end='\n\n')
    print("Root Directory : ")
    for i in range(len(users)):
        print(f"\t--> {users[i]}")
        for j in range(len(directories[i])):
            print(f"\t\t--> {directories[i][j]}")


def main():
    # users = ['Thamizh', 'Sai', 'Saravanan', 'Tarun']
    users = input("Enter the User Names separated by a space : ").split(' ')
    # directories = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L']]
    directories = []
    for i in range(len(users)):
        directories.append(input(f"Enter the file names of the user : {users[i]} separated by a space : ").split(' '))
    single_level(users, directories)
    two_level(users, directories)


if __name__ == "__main__":
    main()
