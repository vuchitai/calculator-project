import os
def cls(): 
    os.system("cls" if os.name == "nt" else "clear")
from fractions import Fraction
print("LƯU Ý: dm3 = l \n")
print("đơn vị đã có")
print("1. mm3")
print("2. cm3")
print("3. dm3")
print("4. m3")
print("5. dam3")
print("6. hm3")
print("7. km3")
donvi = int(input("nhập số: "))
cls()
print("chuyển sang")
print("1. mm3")
print("2. cm3")
print("3. dm3")
print("4. m3")
print("5. dam3")
print("6. hm3")
print("7. km3")
chuyensang = int(input("nhập số: "))

if donvi == 1 and chuyensang == 1:
    cls()
    print("Vì hai đơn vị này giống nhau nên sẽ bằng chính nó")

elif donvi == 1 and chuyensang == 2:
    cls()
    a = float(input("nhập đơn vị đo đã có: "))
    a1 = a/1000
    print("kết quả là:", a1, "cm3")

elif donvi == 1 and chuyensang == 3:
    cls()    
    a2 = float(input("nhập đơn vị đo đã có: "))
    a3 = a2/1000000
    print("kết quả là:", format(a3, '.6f'), "dm3")

elif donvi == 1 and chuyensang == 4:
    cls()
    a4 = float(input("nhập đơn vị đo đã có: "))
    a5 = a4/1000000000
    print("két quả là:", format(a5, '.9f'), "m3")

elif donvi == 1 and chuyensang == 5:
    cls()
    a6 = float(input("nhập đơn vị đo đã có: "))
    a7 = a6/1000000000000
    print("kết quả là:", format(a7, '.12f'), "dam3")

elif donvi == 1 and chuyensang == 5:
    cls()
    a8 = float(input("nhập đơn vị đo đã có: "))
    a9 = a8/1000000000000000
    