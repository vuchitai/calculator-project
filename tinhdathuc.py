import sympy as sp

# Hàm chuyển đổi biểu thức từ chuỗi thành định dạng sympy
def chuyen_doi_bieu_thuc(bieu_thuc):
    bieu_thuc = bieu_thuc.replace("^", "**")  # Chuyển ^ thành **
    return sp.sympify(bieu_thuc)

def tinh_tong_da_thuc():
    # Nhập hai biểu thức từ người dùng
    input_a = input("Nhập biểu thức a(x): ")
    input_b = input("Nhập biểu thức b(x): ")

    # Chuyển đổi biểu thức thành định dạng sympy và tính tổng
    a = chuyen_doi_bieu_thuc(input_a)
    b = chuyen_doi_bieu_thuc(input_b)

    tong = sp.simplify(a + b)

    # In ra đa thức tổng dưới dạng x^n thay vì x**n
    tong_str = str(tong).replace("**", "^")
    print("Đa thức tổng (a + b) là:", tong_str)
    
def tinh_hieu_da_thuc():
    # Nhập hai biểu thức từ người dùng
    input_a = input("Nhập biểu thức a(x): ")
    input_b = input("Nhập biểu thức b(x): ")

    # Chuyển đổi biểu thức thành định dạng sympy và tính tổng
    a = chuyen_doi_bieu_thuc(input_a)
    b = chuyen_doi_bieu_thuc(input_b)

    hieu = sp.simplify(a - b)

    # In ra đa thức tổng dưới dạng x^n thay vì x**n
    hieu_str = str(hieu).replace("**", "^")
    print("Đa thức tổng (a - b) là:", hieu_str)
    
def tinh_tich_da_thuc():
    # Nhập hai biểu thức từ người dùng
    input_a = input("Nhập biểu thức a(x): ")
    input_b = input("Nhập biểu thức b(x): ")

    # Chuyển đổi biểu thức thành định dạng sympy và tính tổng
    a = chuyen_doi_bieu_thuc(input_a)
    b = chuyen_doi_bieu_thuc(input_b)

    tich = sp.simplify(a * b)

    # In ra đa thức tổng dưới dạng x^n thay vì x**n
    tich_str = str(tich).replace("**", "^")
    print("Đa thức tổng (a * b) là:", tich_str)
    
def tinh_thuong_da_thuc():
    # Nhập hai biểu thức từ người dùng
    input_a = input("Nhập biểu thức a(x): ")
    input_b = input("Nhập biểu thức b(x): ")

    # Chuyển đổi biểu thức thành định dạng sympy và tính tổng
    a = chuyen_doi_bieu_thuc(input_a)
    b = chuyen_doi_bieu_thuc(input_b)

    thuong = sp.simplify(a / b)

    # In ra đa thức tổng dưới dạng x^n thay vì x**n
    thuong_str = str(thuong).replace("**", "^")
    print("Đa thức tổng (a / b) là:",_thuong_str)