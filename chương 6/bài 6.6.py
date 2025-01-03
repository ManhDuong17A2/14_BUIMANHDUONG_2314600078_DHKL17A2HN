# viết chương trình sử dụng hai luồng sao cho một luồng viết các số chẵn theo thứ tự tăng dần và các số lẻ khác theo thứ tự tăng dần đối với một ngưỡng nhất định
import threading

# In số chẵn theo thứ tự tăng dần
def print_even(max_num):
    for i in range(2, max_num + 1, 2):
        print(f"Even: {i}")

# In số lẻ theo thứ tự tăng dần
def print_odd(max_num):
    for i in range(1, max_num + 1, 2):
        print(f"Odd: {i}")

def main():
    max_num = 20
    even_thread = threading.Thread(target=print_even, args=(max_num,))
    odd_thread = threading.Thread(target=print_odd, args=(max_num,))

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

if __name__ == "__main__":
    main()
