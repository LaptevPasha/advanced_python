import threading
import os
import time


def number_generator(thread_number):
    global counter
    while True:
        if counter < 101:
            if ((counter % 2) == (thread_number % 2)):
                print('Thread ' + str(thread_number) + ': ' + str(counter))
                counter += 1
        else:
            os._exit(0)
        time.sleep(0.1)


counter = 0

timer1 = threading.Timer(0.1, number_generator, args=[0])
timer2 = threading.Timer(0.2, number_generator, args=[1])
timer1.start()
timer2.start()
