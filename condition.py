import os
import threading


def number_generator(thread_number):
    global counter
    while True:
        condition.acquire()
        if counter < 101:
            print('Thread ' + str(thread_number) + ': ' + str(counter))
            counter += 1
        else:
            os._exit(0)
        condition.notify_all()
        condition.wait()


counter = 0

condition = threading.Condition()

thread_a = threading.Thread(target=number_generator, args=[0])
thread_b = threading.Thread(target=number_generator, args=[1])

thread_a.start()
thread_b.start()
