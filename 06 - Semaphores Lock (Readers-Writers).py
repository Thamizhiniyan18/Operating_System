# Importing the multiprocessing library
import multiprocessing


def withdrawal(balance_amount, semaphore):
    for _ in range(10000):
        semaphore.acquire()
        balance_amount.value = balance_amount.value - 1
        semaphore.release()


def deposit(balance_amount, semaphore):
    for _ in range(10000):
        semaphore.acquire()
        balance_amount.value = balance_amount.value + 1
        semaphore.release()


for _ in range(5):
    # Initialising balance in shared memory
    balance = multiprocessing.Value('i', 1000)

    lock = multiprocessing.Lock()

    # Process Creation
    p1 = multiprocessing.Process(target=withdrawal, args=(balance, lock))
    p2 = multiprocessing.Process(target=deposit, args=(balance, lock))

    # Starting the Processes
    p1.start()
    p2.start()

    # Waiting for the processes to complete
    p1.join()
    p2.join()

    print("Balance after all the withdrawals and deposits is : {}".format(balance.value))
