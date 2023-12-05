import os
def cls(): 
        os.system("cls" if os.name == "nt" else "clear")
        
def do_dai_chu_vi():
    cls()
    print("đơn vị đã có")
    print("1. mm")
    print("2. cm")
    print("3. dm")
    print("4. m")
    print("5. dam")
    print("6. hm")
    print("7. km")
    donvi = int(input("nhập số: "))
    cls()
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
        cls()
        a = float(input("nhập đơn vị đo đã có: "))
        a1 = a/10
        print("kết quả là:", a1, "cm")
        
    elif donvi == 1 and chuyensang == 3:
        cls() 
        a2 = float(input("nhập đơn vị đo đã có: "))
        a3 = a2/100
        print("kết quả là:", a3, "dm")
        
    elif donvi == 1 and chuyensang == 4:
        cls()
        a4 = float(input("nhập đơn vị đo đã có: "))
        a5 = a4/1000
        print("kết quả là:", a5, "m")
        
    elif donvi == 1 and chuyensang == 5:
        cls()
        a6 = float(input("nhập đơn vị đo đã có: "))
        a7 = a6/10000
        print("kết quả là: ", a7, "dam")
        
    elif donvi == 1 and chuyensang == 6:
        cls()
        a8 = float(input("nhập đơn vị đo đã có: "))
        a9 = a8/100000
        print("kết quả là: ", format(a9, '.5f'), "hm")
        
    elif donvi == 1 and chuyensang == 7:
        cls()
        a10 = float(input("nhập đơn vị đo đã có: "))
        b1 = a10/1000000
        print("kết quả là: ", format(b1, '.6f'), "km")
        
    elif donvi == 2 and chuyensang == 1:
        cls()
        b2 = float(input("nhập đơn vị đo đã có: "))
        b3 = b2*10
        print("kết quả là: ", b3, "mm")
        
    elif donvi == 2 and chuyensang == 3:
        cls()
        b6 = float(input("nhập đơn vị đo đã có: "))
        b7 = b6/10
        print("kết quả là: ", b7, "dm")
        
    elif donvi == 2 and chuyensang == 4:
        cls()
        b8 = float(input("nhập đơn vị đo đã có: "))
        b9 = b8/100
        print("kết quả là: ", b9, "m")
        
    elif donvi == 2 and chuyensang == 5:
        cls()
        b10 = float(input("nhập đơn vị đo đã có: "))
        c1 = b10/1000
        print("kết quả là: ", c1, "dam")
        
    elif donvi == 2 and chuyensang == 6:
        cls()
        c2 = float(input("nhập đơn vị đo đã có: "))
        c3 = c2/10000
        print("kết quả là:", c3, "hm")
        
    elif donvi == 2 and chuyensang == 7:
        cls()
        c4 = float(input("nhập đơn vị đo đã có: "))
        c5 = c4/100000
        print("kết quả là:", format(c5, '.5f'), "km")
        
    elif donvi == 3 and chuyensang == 1:
        cls()
        c6 = float(input("nhập đơn vị đo đã có: "))
        c7 = c6*100
        print("kết quả là:", c7, "mm")
        
    elif donvi == 3 and chuyensang == 2:
        cls()
        c8 = float(input("nhập đơn vị đo đã có: "))
        c9 = c8*10
        print("kết quả là:", c9, "cm")
        
    elif donvi == 3 and chuyensang == 4:
        cls()
        c10 = float(input("nhập đơn vị đo đã có: "))
        d1 = c10/10
        print("kết quả là:", d1, "m")
        
    elif donvi == 3 and chuyensang == 5:
        cls()
        d2 = float(input("nhập đơn vị đo đã có: "))
        d3 = d2/100
        print("kết quả là:", d3, "dam")
        
    elif donvi == 3 and chuyensang == 6:
        cls()
        d4 = float(input("nhập đơn vị đo đã có: "))
        d5 = d4/1000
        print("kết quả là:", d5, "hm")
        
    elif donvi == 3 and chuyensang == 7:
        cls()
        d6 = float(input("nhập đơn vị đo đã có: "))
        d7 = d6/10000
        print("kết quả là:", d7, "km")
        
    elif donvi == 4 and chuyensang == 1:
        cls()
        d8 = float(input("nhập đơn vị đo đã có: "))
        d9 = d8*1000
        print("kết quả là:", d9, "mm")
        
    elif donvi == 4 and chuyensang == 2:
        cls()
        d10 = float(input("nhập đơn vị đo đã có: "))
        e1 = d10*100
        print("kết quả là:", e1, "cm")
        
    elif donvi == 4 and chuyensang == 3:
        cls()
        e2 = float(input("nhập đơn vị đo đã có: "))
        e3 = e2*10
        print("kết quả là:", e3, "dm")
        
    elif donvi == 4 and chuyensang == 5:
        cls()
        e4 = float(input("nhập đơn vị đo đã có: "))
        e5 = e4/10
        print("kết quả là:", e5, "dam")
        
    elif donvi == 4 and chuyensang == 6:
        cls()
        e6 = float(input("nhập đơn vị đo đã có: "))
        e7 = e6/100
        print("kết quả là:", e7, "hm")
        
    elif donvi == 4 and chuyensang == 7:
        cls()
        e8 = float(input("nhập đơn vị đo đã có: "))
        e9 = e8/1000
        print("kết quả là:", e9, "km")

    elif donvi == 5 and chuyensang == 1:
        cls()
        e10 = float(input("nhập đơn vị đo đã có: "))
        f1 = e10*10000
        print("kết quả là:", f1, "mm")
        
    elif donvi == 5 and chuyensang == 2:
        cls()
        f2 = float(input("nhập đơn vị đo đã có: "))
        f3 = f2*1000
        print("kết quả là:", f3, "cm")
        
    elif donvi == 5 and chuyensang == 3:
        cls()
        f4 = float(input("nhập đơn vị đo đã có: "))
        f5 = f4*100
        print("kết quả là:", f5, "dm")
        
    elif donvi == 5 and chuyensang == 4:
        cls()
        f6 = float(input("nhập đơn vị đo đã có: "))
        f7 = f6*10
        print("kết quả là:", f7, "m")
        
    elif donvi == 5 and chuyensang == 6:
        cls()
        f8 = float(input("nhập đơn vị đo đã có: "))
        f9 = f8/10
        print("kết quả là:", f9, "hm")
        
    elif donvi == 5 and chuyensang == 7:
        cls()
        f10 = float(input("nhập đơn vị đo đã có: "))
        g1 = f10/100
        print("kết quả là:", g1, "km")
        
    elif donvi == 6 and chuyensang == 1:
        cls()
        g2 = float(input("nhập đơn vị đo đã có: "))
        g3 = g2*100000
        print("kết quả là:", g3, "mm")
        
    elif donvi == 6 and chuyensang == 2:
        cls()
        g4 = float(input("nhập đơn vị đo đã có: "))
        g5 = g4*10000
        print("kết quả là:", g5, "cm")
        
    elif donvi == 6 and chuyensang == 3:
        cls()
        g6 = float(input("nhập đơn vị đo đã có: "))
        g7 = g6*1000
        print("kết quả là:", g7, "dm")
        
    elif donvi == 6 and chuyensang == 4:
        cls()
        g8 = float(input("nhập đơn vị đo đã có: "))
        g9 = g8*100
        print("kết quả là:", g9, "m")
        
    elif donvi == 6 and chuyensang == 5:
        cls()
        g10 = float(input("nhập đơn vị đo đã có: "))
        h1 = g10*10
        print("kết quả là:", h1, "dam")
        
    elif donvi == 6 and chuyensang == 7:
        cls()
        h2 = float(input("nhập đơn vị đo đã có: "))
        h3 = h2/10
        print("kết quả là:", h3, "km")
        
    elif donvi == 7 and chuyensang == 1:
        cls()
        h4 = float(input("nhập đơn vị đo đã có: "))
        h5 = h4*1000000
        print("kết quả là:", h5, "mm")
        
    elif donvi == 7 and chuyensang == 2:
        cls()
        h6 = float(input("nhập đơn vị đo đã có: "))
        h7 = h6*100000
        print("kết quả là:", h7, "cm")
        
    elif donvi == 7 and chuyensang == 3:
        cls()
        h8 = float(input("nhập đơn vị đo đã có: "))
        h9 = h8*10000
        print("kết quả là:", h9, "dm")
        
    elif donvi == 7 and chuyensang == 4:
        cls()
        h10 = float(input("nhập đơn vị đo đã có: "))
        i1 = h10*1000
        print("kết quả là:", i1, "m")
        
    elif donvi == 7 and chuyensang == 5:
        cls()
        i2 = float(input("nhập đơn vị đo đã có: "))
        i3 = i2*100
        print("kết quả là:", i3, "dam")
        
    elif donvi == 7 and chuyensang == 6:
        cls()
        i4 = float(input("nhập đơn vị đo đã có: "))
        i5 = i4*10
        print("kết quả là:", i5, "hm")
        