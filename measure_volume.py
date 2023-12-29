import os
def cls(): 
    os.system("cls" if os.name == "nt" else "clear")
    
def measure_volume():
    print("1. tấn")
    print("2. tạ")
    print("3. yến")
    print("4. kg")
    print("5. hg")
    print("6. dag")
    print("7. g")
    print("8. mg")
    donvi = int(input("nhập số để lựa chọn: "))
    print("1. tấn")
    print("2. tạ")
    print("3. yến")
    print("4. kg")
    print("5. hg")
    print("6. dag")
    print("7. g")
    print("8. mg")
    chuyensang = int(input("nhập số để lựa chọn: "))

    if donvi == 1 and chuyensang == 1:
        cls()
        print("vì 2 đơn vị này giống nhau nên chúng sẽ bằng nhau")
        
    elif donvi == 1 and chuyensang == 2:
        cls()
        a = float(input("nhập đơn vị đo đã có: "))
        print("kết quả là:", a*20, "tạ")
        
    elif donvi == 1 and chuyensang == 3:
        cls()
        a1 = float(input("nhập đơn vị đo đã có: "))
        print("kết quả là:", a1*100, "yến")
        
    elif donvi == 1 and chuyensang == 4:
        cls()
        a2 = float(input("nhập đơn vị đo đã có: "))
        print("kết quả là:", a2*1000, "kg")
        
    elif donvi == 1 and chuyensang == 5:
        cls()
        a3 = float(input("nhập đơn vị đo đã có: "))
        print("kết quả là:", a3*10000, "hg")
        
    elif donvi == 1 and chuyensang == 6:
        cls()
        a4 = float(input("nhập đơn vị đo đã có: "))
        print("kết quả là:", a4*100000, "dag")
        
    elif donvi == 1 and chuyensang == 7:
        cls()
        a5 = float(input("nhập đơn vị đo đã có: "))
        print("kết quả là:", format(a5*1000000, '.6f'), "g")
        
    elif donvi == 1 and chuyensang == 8:
        cls()
        a6 = float(input("nhập đơn vị đo đã có: "))
        print("kết quả là:", format(a6*1000000000, '.9f'), "mg")
        
    elif donvi == 2 and chuyensang == 1:
        cls()
        a7 = float(input("nhập đơn vị đo đã có: "))
        print("kết quả là:", a7/20, "tấn")
        
    elif donvi == 2 and chuyensang == 2:
        cls()
        print("vì 2 đơn vị này giống nhau nên chúng sẽ bằng nhau")
        
    elif donvi == 2 and chuyensang == 3:
        cls()
        a8 = float(input("nhập đơn vị đo đã có: "))
        print("kết quả là:", a8*5, "yến")
        
    elif donvi == 2 and chuyensang == 4:
        cls()
        a9 = float(input("nhập đơn vị đo đã có: "))
        print("kết quả là:", a9*50, "kg")
        
    elif donvi == 2 and chuyensang == 5:
        cls()
        a10 = float(input("nhập đơn vị đo đã có: "))
        print("kết quả là:", a10*500, "hg")
        
    elif donvi == 2 and chuyensang == 6:
        cls()
        b1 = float(input("nhập đơn vị đo đã có: "))
        print("kết quả là:",)
        
    elif donvi == 2 and chuyensang == 7:
        cls()
        b2 = float(input("nhập đơn vị đo đã có: "))