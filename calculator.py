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
            number1 = float(input("Nhập số đầu tiên để thực hiện phép tính: "))
            operation = input("Nhập dấu để tính ( cộng, trừ, nhân, hoặc chia ): ")
            number2 = float(input("Nhập số thứ hai để thực hiện phép tính: "))

            if operation == "cộng":
                result = number1 + number2
            elif operation == "trừ":
                result = number1 - number2
            elif operation == "nhân":
                result = number1 * number2
            elif operation == "chia":
                result = number1 / number2
            print("kết quả là:", result)

        elif vote == 2:
            clear_screen()
            print("Bạn đã chọn tính phân số")
            print("Cách ghi: 2 phần 3 = 2/3")
            number3 = Fraction(input("Nhập số đầu tiên để thực hiện phép tính: "))
            operations = input("Nhập dấu để tính ( cộng, trừ, nhân, hoặc chia ): ")
            number4 = Fraction(input("Nhập số thứ hai để thực hiện phép tính: "))

            if operations == "cộng":
                result1 = number3 + number4
            elif operations == "trừ":
                result1 = number3 - number4
            elif operations == "nhân":
                result1 = number3 * number4
            elif operations == "chia":
                result1 = number3 / number4
            print("kết quả là:", result1)

    elif choice == 2:
        clear_screen()
        print("Bạn đã chọn tính chu vi / diện tích của các loại hình phẳng.")
        print("Bạn muốn tính kiểu tính gì?")
        print("1. chu vi")
        print("2. diện tích")
        choose = int(input("Nhập số để lựa chọn: "))

        if choose == 1:
            clear_screen()
            print("Bạn đã chọn tính chu vi")
            print("Bạn muốn tính chu vi hình nào?")
            print("1. hình vuông")
            print("2. hình chữ nhật")
            print("3. hình tam giác")
            print("4. hình thang")
            print("5. hình bình hành")
            print("6. hình thoi")
            print("7. hình tròn")
            select =  int(input("Nhập số để lựa chọn: "))
            
            if select == 1:
                clear_screen()
                print("Bạn đã chọn tính chu vi hình vuông")
                a = float(input("Mời bạn nhập độ dài của 1 cạnh hình vuông: "))
                tong = a * 4
                print("kết quả là:", tong, "cm")

            elif select == 2:
                clear_screen()
                print("Bạn đã chọn tính chu vi hình chữ nhật")
                b = float(input("Mời bạn nhập chiều dài cạnh hình chữ nhật: "))
                c = float(input("Mời bạn nhập chiều rộng cạnh hình chữ nhật: "))
                tong1 = (b + c) * 2
                print("Kết quả là:", tong1 ,"cm")

            elif select == 3:
                clear_screen()
                print("Bạn đã chọn tính chu vi hình tam giác")
                e = float(input("Mời bạn nhập chiều dài cạnh thứ 1 của hình: "))
                f = float(input("Mời bạn nhập chiều dài cạnh thứ 2 của hình: "))
                g = float(input("Mời bạn nhập chiều dài cạnh thứ 3 của hình: "))
                tong2 = e + f + g
                print("Kết quả là:", tong2 ,"cm")
                
            elif select == 4:
                clear_screen()
                print("Bạn đã chọn tính chu vi hình thang")
                h = float(input("Mời bạn nhập chiều dài đáy bé của hình: "))
                i = float(input("Mời bạn nhập chiều dài đáy lớn của hình: "))
                k = float(input("Mời bạn nhập chiều dài cạnh bên thứ 1 của hình: "))
                l = float(input("Mời bạn nhập chiều dài cạnh bên thứ 2 của hình: "))
                tong3 = h + i + k + l
                print("Kết quả là:", tong3 ,"cm")

            elif select == 5:
                clear_screen()
                print("Bạn đã chọn tính chu vi hình bình hành")
                m = float(input("Mời bạn nhập chiều dài cạnh thứ 1 của hình: "))
                n = float(input("Mời bạn nhập chiều dài cạnh thứ 2 của hình: "))
                tong4 = 2 * (m + n)
                print("Kết quả là:", tong4, "cm")

            elif select == 6:
                clear_screen()
                print("Bạn đã chọn tính chu vi hình thoi")
                o = float(input("Mời bạn nhập độ dài của 1 cạnh hình thoi: "))
                tong5 = o * 4
                print("kết quả là:", tong5, "cm")

            elif select == 7:
                clear_screen()
                print("Bạn đã chọn tính chu vi hình tròn")
                p = float(input("Mời bạn nhập bán kính hình tròn: "))
                tong6 = 2 * pi * p
                print("Kết quả là:", tong6,"cm")

        elif choose == 2:
            clear_screen()
            print("Bạn đã chọn tính diện tích")
            print("Bạn muốn tính diện tích hình nào?")
            print("1. hình vuông")
            print("2. hình chữ nhật")
            print("3. hình tam giác")
            print("4. hình thang")
            print("5. hình bình hành")
            print("6. hình thoi")
            print("7. hình tròn")
            sort = float(input("Nhập số để lựa chọn: "))

            if sort == 1:
                clear_screen()
                print("Bạn đã chọn tính diện tích hình vuông")
                q = float(input("Mời bạn nhập chiều dài của 1 cạnh hình vuông: "))
                tong7 = q * q
                print("Kết quả là:", tong7,"cm2")

            elif sort == 2:
                clear_screen()
                print("Bạn đã chọn tính diện tích hình chữ nhật")
                r = float(input("Mời bạn nhập chiều dài của hình: "))
                s = float(input("Mời bạn nhập chiều rộng của hình: "))
                tong8 = r * s
                print("Kết quả là:", tong8,"cm2" )

            elif sort == 3:
                clear_screen()
                print("Bạn đã chọn tính diện tích hình tam giác")
                t = float(input("Mời bạn nhập chiều cao của hình: "))
                u = float(input("Mời bạn nhập chiều dài cạnh đáy của hình: "))
                tong9 = 1/2 * t * u
                print("Kết quả là:", tong9, "cm2")

            elif sort == 4:
                clear_screen()
                print("Bạn đã chọn tính diện tích hình thang")
                v = float(input("Mời bạn nhập chiều dài đáy bé của hình: "))
                x = float(input("Mời bạn nhập chiều dài đáy lớn của hình: "))
                y = float(input("Mời bạn nhập chiều cao của hình: "))
                tong10 = (v + x) * y / 2
                print("Kết quả là:", tong10, "cm2")

            elif sort == 5:
                clear_screen()
                print("Bạn đã chọn tính diện tích hình bình hành")
                a1 = float(input("Mời bạn nhập chiều dài của hình: "))
                b1 = float(input("Mời bạn nhập chiều cao của hình: "))
                tong11 = a1 * b1
                print("Kết quả là:", tong11, "cm2")

            elif sort == 6:
                clear_screen()
                print("Bạn đã chọn tính diện tích hình thoi")
                c1 = float(input("Mời bạn nhập chiều dài đường chéo thứ 1 của hình: "))
                d1 = float(input("Mời bạn nhập chiều dài đường chéo thứ 2 của hình: "))
                tong12 = 1/2 * c1 * d1
                print("Kết quả là:", tong12, "cm2")

            elif sort == 7:
                clear_screen()
                print("Bạn đã chọn tính diện tích hình tròn")
                e1 = float(input("Mời bạn nhập bán kính của hình: "))
                tong13 = pi * e1 * e1
                print("Kết quả là:", tong13, "cm2")  

    elif choice == 3:
        clear_screen()
        print("Bạn đã chọn tính chu vi / diện tích / thể tích của các hình không gian")
        print("Bạn muốn tính kiểu gì?")
        print("1. chu vi")
        print("2. diện tích")
        print("3. thể tích")
        option = float(input("Nhập só để lựa chọn: "))

        if option == 1:
            clear_screen()
            print("Bạn đã chọn tính chu vi")
            print("Bạn muốn tính chu vi hình nào? ")
            print("1. hình lập phương")
            print("2. hình hộp chữ nhật")
            print("3. hình chóp tam giác đều")
            print("4. hình chóp tứ giác đều")
            print("5. hình cầu")
            print("6. hình nón")
            print("7. hình trụ")
            print("8. hình lăng trụ")
            pick = float(input("Nhập số để lựa chọn: "))

            if pick == 1:
                clear_screen()
                print("Bạn đã chọn tính chu vi hình lập phương")
                f1 = float(input("Mời bạn nhập chiều dài 1 cạnh của hình: "))
                tong14 = f1 * 12
                print("Kết quả là:", tong14, "cm")

            elif pick == 2:
                clear_screen()
                print("Bạn đã chọn tính chu vi hình hộp chữ nhật")
                g1 = float(input("Mời bạn nhập chiều dài của hình: "))
                h1 = float(input("Mời bạn nhập chiều rộng của hình: "))
                i1 = float(input("Mời bạn nhập chiều cao của hình: "))
                tong15 = 4 * (g1 + h1 + i1)
                print("Kết quả là:", tong15, "cm")

            elif pick == 3:
                clear_screen()
                print("Bạn đã chọn tính chu vi hình chóp tam giác đều")
                k1 = float(input("Mời bạn nhập chiều dài 1 cạnh của hình: "))
                tong16 = k1 * 6
                print("Kết quả là:", tong16, "cm")

            elif pick == 4:
                clear_screen()
                print("Bạn đã chọn tính chu vi hình chóp tứ giác đều")   
                l1 = float(input("Mời bạn nhập chiều dài 1 cạnh của hình: "))
                tong17 = l1 * 8
                print("Kết quả là:", tong17, "cm")

            elif pick == 5:
                clear_screen()
                print("Bạn đã chọn tính chu vi hình cầu")
                m1 = float(input("Mời bạn nhập bán kính hình cầu: "))
                tong18 = 2 * pi * m1
                print("Kết quả là:", tong18, "cm")

            elif pick == 6:
                clear_screen()
                print("Bạn đã chọn tính chu vi xung quanh hình nón")
                n1 = float(input("Mời bạn nhập bán kính của hình: "))
                o1 = float(input("Mời bạn nhập chiều dài đường sinh của hình: "))
                tong19 = pi * (n1 + o1)
                print("Kết quả là:", tong19, "cm")
                
            elif pick == 7:
                clear_screen()
                print("Bạn đã chọn tính chu vi hình trụ")
                p1 = float(input("Mời bạn nhập bán kính đường tròn đáy của hình: "))
                q1 = float(input("Mời bạn nhập chiều cao của hình: "))
                tong20 = 2 * (pi * p1 + q1)
                print("Kết quả là:", tong20, "cm")

            elif pick == 8:
                clear_screen()
                print("Bạn đã chọn tính chu vi hình lăng trụ")
                print("Bạn muốn tính chu vi hình lăng trụ nào?")
                print("1. lăng trụ đứng tam giác")
                print("2. lăng trụ đứng tứ giác")
                print("3. lăng trụ tam giác")
                print("4. lăng trụ tứ giác")
                judgment = float(input("Nhập số để lựa chọn: "))

                if judgment == 1:
                    clear_screen()
                    print("Bạn đã chọn tính chu vi hình lăng trụ tam giác")
                    r1 = float(input("Mời bạn nhập cạnh đáy của hình: "))
                    s1 = float(input("Mời bạn nhập cạnh bên thứ 1 của hình: "))
                    t1 = float(input("Mời bạn nhập cạnh bên thứ 2 của hình: "))
                    u1 = float(input("Mời bạn nhập cạnh bên thứ 3 của hình: "))
                    tong21 = 6 * r1 + (s1 + t1 + u1)
                    print("Kết quả là:", tong21, "cm")

                elif judgment == 2:
                    clear_screen()
                    print("Bạn đã chọn tính chu vi lăng trụ tứ giác")
                    v1 = float(input("Mời bạn nhập cạch đáy của hình: ")) 
                    x1 = float(input("Mời bạn nhập cạnh bên thứ 1 của hình: "))
                    y1 = float(input("Mời bạn nhập cạnh bên thứ 2 của hình: "))
                    a2 = float(input("Mời bạn nhập cạnh bên thứ 3 của hình: "))
                    b2 = float(input("Mời bạn nhập cạnh bên thứ 4 của hình: "))
                    tong22 = 8 * v1 + (x1 + y1 + a2 + b2)
                    print("Kết quả là:", tong22, "cm")

                elif judgment == 3:
                    clear_screen()
                    print("Bạn đã chọn tính chu vi hình lăng trụ đứng tam giác")
                    c2 = float(input("Mời bạn nhập cạnh đáy thứ 1 của hình: "))
                    d2 = float(input("Mời bạn nhập cạnh đáy thứ 2 của hình: "))
                    e2 = float(input("Mời bạn nhập cạnh đáy thứ 3 của hình: "))
                    f2 = float(input("Mời bạn nhập cạnh bên của hình: "))
                    tong23 = (c2 + d2 + e2) * 2 + (f2 * 3)
                    print("Kết quả là:", tong23, "cm")

                elif judgment == 4:
                    clear_screen()
                    print("Bạn đã chọn tính chu vi hình lăng trụ tứ giác đứng")
                    g2 = float(input("Mời bạn nhập cạnh đáy thứ 1 của hình: "))
                    h2 = float(input("Mời bạn nhập cạnh đáy thứ 2 của hình: "))
                    i2 = float(input("Mời bạn nhập cạnh đáy thứ 3 của hình: "))
                    k2 = float(input("Mời bạn nhập cạnh đáy thứ 4 của hình: "))
                    l2 = float(input("Mời bạn nhập cạnh bên của hình: "))
                    tong24 = (g2 + h2 + i2 + k2) * 2 + (l2 * 4)
                    print("Kết quả là:", tong24, "cm")


        elif option == 2:
            clear_screen()
            print("Bạn đã chọn tính diện tích")
            print("Bạn muốn tính kiểu tính diện tích nào?")
            print("1. Sxq: diện tích xung quanh")
            print("2. Stp: diện tích toàn phần ")
            decision = float(input("Nhập số để lựa chọn: "))

            if decision == 1:
                clear_screen()
                print("Bạn đã chọn tính Sxq")
                print("Bạn muốn tính Sxq hình nào? ")
                print("1. hình lập phương")
                print("2. hình hộp chữ nhật")
                print("3. hình chóp tam giác đều")
                print("4. hình chóp tứ giác đều")
                print("5. hình nón")
                print("6. hình trụ")
                print("7. lăng trụ")
                resolution = float(input("Nhập số để lựa chọn: "))

                if resolution == 1:
                    clear_screen()
                    print("Bạn đã chọn tính Sxq hình lập phương")
                    m2 = float(input("Mời bạn nhập chiều dài của hình: "))
                    tong25 = m2* m2 * 4
                    print("Kết quả là:", tong25, "cm2")

                elif resolution == 2:
                    clear_screen()
                    print("Bạn đã chọn tính Sxq hình hộp chứ nhật")
                    n2 = float(input("Mời bạn nhập chiều dài của hình: "))
                    o2 = float(input("Mời bạn nhập chiều rộng của hình: "))
                    p2 = float(input("Mời bạn nhập chiều cao của hình: "))
                    tong26 = 2 * (n2 + o2 + p2)
                    print("Kết quả là:", tong26, "cm2")
                    
                elif resolution == 3:
                    clear_screen()
                    print("Bạn đã chọn tính Sxq hình chóp tam giác đều ")
                    q2 = float(input("Mời bạn nhập chiều dài cạnh đáy của hình: "))
                    r2 = float(input("Mời bạn nhập chiều cao mặt bên của hình: "))
                    tong27 = 3 * 1/2 * q2 * r2
                    print("Kết quả là:", tong27, "cm2")

                elif resolution == 4:
                    clear_screen()
                    print("Bạn đã chọn Sxq của hình chóp tứ giác đều")
                    s2 = float(input("Mời bạn nhập chiều dài cạnh đáy của hình: "))
                    t2 = float(input("Mời bạn nhập chiều cao mặt bên của hình: "))
                    tong28 = 4 * 1/2 * s2 * t2
                    print("Kết quả là:", tong28, "cm2")

                elif resolution == 5:
                    clear_screen()
                    print("Bạn đã chọn tính Sxq hình nón")
                    u2 = float(input("Mời bạn nhập đường sinh của hình: "))
                    v2 = float(input("Mời bạn nhập bán kính đáy của hình: "))
                    tong29 = pi * u2 * v2
                    print("Kết quả là:", tong29, "cm2")

                elif resolution == 6:
                    clear_screen()
                    print("Bạn đã chọn tính Sxq hình cầu")
                    x2 = float(input("Mời bạn nhập bán kính của hình: "))
                    tong30 = 4 * pi * x2 * x2
                    print("Kết quả là:", tong30, "cm2")

                elif resolution == 7:
                    clear_screen()
                    print("Bạn đã chọn tính Sxq hình lăng trụ")
                    print("Bạn muốn tính Sxq của hình lăng trụ nào? ")
                    print("1. lăng trụ đứng tam giác")
                    print("2. lăng trụ đứng tứ giác")
                    print("3. lăng trụ tam giác")
                    print("4. lăng trụ tứ giác")
                    determination = float(input("Nhập số để lựa chọn: "))

                    if determination == 1:
                        print("Bạn đã chọn tính Sxq của hình lăng trụ đứng tam giác")
                        y2 = float(input("Mời bạn nhập chu vi đáy của hình: "))      
                        z2 = float(input("Mời bạn nhập chiều cao của hình: "))      
                        tong31 = y2 * z2
                        print("Kết quả là:", tong31, "cm2")

                    elif determination == 2:
                        print("Bạn đã chọn tính Sxq của hình lăng trụ đứng tứ giác")
                        a3 = float(input("Mời bạn nhập chu vi đáy của hình: "))      
                        b3 = float(input("Mời bạn nhập chiều cao của hình: "))      
                        tong32 = a3 * b3
                        print("Kết quả là:", tong32, "cm2")  

                    elif determination == 3:
                        print("Bạn đã chọn tính Sxq của hình lăng trụ tam giác")
                        c3 = float(input("Mời bạn nhập chu vi đáy của hình: "))      
                        d3 = float(input("Mời bạn nhập chiều cao của hình: "))      
                        tong33 = c3 * d3
                        print("Kết quả là:", tong33, "cm2")                             

                    elif determination == 4:
                        print("Bạn đã chọn tính Sxq của hình lăng trụ tứ giác")
                        e3 = float(input("Mời bạn nhập chu vi đáy của hình: "))      
                        f3 = float(input("Mời bạn nhập chiều cao của hình: "))      
                        tong34 = e3 * f3
                        print("Kết quả là:", tong34, "cm2")

            elif decision == 2:
                clear_screen()
                print("Bạn đã chọn tính Stp")
                print("Bạn muốn tính Stp hình nào?")
                print("1. hình lập phương")
                print("2. hình hộp chữ nhật")
                print("3. hình chóp tam giác đều")
                print("4. hình chóp tứ giác đều")
                print("5. hình nón")
                print("6. hình trụ")
                print("7. hình cầu")
                print("8. hình lăng trụ")
                preference = float(input("Nhập số để lựa chọn: "))

                if preference == 1:
                    clear_screen()
                    print("Bạn đã chọn tính Stp hình lập phương")
                    g3 = float(input("Mời bạn nhập chiều dài 1 cạnh của hình: "))
                    tong35 = 6 * g3 * g3
                    print("Kết quả là:", tong35, "cm2")

                elif preference == 2:
                    clear_screen()
                    print("Bạn đã chọn tính Stp hình hộp chữ nhật")
                    h3 = float(input("Mời bạn nhập Sxq của hình: "))
                    i3 = float(input("Mời bạn nhập diện tích đáy của hình: "))
                    tong36 = h3 + i3 * 2
                    print("Kết quả là:", tong36, "cm2")

                elif preference == 3:
                    clear_screen()
                    print("Bạn đã chọn tính Stp hình chóp tam giác đều")
                    k3 = float(input("Mời bạn nhập Sxq của hình: "))
                    l3 = float(input("Mời bạn nhập chiều dài cạnh đáy của hình: "))
                    tong37 = k3 + l3 * 3
                    print("Kết quả là:", tong37, "cm2")

                elif preference == 4:
                    clear_screen()
                    print("Bạn đã chọn tính Stp hình chóp tứ giác đều")
                    m3 = float(input("Mời bạn nhập Sxq của hình: "))
                    n3 = float(input("Mời bạn nhập chiều dài cạnh đáy của hình: "))
                    tong38 = m3 + n3 * 4
                    print("Kết quả là:", tong38, "cm2")

                elif preference == 5:
                    clear_screen()
                    print("Bạn đã chọn tính Stp hình nón")
                    o3 = float(input("Mời bạn nhập Sxq của hình: "))
                    p3 = float(input("Mời bạn nhập diện tích đáy của hình: "))
                    tong38 = o3 + p3 
                    print("Kết quả là:", tong38, "cm2")

                elif preference == 6:
                    clear_screen()
                    print("Bạn đã chọn tính Stp hình trụ")
                    q3 = float(input("Mời bạn nhập chiều cao của hình: "))
                    r3 = float(input("Mời bạn nhập bán kính của hình: "))
                    tong39 = 2 * pi * r3 * (r3 + q3)
                    print("Kết quả là:", tong39, "cm2")

                elif preference == 7:
                    clear_screen()
                    print("Bạn đã chọn tính Stp hình cầu")
                    s3 = float(input("Mời bạn nhập bán kính của hình: "))
                    tong40 = 4 * pi * s3 ** 2
                    print("Kết quả là:", tong40, "cm2")

                elif preference == 8:
                    clear_screen()
                    print("Bạn đã chọn tính Stp hình lăng trụ")
                    print("Bạn muốn tính Stp hình lăng trụ nào?")
                    print("1. lăng trụ đứng tam giác")
                    print("2. lăng trụ đứng tứ giác")
                    print("3. lăng trụ tam giác")
                    print("4. lăng trụ tứ giác")
                    alternative = float(input("Nhập số để lựa chọn: "))

                    if alternative == 1:
                        clear_screen()
                        print("Bạn đã chọn tính Stp hình lăng trụ đứng tam giác")
                        t3 = float(input("Mời bạn nhập chiều dài cạnh đáy thứ 1 của hình: "))
                        u3 = float(input("Mời bạn nhập chiều dài cạnh đáy thứ 2 của hình: "))
                        v3 = float(input("Mời bạn nhập chiều dài cạnh đáy thứ 3 của hình: "))
                        x3 = float(input("Mời bạn nhập Sxq của hình: "))
                        tong41 = x3 + (u3 + t3 + v3) * 2
                        print("Kết quả là:", tong41, "cm2")

                    elif alternative == 2:
                        clear_screen()
                        print("Bạn đã chọn tính Stp hình lăng trụ đứng tứ giác")
                        y3 = float(input("Mời bạn nhập chiều dài cạnh đáy thứ 1 của hình: "))
                        a4 = float(input("Mời bạn nhập chiều dài cạnh đáy thứ 2 của hình: "))
                        b4 = float(input("Mời bạn nhập chiều dài cạnh đáy thứ 3 của hình: "))
                        c4 = float(input("Mời bạn nhập chiều dài cạnh đáy thứ 4 của hình: "))
                        d4 = float(input("Mời bạn nhập Sxq của hình: "))
                        tong42 = d4 + (y3 + a4 + b4 + c4) * 2
                        print("Kết quả là:", tong42, "cm2")

                    elif alternative == 3:
                        clear_screen()
                        print("Bạn đã chọn tính Stp hình lăng trụ tam giác")
                        e4 = float(input("Mời bạn nhập diện tích 1 mặt đáy của hình: "))
                        f4 = float(input("Mời bạn nhập diện tích 1 mặt bên của hình: "))
                        tong43 = e4 * 2 + f4 * 3
                        print("Kết quả là:", tong43, "cm2")

                    elif alternative == 4:
                        clear_screen()
                        print("Bạn đã chọn tính Stp hình lăng trụ tứ giác")
                        g4 = float(input("Mời bạn nhập diện tích 1 mặt đáy của hình: "))
                        h4 = float(input("Mời bạn nhập diện tích 1 mặt bên của hình: "))
                        tong44 = g4 * 2 + h4 * 4
                        print("Kết quả là:", tong44, "cm2")                    
                        
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
            tinh_thuong_da_thuc
        
        
        
    elif choice == 8:
        clear_screen()
        print("cảm ơn bạn đã sử dụng.")
        break

    cont = input("Tiếp tục tính toán? (có/không): ").lower()
    if cont.lower() != 'có':
        clear_screen() 
        print("cảm ơn bạn đã sử dụng.")
        break 
    