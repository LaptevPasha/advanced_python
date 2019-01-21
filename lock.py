import threading
import os


def number_generator(thread_number):
    global counter
    while True:
        lock.acquire()
        if counter < 101:
            if ((counter % 2) == (thread_number % 2)):
                print('Thread ' + str(thread_number) + ': ' + str(counter))
                counter += 1
        else:
            os._exit(0)
        lock.release()


counter = 0

lock = threading.Lock()

thread_a = threading.Thread(target=number_generator, args=[0])
thread_b = threading.Thread(target=number_generator, args=[1])

thread_a.start()
thread_b.start()
