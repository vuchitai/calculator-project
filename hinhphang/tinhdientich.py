import os
def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")
        
import math
pi = math.pi

def tinh_dien_tich():
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