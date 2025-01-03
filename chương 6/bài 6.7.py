import threading
import time
from datetime import datetime

def task(name):
    print(f"Starting {name}")
    for _ in range(5):
        print(f"{name}: Web {datetime.now().strftime('%b %d %H:%M:%S %Y')}")
        time.sleep(1)  
    print(f"Exiting {name}")

def main():
    print("Starting Main Thread")

    threads = [
        threading.Thread(target=task, args=("Google",)),
        threading.Thread(target=task, args=("Yahoo",)),
        threading.Thread(target=task, args=("Facebook",))
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Exiting Main Thread")

if __name__ == "__main__":
    main()
