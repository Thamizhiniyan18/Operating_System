# Importing the required libraries
import threading
import time

resource = 1
completed_count = 0


class Philosopher(threading.Thread):
    # Declaring the Constructor
    def __init__(self, philosopher_id):
        threading.Thread.__init__(self)
        self.ID = philosopher_id
        self.completed = False
        self.state = True

    def run(self):
        while completed_count < 3:
            if not self.completed:
                if resource > 0:
                    self.eating()
                    self.state = True
                    self.completed = True
                else:
                    if self.state:
                        self.thinking()
                        self.state = False
        print(f"\nPhilosopher {self.ID} has FINISHED Eating....")

        return 0


    def eating(self):
        global resource, completed_count
        print(f"Philosopher {self.ID} is Eating")
        resource -= 1
        time.sleep(2)
        resource += 1
        completed_count += 1



    def thinking(self):
        global resource
        print(f"philosopher {self.ID} is Thinking")


def main():
    philosophers = []

    for i in range(3):
        philosophers.append(
            Philosopher(
                i
            )
        )

    for i in range(3):
        philosophers[i].start()

    for i in range(3):
        philosophers[i].join()


# DRIVER CODE
if __name__ == "__main__":
    main()
