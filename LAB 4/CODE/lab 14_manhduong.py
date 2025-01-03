import sqlite3

def create_database():
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS product (
            Id INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Price REAL NOT NULL,
            Amount INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def display_products():
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    if products:
        for product in products:
            print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Amount: {product[3]}")
    else:
        print("Danh sách sản phẩm trống.")
    conn.close()

def add_product():
    name = input("Nhập tên sản phẩm: ")
    price = float(input("Nhập giá sản phẩm: "))
    amount = int(input("Nhập số lượng sản phẩm: "))

    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?)", (name, price, amount))
    conn.commit()
    conn.close()
    print("Đã thêm sản phẩm mới.")

def search_product_by_name():
    name = input("Nhập tên sản phẩm cần tìm: ")

    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product WHERE Name LIKE ?", (f"%{name}%",))
    products = cursor.fetchall()
    if products:
        for product in products:
            print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Amount: {product[3]}")
    else:
        print("Không tìm thấy sản phẩm nào.")
    conn.close()

def update_product():
    product_id = int(input("Nhập ID sản phẩm cần cập nhật: "))
    new_price = float(input("Nhập giá mới: "))
    new_amount = int(input("Nhập số lượng mới: "))

    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE product SET Price = ?, Amount = ? WHERE Id = ?", (new_price, new_amount, product_id))
    conn.commit()
    conn.close()
    print("Đã cập nhật sản phẩm.")

def delete_product():
    product_id = int(input("Nhập ID sản phẩm cần xóa: "))

    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM product WHERE Id = ?", (product_id,))
    conn.commit()
    conn.close()
    print("Đã xóa sản phẩm.")

def main_menu():
    while True:
        print("\nQuản lý sản phẩm:")
        print("1. Hiển thị danh sách sản phẩm")
        print("2. Thêm sản phẩm mới")
        print("3. Tìm kiếm sản phẩm theo tên")
        print("4. Cập nhật thông tin sản phẩm")
        print("5. Xóa sản phẩm")
        print("6. Thoát")

        choice = input("Chọn chức năng (1-6): ")

        if choice == '1':
            display_products()
        elif choice == '2':
            add_product()
        elif choice == '3':
            search_product_by_name()
        elif choice == '4':
            update_product()
        elif choice == '5':
            delete_product()
        elif choice == '6':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    create_database()
    main_menu()
