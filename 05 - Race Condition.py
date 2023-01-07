# Importing the multiprocessing library
import multiprocessing


def withdrawal(balance_amount):
    for _ in range(10000):
        balance_amount.value = balance_amount.value - 1


def deposit(balance_amount):
    for _ in range(10000):
        balance_amount.value = balance_amount.value + 1


for _ in range(5):
    # Initialising balance in shared memory
    balance = multiprocessing.Value('i', 1000)

    # Process Creation
    p1 = multiprocessing.Process(target=withdrawal, args=(balance,))
    p2 = multiprocessing.Process(target=deposit, args=(balance, ))

    # Starting the Processes
    p1.start()
    p2.start()

    # Waiting for the processes to complete
    p1.join()
    p2.join()

    print("Balance after all the withdrawals and deposits is : {}".format(balance.value))
