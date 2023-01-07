def main():
    print("Round robin Scheduling")

    # Getting the Burst time of all processes
    burst_time_str = input("Enter the Burst time of all the processes separated by a space : ").split(' ')

    burst_time = []  # Empty list to store the integer burst time values

    for i in range(len(burst_time_str)):
        burst_time.append(int(burst_time_str[i]))

    quantum = int(input("Enter the quantum : "))

    waiting_time = [0] * len(burst_time)  # Initializing a list of size of burst_time with zero
    turn_around_time = [0] * len(burst_time)

    # Calculating the Waiting Time
    balance_burst_time = [0] * len(burst_time)  # Initializing a list of size of burst_time with zero

    # Copying the burst_time to remaining_burst_time
    for i in range(len(burst_time)):
        balance_burst_time[i] = burst_time[i]

    current_time = 0

    # Initialising a while loop to execute round-robin scheduling cycle
    while True:
        finished = True
        for i in range(len(burst_time)):
            if balance_burst_time[i] > 0:
                finished = False  # The process is not yet completed
                if balance_burst_time[i] > quantum:
                    current_time += quantum  # Incrementing the current time
                    # Subtract the quantum from balance_burst_time
                    balance_burst_time[i] -= quantum
                else:
                    current_time += balance_burst_time[i]

                    waiting_time[i] = current_time - burst_time[i]

                    balance_burst_time[i] = 0  # As the process is finished

        # Checking whether all processes are done
        if finished:
            break

    # Calculating the Turn Around Time
    for i in range(len(burst_time)):
        turn_around_time[i] = burst_time[i] + waiting_time[i]

    print(f"Average Turn Around Time : {sum(turn_around_time) / len(turn_around_time) } seconds")
    print(f"Average Waiting Time : {sum(waiting_time) / len(waiting_time)} seconds")


if __name__ == "__main__":
    main()
