import threading

# Hàm tính tổng các phần tử trong một phần của danh sách
def compute_sum(part, result, index):
    result[index] = sum(part)
    print(f"Partial sum for {part}: {result[index]}")

# Chương trình chính
def main():
    numbers = [3, 5, 7, 2, 8, 6, 4, 7, 1, 9]
    mid = len(numbers) // 2

    # Chia danh sách thành 2 phần
    part1 = numbers[:mid]
    part2 = numbers[mid:]

    # Mảng lưu kết quả từ các luồng
    result = [0, 0]

    # Tạo và khởi chạy các luồng
    threads = [
        threading.Thread(target=compute_sum, args=(part1, result, 0)),
        threading.Thread(target=compute_sum, args=(part2, result, 1))
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # Tính tổng cuối cùng
    total_sum = sum(result)
    print(f"Total sum: {total_sum}")

if __name__ == "__main__":
    main()
