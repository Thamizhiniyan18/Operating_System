# pages_list = [3, 8, 2, 3, 9, 1, 6, 3, 8, 9, 3, 6, 2, 1, 3]
str_pages_list = input("Enter the required pages separated by a space : ").split(' ')
pages_list = []

for process in str_pages_list:
    pages_list.append(int(process))

# pages_list without duplicates
set_pages_list = set(pages_list)

# Initialising an empty list for storing the Frequency of pages
frequency = [0] * len(set_pages_list)


def decrement_frequency(page):
    for i, p in enumerate(set_pages_list):
        if p == page:
            frequency[i] -= 1


def increment_frequency(page):
    for i, p in enumerate(set_pages_list):
        if p == page:
            frequency[i] += 1


def main():
    frames = 5
    total_number_of_pages = len(pages_list)

    # Initialising a variable page_faults to 0 to have the count of the page faults
    page_faults = 0

    # Initialising an empty list for storing the pages in the memory
    memory = []

    # for i in set_pages_list:
    #     print(i)

    for page in pages_list:
        # Checking whether current page is present in the memory
        if page not in memory:

            # Checking whether the memory is full
            if frames == len(memory):
                decrement_frequency(page)
                memory.remove(memory[0])

            # Adding the current page to the end of the memory
            memory.append(page)

            # Incrementing the frequency of the current page
            increment_frequency(page)

            page_faults += 1

        else:
            # If page is already present in the memory remove the element and add it to the end of the memory and
            # increase its frequency
            increment_frequency(page)

            if page in memory:
                memory.remove(page)

            memory.append(page)

    print(f"Total Number of Page Hits : {total_number_of_pages - page_faults}")
    print(f"Total Number of Page Faults : {page_faults}")


# DRIVER CODE
if __name__ == "__main__":
    main()
