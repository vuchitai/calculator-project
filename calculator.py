import os
def calculator():
    '''j cx dc'''
import math
def clear_screen(): 
        os.system("cls" if os.name == "nt" else "clear")
    
pi = math.pi


while True:
    clear_screen()
    print("Bạn muốn tính toán cái gì?")
    print("1. phép tính thường")
    print("2. chu vi / diện tích của các loại hình phẳng")
    print("3. chu vi / diện tích / thể tích của các loại hình không gian")
    print("4. tìm ƯCLN / BCNN")
    print("5. thoát")
    choice = int(input("Nhập số để lựa chọn: "))
    
    if choice == 1:
        clear_screen()
        print("Bạn đã chọn tính phép tính thường")
        print("Lưu ý: căn bậc 3 của 27 là '27^(1/3)'")
        phep_tinh = input("nhập phép tính: ")
        phep_tinh = phep_tinh.replace("^", "**")
        print(eval(phep_tinh))


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
        option = int(input("Nhập số để lựa chọn: "))

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
            decision = int(input("Nhập số để lựa chọn: "))

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
        print("Bạn đã chọn tìm ƯCLN BCNN")
        from timso import tim_uoc_chung_va_boi_chung_cua_nhieu_so
        tim_uoc_chung_va_boi_chung_cua_nhieu_so()

    
    elif choice == 5:
        clear_screen()
        print("cảm ơn bạn đã sử dụng.")
        break

    cont = input("Tiếp tục tính toán? (có/không): ").lower()
    if not cont.islower() or cont != 'có':
        clear_screen() 
        print("cảm ơn bạn đã sử dụng.")
        break
