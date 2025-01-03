# viết chương trình python tạo 2 luồng để tìm và in các số chẵn và lẻ từ 30 đến 50
import threading

def print_even_numbers():
    print("Các số chẵn từ 30 đến 50:")
    for num in range(30, 51):
        if num % 2 == 0:
            print(num, end=" ")
    print() 

def print_odd_numbers():
    print("Các số lẻ từ 30 đến 50:")
    for num in range(30, 51):
        if num % 2 != 0:
            print(num, end=" ")
    print()  

def main():
    even_thread = threading.Thread(target=print_even_numbers)
    odd_thread = threading.Thread(target=print_odd_numbers)

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

if __name__ == "__main__":
    main()
