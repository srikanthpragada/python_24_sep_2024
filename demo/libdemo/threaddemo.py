import threading
from threading import Thread


class ChildThread(Thread):
    def run(self):
        for i in range(1, 11):
            print(f'Child {i}')


def printNumbers():
    for i in range(1, 11):
        print(f'Print Thread {i}')


# print(threading.main_thread())
print(threading.current_thread())

ct = ChildThread()
ct.start()

ct2 = Thread(target = printNumbers)
ct2.start()


print(f'Count = {threading.active_count()}')

for i in range(1, 11):
    print(f"Main {i}")
