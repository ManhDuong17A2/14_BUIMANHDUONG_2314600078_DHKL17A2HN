import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Tạo cơ sở dữ liệu
def create_database():
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS product (
            Id INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Price REAL NOT NULL,
            Amount INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Hiển thị danh sách sản phẩm
def display_products():
    tree.delete(*tree.get_children())
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)
    conn.close()

# Thêm sản phẩm
def add_product():
    name, price, amount = entry_name.get(), entry_price.get(), entry_amount.get()
    if not name or not price or not amount:
        return messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
    conn = sqlite3.connect("product.db")
    conn.execute("INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?)", (name, float(price), int(amount)))
    conn.commit()
    conn.close()
    display_products()
    clear_entries()

# Xóa sản phẩm
def delete_product():
    selected = tree.focus()
    if not selected:
        return messagebox.showerror("Lỗi", "Vui lòng chọn sản phẩm để xóa!")
    product_id = tree.item(selected)["values"][0]
    conn = sqlite3.connect("product.db")
    conn.execute("DELETE FROM product WHERE Id = ?", (product_id,))
    conn.commit()
    conn.close()
    display_products()

# Cập nhật sản phẩm
def update_product():
    selected = tree.focus()
    if not selected:
        return messagebox.showerror("Lỗi", "Vui lòng chọn sản phẩm để cập nhật!")
    product_id = tree.item(selected)["values"][0]
    name, price, amount = entry_name.get(), entry_price.get(), entry_amount.get()
    if not name or not price or not amount:
        return messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
    conn = sqlite3.connect("product.db")
    conn.execute("UPDATE product SET Name = ?, Price = ?, Amount = ? WHERE Id = ?", 
                 (name, float(price), int(amount), product_id))
    conn.commit()
    conn.close()
    display_products()
    clear_entries()

# Điền thông tin sản phẩm vào ô nhập liệu khi chọn
def fill_entries(event):
    selected = tree.focus()
    if not selected:
        return
    values = tree.item(selected)["values"]
    entry_name.delete(0, tk.END)
    entry_name.insert(0, values[1])
    entry_price.delete(0, tk.END)
    entry_price.insert(0, values[2])
    entry_amount.delete(0, tk.END)
    entry_amount.insert(0, values[3])

# Xóa dữ liệu trong các ô nhập liệu
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_amount.delete(0, tk.END)

# Giao diện
create_database()
root = tk.Tk()
root.title("Quản Lý Sản Phẩm")

# Nhập liệu
tk.Label(root, text="Tên:").grid(row=0, column=0)
tk.Label(root, text="Giá:").grid(row=1, column=0)
tk.Label(root, text="Số lượng:").grid(row=2, column=0)
entry_name, entry_price, entry_amount = tk.Entry(root), tk.Entry(root), tk.Entry(root)
entry_name.grid(row=0, column=1)
entry_price.grid(row=1, column=1)
entry_amount.grid(row=2, column=1)
tk.Button(root, text="Thêm", command=add_product).grid(row=3, column=0)
tk.Button(root, text="Cập nhật", command=update_product).grid(row=3, column=1)

# Bảng dữ liệu
columns = ("ID", "Tên", "Giá", "Số lượng")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=4, column=0, columnspan=2)
tree.bind("<<TreeviewSelect>>", fill_entries)

# Nút xóa
tk.Button(root, text="Xóa", command=delete_product).grid(row=5, column=0, columnspan=2)

# Hiển thị dữ liệu ban đầu
display_products()

root.mainloop()
