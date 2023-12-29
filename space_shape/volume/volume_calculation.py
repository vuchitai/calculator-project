import os
def clear_screen(): 
        os.system("cls" if os.name == "nt" else "clear")
        
import math
pi = math.pi

def volume_calculation():
        
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