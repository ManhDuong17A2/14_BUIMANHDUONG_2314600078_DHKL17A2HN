import threading
import time

class SimpleTask:
    def __init__(self, lock):
        self.lock = lock

    def run_task(self, counter):
        for _ in range(4):
            time.sleep(2)
            with self.lock:  
                counter[0] += 1
                print(f"Counter đã tăng lên: {counter[0]}")

def main():
    counter = [0]  
    lock = threading.Lock() 
    tasks = [threading.Thread(target=SimpleTask(lock).run_task, args=(counter,)) for _ in range(4)]
    for task in tasks:
        task.start()
    for task in tasks:
        task.join()

if __name__ == "__main__":
    main()
