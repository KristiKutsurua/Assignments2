import threading
import queue
import random
import time

def process_queue(queue):
    while not queue.empty():
        try:
            num = queue.get(block=False)
            thread_name = threading.current_thread().name
            if num % 2 == 0:
                print(f"Thread {thread_name}: Element {num} is even.")
            else:
                print(f"Thread {thread_name}: Element {num} is odd.")
            time.sleep(1)
        except queue.Empty:
            break

def fill_queue(queue, size):
    for _ in range(size):
        num = random.randint(1, 100)
        queue.put(num)
        print(f"Inserted {num} into the queue.")
        time.sleep(0.5)

def main():
    num_elements = 10
    my_queue = queue.Queue()

    fill_thread = threading.Thread(target=fill_queue, args=(my_queue, num_elements))
    fill_thread.start()
    fill_thread.join()

    threads = []
    for i in range(3):
        thread = threading.Thread(target=process_queue, args=(my_queue,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All tasks completed.")

if __name__ == "__main__":
    main()
