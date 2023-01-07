# Calculates the difference of each track number with the number with the head position
def calculate_difference(queue, head_pointer, difference):
    for i in range(len(difference)):
        difference[i][0] = abs(queue[i] - head_pointer)


# Finding accessed track which is at minimum distance from head
def find_minimum_distance(difference):
    index = -1
    minimum = 999999999

    for i in range(len(difference)):
        if not difference[i][1] and minimum > difference[i][0]:
            minimum = difference[i][0]
            index = i

    return index


def main():
    # requests = [82, 170, 43, 140, 24, 16, 190]
    # head_pointer = 50
    str_requests = input("Enter the requests separated by a space : ").split(' ')
    requests = []
    for request in str_requests:
        requests.append(int(request))

    head_pointer = int(input("Enter the Head Pointer : "))

    difference = [0] * len(requests)

    # Initializing array
    for i in range(len(requests)):
        difference[i] = [0, 0]

    # Defining a variable seek count with a value 0
    seek_count = 0

    # Initializing list for storing seek sequence
    seek_sequence = [0] * (len(requests) + 1)

    for i in range(len(requests)):
        seek_sequence[i] = head_pointer
        calculate_difference(requests, head_pointer, difference)
        index = find_minimum_distance(difference)

        difference[index][1] = True

        # incrementing the seek_count
        seek_count += difference[index][0]

        # current request is now new head_pointer
        head_pointer = requests[index]

    # For last access track
    seek_sequence[len(seek_sequence) - 1] = head_pointer

    print(f"Total Number of seek Operations = {seek_count}")


if __name__ == "__main__":
    main()
