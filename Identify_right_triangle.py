import os
def cls(): 
    os.system("cls" if os.name == "nt" else "clear")

def tam_giac_vuong():
    a = int(input("nhập vào số a: "))
    b = int(input("nhập vào số b: "))
    c = int(input("nhập vào số c: "))

    cls()

    tam_giac = a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2
    if tam_giac:
        print("đây là tam giác vuông")
    else:
        print("đây không phải là tam giác vuông")
        
        