# viết chương trình python sử dụng luồng để tải xuống đồng thời nhiều tệptệp
import threading
import time

def download_file(file_name):
    print(f"Bắt đầu tải: {file_name}")
    time.sleep(2)  
    print(f"Hoàn tất tải: {file_name}")

def main():
    files = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]
    threads = []

    for file in files:
        thread = threading.Thread(target=download_file, args=(file,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
