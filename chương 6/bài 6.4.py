# viết chương trình python để tính giai thừa của một số bằng nhiều luồng
import threading

def calculate_factorial(num, result, index):
    """Hàm tính giai thừa của một số."""
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    result[index] = factorial  
    print(f"Giai thừa của {num} là: {factorial}")

def main():
    numbers = [2,3,5]  
    threads = []
    results = [0] * len(numbers)  


    for i, num in enumerate(numbers):
        thread = threading.Thread(target=calculate_factorial, args=(num, results, i))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("\nKết quả cuối cùng:")
    for i, num in enumerate(numbers):
        print(f"Giai thừa của {num}: {results[i]}")

if __name__ == "__main__":
    main()
