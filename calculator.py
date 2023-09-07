import os
def calculator():
    '''j cx dc'''
import math
def clear_screen(): 
        os.system("cls" if os.name == "nt" else "clear")

def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    gcd = find_gcd(a, b)
    lcm = (a * b) // gcd
    return lcm

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
    

from fractions import Fraction

pi = math.pi


while True:
    clear_screen()
    print("Bạn muốn tính toán cái gì?")
    print("1. phép tính thường")
    print("2. chu vi / diện tích của các loại hình phẳng")
    print("3. chu vi / diện tích / thể tích của các loại hình không gian")
    print("4. tìm ƯCLN / BCNN")
    print("5. tính lũy thừa")
    print("6. tính căn bậc")
    print("7. tính đa thức 1 biến")
    print("8. thoát")
    choice = int(input("Nhập số để lựa chọn: "))
    
    if choice == 1:
        clear_screen()
        print("Bạn đã chọn phép tính thường")
        print("Bạn muốn tính phép tính dạng nào?")
        print("1. Số thường")
        print("2. Phân số")
        vote = int(input("Nhập số để lựa chọn: "))
        
        if vote == 1:
            clear_screen()
            print("Bạn đã chọn tính số thường")
            from pheptinhthuong.tinhsothuong import tinh_so_thuong
            result1 = tinh_so_thuong()
            print(f"Kết quả là: {result1}")

        elif vote == 2:
            clear_screen()
            print("Bạn đã chọn tính phân số")
            print("Cách ghi: 2 phần 3 = 2/3")
            from pheptinhthuong.tinhphanso import tinh_phan_so
            result3 = tinh_phan_so()
            print(f"KQ là:, {result3}")


    elif choice == 2:
        clear_screen()
        print("Bạn đã chọn tính chu vi / diện tích của các loại hình phẳng.")
        print("Bạn muốn tính kiểu tính gì?")
        print("1. chu vi")
        print("2. diện tích")
        choose = int(input("Nhập số để lựa chọn: "))

        if choose == 1:
            clear_screen()
            from hinhphang.tinhchuvi import tinh_chu_vi
            tinh_chu_vi()
            
        elif choose == 2:
            clear_screen()
            from hinhphang.tinhdientich import tinh_dien_tich
            tinh_dien_tich()
            
    elif choice == 3:
        clear_screen()
        print("Bạn đã chọn tính chu vi / diện tích / thể tích của các hình không gian")
        print("Bạn muốn tính kiểu gì?")
        print("1. chu vi")
        print("2. diện tích")
        print("3. thể tích")
        option = float(input("Nhập số để lựa chọn: "))

        if option == 1:
            clear_screen()
            from hinhkogian.chuvi.tinhchuvikogian import tinh_chu_vi
            tinh_chu_vi()

        elif option == 2:
            clear_screen()
            print("Bạn đã chọn tính diện tích")
            print("Bạn muốn tính kiểu tính diện tích nào?")
            print("1. Sxq: diện tích xung quanh")
            print("2. Stp: diện tích toàn phần ")
            decision = float(input("Nhập số để lựa chọn: "))

            if decision == 1:
                clear_screen()
                from hinhkogian.dientich.Sxq.Sxq import tinh_Sxq
                tinh_Sxq()

            elif decision == 2:
                clear_screen()
                from hinhkogian.dientich.Stp.Stp import tinh_Stp
                tinh_Stp()
                
                        
        elif option == 3:
            clear_screen()
            print("bạn đã chọn tính thể tích")
            print("Bạn muốn tích thể tích hình nào?")
            print("1. hình lập phương")
            print("2. hình hộp chữ nhật")
            print("3. hình chóp tam giác đều")
            print("4. hình chóp tứ giác đều")
            print("5. hình nón")
            print("6. hình trụ")
            print("7. hình cầu")
            print("8. hình lăng trụ")
            elect = float(input("Nhập số để lựa chọn: ")) 

            if elect == 1:
                clear_screen()
                print("Bạn đã chọn tính thể tích hình lập phương")
                i4 = float(input("Mời bạn nhập chiều dài 1 cạnh của hình: "))
                tong45 = i4 ** 3
                print("Kết quả là:", tong45, "cm3")

            elif elect == 2:
                clear_screen()
                print("Bạn đã chọn tính thể tích hình hộp chữ nhật")
                k4 = float(input("Mời bạn nhập chiều dài của hình: "))
                l4 = float(input("Mời bạn nhập chiều rộng của hình: "))
                m4 = float(input("Mời bạn nhập chiều cao của hình: "))
                tong46 = k4 * l4 * m4
                print("Kết quả là:", tong46, "cm3")

            elif elect == 3:
                clear_screen()
                print("Bạn đã chọn tính thể tích hình chóp tam giác đều")
                n4 = float(input("Mời bạn nhập diện tích đáy của hình: "))
                o4 = float(input("Mời bạn nhập chiều cao của hình: "))
                tong47 = 1/3 * n4 * o4
                print("Kết quả là:", tong47, "cm3")
                        
            elif elect == 4:
                clear_screen()
                print("Bạn đã chọn tính thể tích hình chóp tứ giác đều")
                p4 = float(input("Mời bạn nhập diện tích đáy của hình: "))
                q4 = float(input("Mời bạn nhập chiều cao của hình: "))
                tong48 = 1/3 * p4 * q4
                print("Kết quả là:", tong48, "cm3")

            elif elect == 5:
                clear_screen()
                print("Bạn đã chọn tính thể tích hình nón")
                r4 = float(input("Mời bạn nhập bán kính đáy của hình: "))
                s4 = float(input("Mời bạn nhập chiều cao của hình: "))
                tong49 = 1/3 * pi * r4 ** 2 * s4
                print("Kết quả là:", tong49, "cm3")

            elif elect == 6:
                clear_screen()
                print("Bạn đã chọn tính thể tích hình trụ")
                t4 = float(input("Mời bạn nhập bán kính của hình: "))
                u4 = float(input("Mời bạn nhập chiều cao của hình: "))
                tong50 = pi * t4 ** 2 * u4
                print("Kết quả là:", tong50, "cm3")

            elif elect == 7:
                clear_screen()
                print("Bạn đã chọn tính thể tích hình cầu")
                v4 = float(input("Mời bạn nhập bán kính của hình: "))
                tong51 = 4 * pi * v4 ** 2
                print("Kết quả là:", tong51, "cm3")     

            elif elect == 8:
                clear_screen()
                print("Bạn đã chọn tính thể tích hình lăng trụ")
                print("Bạn muốn tính thể tích hình lăng trụ nào?")
                print("1. lăng trụ đứng tam giác")
                print("2. lăng trụ đứng tứ giác")
                print("3. lăng trụ tam giác")
                print("4. lăng trụ tứ giác")
                decide = float(input("Nhập số để lựa chọn: "))

                if decide == 1:
                    clear_screen()
                    print("Bạn đã chọn tính thể tích hình lăng trụ đứng tam giác")
                    x4 = float(input("Mời bạn nhập diện tích đáy của hình: "))
                    y4 = float(input("Mời bạn nhập chiều cao của hình: "))
                    tong52 = x4 * y4
                    print("Kết quả là:", tong52, "cm3")

                elif decide == 2:
                    clear_screen()
                    print("Bạn đã chọn tính thể tích hình lăng trụ đứng tứ giác")
                    a5 = float(input("Mời bạn nhập diện tích đáy của hình: "))
                    b5 = float(input("Mời bạn nhập chiều cao của hình: "))
                    tong53 = a5 * b5
                    print("Kết quả là:", tong53, "cm3")

                elif decide == 3:
                    clear_screen()
                    print("Bạn đã chọn tính thể tích hình lăng trụ tam giác")
                    c5 = float(input("Mời bạn nhập diện tích đáy của hình: "))
                    d5 = float(input("Mời bạn nhập chiều cao của hình: "))
                    tong54 = c5 * d5
                    print("Kết quả là:", tong54, "cm3")
                    
                elif decide == 4:
                    clear_screen()
                    print("Bạn đã chọn tính thể tích hình lăng trụ tứ giác")
                    e5 = float(input("Mời bạn nhập diện tích đáy của hình: "))
                    f5 = float(input("Mời bạn nhập chiều cao của hình: "))
                    tong55 = e5 * f5
                    print("Kết quả là:", tong55, "cm3")

    elif choice == 4:
        clear_screen()
        print("Bạn đã chọn tìm ƯCLN / BCNN")
        print("Bạn muốn tìm cái nào?")
        print("1.ƯCLN")
        print("2.BCNN")
        cull = int(input("Nhập số để lựa chọn: "))
        
        if cull == 1:
            clear_screen()
            print("Bạn đã chọn tìm ƯCLN")
            g5 = float(input("Mời bạn nhập số thứ nhất: "))
            h5 = float(input("Mời bạn nhập số thứ hai: "))
            gcd = find_gcd(g5, h5)
            print("Ước chung lớn nhất của", g5, "và", h5, "là:", gcd)

        elif cull == 2:
            clear_screen()
            print("Bạn đã chọn tìm BCNN")
            i5 = float(input("Mời bạn nhập số thứ nhất: "))
            k5 = float(input("Mời bạn nhập số thứ hai: "))
            lcm = find_lcm(i5, k5)
            print("Bội số chung nhỏ nhất của", i5, "và", k5, "là:", lcm)

    elif choice == 5:
        clear_screen()
        print("Bạn đã chọn tính lũy thừa")
        l5 = float(input("Mời bạn nhập cơ số: "))
        m5 = float(input("Mời bạn nhập số mũ: "))
        tong56 = l5 ** m5
        print("Kết quả là:", tong56)
        
    elif choice == 6:
        clear_screen()
        print("Bạn đã chọn tính căn bậc")
        n5 = float(input("Mời bạn nhập radicand của phép tính: "))
        o5 = int(input("Mời bạn nhập căn bậc của phép tính: "))
        tong57 = f'{n5**(1/o5)}'
        print(f'căn bậc {o5} của {n5} là:', tong57)

    elif choice == 7:
        clear_screen()
        print("Bạn đã chọn tính đa thức 1 biến")
        print("Bạn muốn tính kiểu gì?")
        print("1. tổng")
        print("2. hiệu")
        print("3. tích")
        print("4. thương")
        range = int(input("Nhập số để lựa chọn: "))
        
        if range == 1:
            clear_screen()
            print("Bạn đã chọn tính tổng đa thức")
            tinh_tong_da_thuc()
            
        elif range == 2:
            clear_screen()
            print("Bạn đã chọn tính hiệu đa thức")
            tinh_hieu_da_thuc()
            
        elif range == 3:
            clear_screen()
            print("Bạn đã chọn tính tích đa thức")
            tinh_tich_da_thuc()
            
        elif range == 4:
            clear_screen()
            print("Bạn đã chọn tính thương đa thức")
            tinh_thuong_da_thuc()
        
        
    elif choice == 8:
        clear_screen()
        print("cảm ơn bạn đã sử dụng.")
        break

    cont = input("Tiếp tục tính toán? (có/không): ").lower()
    if cont.lower() != 'có':
        clear_screen() 
        print("cảm ơn bạn đã sử dụng.")
        break 
    