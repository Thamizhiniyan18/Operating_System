def main():
    # process_list = [3, 2, 1, 3, 4, 1, 6, 2, 4, 3, 4, 2, 1, 4, 5, 2, 1, 3, 4]
    str_process_list = input("Enter the required pages separated by a space : ").split(' ')
    process_list = []

    for process in str_process_list:
        process_list.append(int(process))

    frames = 3

    # Pages in the current memory
    memory = []

    page_faults = 0

    for process in process_list:
        # Checking if current process is present in the memory
        if process not in memory:
            # Checking whether the memory is full
            if frames == len(memory):
                memory.remove(memory[0])
                memory.append(process)

            else:
                memory.append(process)

            # Incrementing the page_faults
            page_faults += 1

        # If the current process already exists in the memory
        else:
            # Removing the previous index of the memory
            memory.remove(process)

            # Appending the current process
            memory.append(process)

    print(f"Total Number of Hits : {len(process_list) - page_faults}")
    print(f"Total Number of Page Faults : {page_faults}")


# DRIVER CODE
if __name__ == "__main__":
    main()
