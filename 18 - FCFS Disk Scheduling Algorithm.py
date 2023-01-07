def main():
    # requests = [82, 170, 43, 140, 24, 16, 190]
    # head_pointer = 50
    str_requests = input("Enter the requests separated by a space : ").split(' ')
    requests = []
    for request in str_requests:
        requests.append(int(request))

    head_pointer = int(input("Enter the Head Pointer : "))

    # Defining a variable seek count with a value 0
    seek_count = 0

    for i in range(len(requests)):
        current_request = requests[i]

        # Calculating the distance
        distance = abs(current_request - head_pointer)

        # incrementing the seek_count
        seek_count += distance

        # current request is now new head_pointer
        head_pointer = current_request

    print(f"Total Number of seek Operations = {seek_count}")


if __name__ == "__main__":
    main()
