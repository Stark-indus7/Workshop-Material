# This project implements a real-time data processing pipeline using queues.
# Implement the code here

import time
from queue import Queue

def data_producer(queue):
    for i in range(10):
        time.sleep(1)
        data = f"Data {i}"
        queue.put(data)
        print(f"Produced: {data}")

def data_consumer(queue):
    while not queue.empty():
        data = queue.get()
        print(f"Consumed: {data}")
        queue.task_done()

if __name__ == "__main__":
    queue = Queue()
    data_producer(queue)
    data_consumer(queue)
