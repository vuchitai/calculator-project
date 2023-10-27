while True: 
    try:
        print("Bạn muốn tính toán cái gì?")
        print("1. phép tính thường")
        print("2. chu vi / diện tích của các loại hình phẳng")
        print("3. chu vi / diện tích / thể tích của các loại hình không gian")
        print("4. tìm ƯCLN / BCNN")
        print("5. thoát")
        choice = int(input("Nhập số để lựa chọn: "))
        
        if choice == 1:
            print("1")
            
    except ValueError:
        print("ko hợp lệ")
        
