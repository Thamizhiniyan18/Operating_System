# Importing the multiprocessing module and time module
import multiprocessing
import time


# Creating a class named Chopsticks
class Chopsticks(object):
    # Declaring the Constructor
    def __init__(self):  # Initialising all the members of the class
        self.ID = None  # ID of the Chopstick
        self.philosopher_ID = None  # Philosophers ID
        self.count = None  # Total number available Chopsticks for eating
        self.right_or_left = None  # States the side of the chopstick either LEFT or RIGHT side
        self.status = 0  # Its states the status of the chopstick [0: Not-Engaged | 1: Engaged]

    def take(self, chopstick_id, philosopher_id, right_or_left, count):  # Defining the member Function take with the
        # following parameters: chopstick's id,philosopher's id,right/left chopstick,total no. of chopsticks available
        # Assigning the parameters to the respected members of the class
        self.ID = chopstick_id
        self.philosopher_ID = philosopher_id
        self.count = count
        self.right_or_left = right_or_left

        # Checking whether the chopstick is NOT-ENGAGED
        while self.status == 0:
            self.status = self.status + 1  # Changing the chopstick's state to ENGAGED
            self.count.value = self.count.value - 1  # Updating the chopstick's count
            print(f"Philosopher {self.philosopher_ID} has took the {self.right_or_left} chopstick with the "
                  f"ID: {self.ID} for Eating.")

    def drop(self, chopstick_id, philosopher_id, right_or_left, count):  # Defining the member Function drop with the
        # following parameters: chopstick's id,philosopher's id,right/left chopstick,total no. of chopsticks available
        # Assigning the parameters to the respected members of the class
        self.ID = chopstick_id
        self.philosopher_ID = philosopher_id
        self.count = count
        self.right_or_left = right_or_left

        # Checking whether the chopstick is ENGAGED
        while self.status == 1:
            self.status = self.status - 1  # Changing the chopstick's state to NOT-ENGAGED
            self.count.value = self.count.value + 1  # Updating the chopstick's count
            print(f"Philosopher {self.philosopher_ID} has dropped the {self.right_or_left} chopstick with the "
                  f"ID: {self.ID} after Eating.")


# Creating a class Philosophers as a Process object
class Philosophers(multiprocessing.Process):
    # Declaring the Constructor
    def __init__(
            self,
            philosopher_id,  # Philosophers ID
            chopsticks_count,  # Total number of chopsticks
            min_eating_time,  # Minimum eating time of the Philosopher
            total_eating_time,  # Total eating time of the Philosopher
            left_chopstick,  # Reference/ID to left chopstick of the Philosopher
            right_chopstick,  # Reference/ID to right chopstick of the Philosopher
            chopsticks_list  # Chopsticks list
    ):
        multiprocessing.Process.__init__(self)
        # Assigning the parameters to the respected members of the class
        self.ID = philosopher_id
        self.chopsticks_count = chopsticks_count
        self.eating_time = min_eating_time
        self.total_eating_time = total_eating_time
        self.left_chopstick = left_chopstick
        self.right_chopstick = right_chopstick
        self.chopsticks_list = chopsticks_list
        self.resource_required = 2  # The Resource required for the philosopher for eating
        self.state = ''

    # Automatically executing Function of the class
    def run(self):
        # Defining a loop that will execute until the total time required by the philosopher for eating becomes zero
        while self.total_eating_time > 0:
            # Checking whether there is enough resource for the philosopher to eat
            if self.chopsticks_count.value > self.resource_required:
                self.eating_state()  # Calling the eating_state() member function
                self.state = True
            else:
                if self.state:
                    self.thinking_state()  # Calling the thinking_state() member function
                    self.state = False

        print(f"\nPhilosopher {self.ID} has FINISHED Eating....")
        print(f"Time taken for philosopher {self.ID} to finish eating : {time.perf_counter() - start_time}\n")

    # Defining the member function eating_state
    def eating_state(self):
        # Creating the objects of the chopstick
        self.chopsticks_list[self.left_chopstick - 1] = Chopsticks()  # Creating an object for the left chopstick
        self.chopsticks_list[self.right_chopstick - 1] = Chopsticks()  # Creating an object for the right chopstick

        # Taking the Left Chopstick
        self.chopsticks_list[self.left_chopstick - 1].take(
            self.left_chopstick,
            self.ID,
            'LEFT',
            self.chopsticks_count
        )

        # Taking the Right Chopstick
        self.chopsticks_list[self.right_chopstick - 1].take(
            self.right_chopstick,
            self.ID,
            'RIGHT',
            self.chopsticks_count
        )
        time.sleep(self.eating_time)

        # Dropping the Right Chopstick
        self.chopsticks_list[self.right_chopstick - 1].drop(
            self.right_chopstick,
            self.ID,
            'RIGHT',
            self.chopsticks_count
        )

        # Dropping the Left Chopstick
        self.chopsticks_list[self.left_chopstick - 1].drop(
            self.left_chopstick,
            self.ID,
            'LEFT',
            self.chopsticks_count
        )

        # Updating the total eating time
        self.total_eating_time = self.total_eating_time - self.eating_time

    # Defining the member function thinking_state
    def thinking_state(self):
        print(f"Philosopher {self.ID} is THINKING !!!!")


# Defining the main() Function of the program
def main():
    # Creating a value in the shared memory
    chopsticks_count = multiprocessing.Value('i', 5)  # Count of the total number of chopsticks available
    # Creating the chopsticks list
    chopsticks = [1, 2, 3, 4, 5]

    philosophers_process_list = []  # Initialising an empty list for storing the process objects

    # Defining the philosophers properties
    philosophers = [
        [1, 1, 5],  # [Philosopher_ID, Minimum_Eating_time, Total_Eating_Time]
        [2, 3, 15],  # [Philosopher_ID, Minimum_Eating_time, Total_Eating_Time]
        [3, 2, 10],  # [Philosopher_ID, Minimum_Eating_time, Total_Eating_Time]
        [4, 5, 20],  # [Philosopher_ID, Minimum_Eating_time, Total_Eating_Time]
        [5, 4, 8]  # [Philosopher_ID, Minimum_Eating_time, Total_Eating_Time]
    ]

    # Looping through each philosopher and creating and appending the process objects of the class Philosophers to the
    # philosophers_process_list list
    for index, philosopher in enumerate(philosophers):
        philosophers_process_list.append(
            Philosophers(
                philosopher[0],  # Philosopher ID
                chopsticks_count,  # Total number of Chopsticks
                philosopher[1],  # Minimum Eating time of a Philosopher
                philosopher[2],  # Total time required for a philosopher to complete eating
                chopsticks[index % 5],  # ID of the left chopstick
                chopsticks[(index + 1) % 5],  # ID of the right chopstick
                chopsticks  # The chopsticks list
            )
        )

    # Looping through the philosophers_process_list and starting each philosopher process
    for i in range(5):
        philosophers_process_list[i].start()

    # Looping through the philosophers_process_list and joining each philosopher process
    for i in range(5):
        philosophers_process_list[i].join()


# Driver code for calling the main() function
if __name__ == "__main__":
    print("The Program started .....")

    start_time = time.perf_counter()
    main()  # Calling the main() function
    end_time = time.perf_counter()

    # Printing the total time taken for the execution of the program
    print("\nTotal time taken : ", end_time - start_time)
