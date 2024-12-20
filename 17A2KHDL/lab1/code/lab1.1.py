import xml.etree.ElementTree as ET 
class XMLReader: 
 def __init__(self, file_path):  #cơ bản bao gồm dường dẫn , để gọi hàm đọc xml
   self.file_path = file_path 
   self.data = None    # thuọc tính data ban đầu là rỗng , tí sẽ có data đc truyền vào 
 def read_xml(self):    # phương thức đọc file xml 
   tree = ET.parse(self.file_path)    # dung thư viện element Tree để lấy file xml thành 1 cây , cơ bản thì file xml đã đc cấu trúc dạng cây 
   self.data = tree.getroot()   #gán data bằng cây đó 
 def display_data(self):   # đoch dữ liệu , cơ bản là duyệt cây 
    if self.data:    # nếu thuộc tính data có thì thực thi tiếp 
       for product in self.data.findall('product'):   #duyệt tất cả các thẻ trong cây , cơ bản là các cành 
         name = product.find('name').text    # đây giường như là các lá cây vậy 
         price = product.find('price').text 
         quantity = product.find('quantity').text 
         print(f"Product: {name}, Price: {price}, Quantity:{quantity}")   #in ra 
# Sử dụng lớp XMLReader 
path="D:\\LAPTRINH PYTHON\\Python_nangcao_BuiManhDuong_DHKL17A2HN\\17A2KHDL\\lab1\\data\\products.xml"  # dùng đường dẫn trực tiếp cho chắc ăn 
reader = XMLReader(path)    #tạo 
reader.read_xml()  # gọi phương thức 
reader.display_data() 
