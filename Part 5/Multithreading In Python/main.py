import threading

# The target function for the thread to call
def targetFunction(num1, num2):
    print(num1 + num2)

# Creating the threads
thread1 = threading.Thread(target=targetFunction, args=(4,5))
thread2 = threading.Thread(target=targetFunction, args=(9,40))

# Telling the threads to fire their targets
thread1.start()
thread2.start()

# Joining the threads because they have completed their work.
thread1.join()
thread2.join()

# Functionality on the main thread
print('test')

# https://www.geeksforgeeks.org/multithreading-python-set-1/