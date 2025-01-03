# viết chương trình python để tạo nhiều luồng và in tên của các luồng đóđó
import threading

def print_thread_name():
    print(f"Đây là luồng: {threading.current_thread().name}")

def main():
    threads = []
    for i in range(5):  
        thread = threading.Thread(target=print_thread_name, name=f"Luồng-{i+1}")
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
