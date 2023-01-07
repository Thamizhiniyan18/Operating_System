# Global Variables Declaration
number_of_processes = 5
number_of_resources = 3


# Main() Function Declaration
def main():
    # Empty boolean variable to check for the possibility of getting a safe sequence
    possibility = True

    # Empty list for storing the SAFE Sequence
    safe_sequence = []

    # Empty List for noting the completion of a process
    state = [0] * 5

    # An Empty Variable to mark the count of the number of finished process
    count = 0

    # The available amount of each resource
    # available = [0, 0, 0]
    available = [3, 3, 2]

    # The maximum demand of each customer
    maximum = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]

    # The amount currently allocated to each customer
    allocation = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]

    # Declaring an empty list need for calculating the required resources
    need = [[0 for i in range(number_of_resources)] for i in range(number_of_processes)]

    # Calculating the Needed Resources :
    for i in range(number_of_processes):
        for j in range(number_of_resources):
            need[i][j] = maximum[i][j] - allocation[i][j]

    # Finding the Safe Sequence
    while count < number_of_processes:
        if not possibility:
            print("Safe Sequence is not Possible")
            break
        for i in range(number_of_processes):
            if state[i] != 1:
                if len(safe_sequence) != number_of_processes:
                    # Checking whether the need of the current process is satisfied or not
                    if available[0] >= need[i][0] and available[1] >= need[i][1] and available[2] >= need[i][2]:
                        # Adding the already allocated resources to available resources after the process is completed
                        available[0] += allocation[i][0]
                        available[1] += allocation[i][1]
                        available[2] += allocation[i][2]

                        # Adding the current process to Safe Sequence
                        safe_sequence.append(f'P{i}')

                        # Changing the state of the current process
                        state[i] = 1

                        # Incrementing the count of number of finished process
                        count += 1

                        # Determining the possibility of existence of Safe Sequence
                        possibility = True
                    else:
                        # Determining the possibility of existence of Safe Sequence
                        possibility = False

    for i in range(len(safe_sequence)):
        print(safe_sequence[i], end="")
        if i != len(safe_sequence) - 1:
            print(" => ", end="")


# Driver Code
if __name__ == "__main__":
    main()
