import os
def clear_screen(): 
        os.system("cls" if os.name == "nt" else "clear")
        
def tinh_Stp():

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