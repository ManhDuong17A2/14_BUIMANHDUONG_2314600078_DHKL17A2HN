import xml.dom.minidom

def main():
    # Phân tích tệp XML
    doc = xml.dom.minidom.parse('samble.xml')

    # In ra tên của phần tử gốc
    print( doc.documentElement.tagName)

    # Lấy danh sách tất cả các phần tử "staff"
    staff_elements = doc.getElementsByTagName("staff")

    # Duyệt qua từng phần tử "staff" và in ra thông tin chi tiết
    for staff in staff_elements:
        print("\nStaff ID:", staff.getAttribute("id"))
        name = staff.getElementsByTagName("name")[0].firstChild.data
        salary = staff.getElementsByTagName("salary")[0].firstChild.data
        print("Name:", name)
        print("Salary:", salary)

if __name__ == '__main__':
    main()
