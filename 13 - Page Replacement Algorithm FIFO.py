# Importing the required modules
from queue import Queue


def main():
    # page_numbers = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]

    page_numbers = input("Enter the required pages separated by a space : ").split(' ')

    total_number_of_pages = len(page_numbers)
    frames = 3  # 5

    memory = set()  # Declaring a set() object

    # Creating a Queue object
    queue = Queue()

    # Count of total number of faults, initialised to zero
    count_faults = 0

    # Iterating through each page
    for i in range(total_number_of_pages):
        # Checking whether there is space in memory
        if len(memory) < frames:
            # Checking if the required page is already in the memory
            if page_numbers[i] not in memory:
                memory.add(page_numbers[i])   # Adding the required page to the memory
                count_faults += 1   # Incrementing the count of total number of faults by 1
                queue.put(page_numbers[i])  # Pushing the required page to the queue to track the sequence

        else:
            # Checking if the required page is already in the memory
            if page_numbers[i] not in memory:
                first_element = queue.queue[0]  # Storing the first page of the queue to a variable

                queue.get()  # Removing the first page from the queue

                # Removing the same page from the memory as well
                memory.remove(first_element)

                # Now pushing the required page
                memory.add(page_numbers[i])

                # Pushing the required page to the queue to track the sequence
                queue.put(page_numbers[i])

                count_faults += 1   # Incrementing the count of total number of faults by 1

    print(f"The Total Number of Hits : {total_number_of_pages - count_faults}")
    print(f"The Total Number of Page Faults : {count_faults}")


# DRIVER CODE
if __name__ == "__main__":
    main()
