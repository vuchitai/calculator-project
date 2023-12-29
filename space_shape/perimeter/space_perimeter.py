import os
def clear_screen(): 
        os.system("cls" if os.name == "nt" else "clear")
        
import math
pi = math.pi

def calculate_the_perimeter_of_space():
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
