print("đơn vị đã có")
print("1. mm")
print("2. cm")
print("3. dm")
print("4. m")
print("5. dam")
print("6. hm")
print("7. km")
donvi = int(input("nhập số: "))
print("chuyển sang")
print("1. mm")
print("2. cm")
print("3. dm")
print("4. m")
print("5. dam")
print("6. hm")
print("7. km")
chuyensang = int(input("nhập số: "))

if donvi == 1 and chuyensang == 2:
    a = float(input("nhập đơn vị đo đã có: "))
    a1 = a/10
    print("kết quả là:", a1, "cm")
    
elif donvi == 1 and chuyensang == 3: 
    a2 = float(input("nhập đơn vị đo đã có: "))
    a3 = a2/100
    print("kết quả là:", a3, "dm")
    
elif donvi == 1 and chuyensang == 4:
    a4 = float(input("nhập đơn vị đo đã có: "))
    a5 = a4/1000
    print("kết quả là:", a5, "m")
    
elif donvi == 1 and chuyensang == 5:
    a6 = float(input("nhập đơn vị đo đã có: "))
    a7 = a6/10000
    print("kết quả là: ", a7, "dam")
    
elif donvi == 1 and chuyensang == 6:
    a8 = float(input("nhập đơn vị đo đã có: "))
    a9 = a8/100000
    print("kết quả là: ", a9, "hm")
    
elif donvi == 1 and chuyensang == 7:
    a10 = float(input("nhập đơn vị đo đã có: "))
    b1 = a10/100000
    print("kết quả là: ", b1, "km")