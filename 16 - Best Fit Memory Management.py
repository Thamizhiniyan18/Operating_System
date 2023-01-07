def main():
    # Available Memory block sizes list
    # memory_block_size = [100, 500, 200, 300, 600]
    str_memory_block_size = input("Enter the Memory block sizes separated by a space : ").split(' ')
    memory_block_size = []
    for block in str_memory_block_size:
        memory_block_size.append(int(block))

    # Process size list
    # process_size = [212, 417, 112, 426]
    str_process_size = input("Enter the Process sizes separated by a space : ").split(' ')
    process_size = []
    for process in str_process_size:
        process_size.append(int(process))

    # Initializing an empty list to store the id of the memory block that is allocated to a process
    allocated_memory_block = [-1] * len(process_size)

    # Looping through each process
    for i in range(len(process_size)):
        best_fit = -1
        for j in range(len(memory_block_size)):
            if memory_block_size[j] > process_size[i]:
                if best_fit == -1:
                    best_fit = j
                elif memory_block_size[best_fit] > memory_block_size[j]:
                    best_fit = j

        if best_fit != -1:
            # Allocating the block j to the current process
            allocated_memory_block[i] = best_fit

            # Reduce available memory in this block
            memory_block_size[best_fit] -= process_size[i]

    print(
        "Process No.".center(20),
        "Process Size".center(20),
        "Block No.".center(20),
        "Wastage".center(20)
    )
    for i in range(len(process_size)):
        print(
            f"{i + 1}".center(20),
            f"{process_size[i]}".center(20),
            f"{allocated_memory_block[i] + 1}".center(20),
            f"{memory_block_size[allocated_memory_block[i]]}".center(20)
        )


if __name__ == "__main__":
    main()
