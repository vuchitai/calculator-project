import os
def clear_screen(): 
        os.system("cls" if os.name == "nt" else "clear")
def tinh_chu_vi():
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

