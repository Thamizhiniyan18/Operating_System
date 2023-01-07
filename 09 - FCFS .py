# Importing the required modules
import threading
import time

# Globally declaring the values
start = time.perf_counter()  # stores the starting time of the program
turn_around_time_list = []  # Empty list that stores the list of turn_around_time
waiting_time_list = []  # Empty list that stores the list of waiting_time_list


def process(process_id, arrival_time, burst_time, semaphore, process_start):
    time.sleep(arrival_time)

    semaphore.acquire()

    print("\nProcess Number :", process_id)
    print("Arrival Time :", arrival_time)
    print("Burst Time :", burst_time)

    time.sleep(burst_time)

    completion_time = int(time.perf_counter() - process_start)
    print("Completion Time :", completion_time, " seconds")

    turn_around_time = completion_time - arrival_time
    print("Turn Around Time :", turn_around_time, " seconds")

    waiting_time = turn_around_time - burst_time
    print("Waiting Time :", waiting_time, " seconds")

    turn_around_time_list.append(turn_around_time)
    waiting_time_list.append(waiting_time)
    semaphore.release()


def main():
    process_list = []  # Stores the threads

    process_table = []  # Empty list for storing the process details

    # Gets the count of total number of process
    number_of_processes = int(input("Enter the total number of processes : "))

    print("Enter the arrival time and burst time separated by a space [ Eg : arrival_time burst_time ]")

    # Getting the processes and its arrival_time, burst_time
    for i in range(number_of_processes):
        process_table.append(input().split(' '))

    lock = threading.Lock()  # Creating a Semaphore

    process_start = time.perf_counter()  # Stores the process starting time

    # Creating the threads
    for i in range(len(process_table)):
        process_list.append(
            threading.Thread(target=process,
                             args=(
                                 i + 1,  # process_id
                                 int(process_table[i][0]),  # arrival_time
                                 int(process_table[i][1]),  # burst_time
                                 lock,  # Semaphore
                                 process_start  # Process queue starting time
                             )
                             )
        )

    # Starting the processes
    for i in range(len(process_list)):
        process_list[i].start()

    # Waiting for the processes to complete
    for i in range(len(process_list)):
        process_list[i].join()

    print("\nAverage Turn Around Time :", round(sum(turn_around_time_list) / len(turn_around_time_list)))
    print("Average Waiting Time :", round(sum(waiting_time_list) / len(waiting_time_list)))


# Driver Code
if __name__ == "__main__":
    print("First Come First Serve Algorithm\n")
    main()
    end = time.perf_counter()
    print(f"\nTotal time taken for the program to finish : {round(end - start)} seconds")
