import time
import threading

def eat_cpu():
    while True:
        pass  # Do nothing forever

threads = []

for _ in range(4):  # 4 CPU monsters
    t = threading.Thread(target=eat_cpu)
    t.start()
    threads.append(t)

time.sleep(60)  # Let them run for 1 minute
