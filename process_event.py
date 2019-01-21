import multiprocessing


def number_generator(process_number, value, event_for_wait, event_for_set):
    while value.value < 100:
        event_for_wait.wait()
        event_for_wait.clear()
        print('Process ' + str(process_number) + ': ' + str(value.value))
        value.value += 1
        event_for_set.set()


counter_value = multiprocessing.Value('i', 0)

event1 = multiprocessing.Event()
event2 = multiprocessing.Event()

process_a = multiprocessing.Process(target=number_generator,
                                    args=(0, counter_value, event1, event2))
process_b = multiprocessing.Process(target=number_generator,
                                    args=(1, counter_value, event2, event1))

process_a.start()
process_b.start()

event1.set()

process_a.join()
process_b.join()
