import os
def clear_screen(): 
        os.system("cls" if os.name == "nt" else "clear")
        
def tinh_Sxq():
    
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

