import os
def calculator():
    '''j cx dc'''
import math
def clear_screen(): 
        os.system("cls" if os.name == "nt" else "clear")
    

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
            from hinhkogian.thetich.tinhthetich import tinh_the_tich
            tinh_the_tich()
            

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
            from timso import find_gcd
            g5 = float(input("Mời bạn nhập số thứ nhất: "))
            h5 = float(input("Mời bạn nhập số thứ hai: "))
            i6 = float(input("Mời bạn nhập số thứ ba: "))
            gcd = find_gcd(g5, h5, i6)
            print("Ước chung lớn nhất của", g5, "và", h5, "và", i6, "là:", gcd)

        elif cull == 2:
            clear_screen()
            print("Bạn đã chọn tìm BCNN")
            i5 = float(input("Mời bạn nhập số thứ nhất: "))
            k5 = float(input("Mời bạn nhập số thứ hai: "))
            l6 = float(input("Mời bạn nhập số thứ ba: "))
            lcm = find_lcm(i5, k5, l6)
            print("Bội số chung nhỏ nhất của", i5, "và", k5, "và", l6, "là:", lcm)

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
            from tinhdathuc import tinh_tong_da_thuc
            tinh_tong_da_thuc()
            
        elif range == 2:
            clear_screen()
            print("Bạn đã chọn tính hiệu đa thức")
            from tinhdathuc import tinh_hieu_da_thuc
            tinh_hieu_da_thuc()
            
        elif range == 3:
            clear_screen()
            print("Bạn đã chọn tính tích đa thức")
            from tinhdathuc import tinh_tich_da_thuc
            tinh_tich_da_thuc()
            
        elif range == 4:
            clear_screen()
            print("Bạn đã chọn tính thương đa thức")
            from tinhdathuc import tinh_thuong_da_thuc
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