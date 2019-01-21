import threading
import os


def number_generator(thread_number, event_for_wait, event_for_set):
    global counter
    while True:
        event_for_wait.wait()
        if counter < 101:
            event_for_wait.clear()
            print('Thread ' + str(thread_number) + ': ' + str(counter))
            counter += 1
            event_for_set.set()
        else:
            os._exit(0)


counter = 0

event1 = threading.Event()
event2 = threading.Event()

thread_a = threading.Thread(target=number_generator, args=(0, event1, event2))
thread_b = threading.Thread(target=number_generator, args=(1, event2, event1))

thread_a.start()
thread_b.start()

event1.set()
