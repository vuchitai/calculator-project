from fractions import Fraction
def tinh_phan_so():
    
    number3 = Fraction(input("Nhập số đầu tiên để thực hiện phép tính: "))
    operations = input("Nhập dấu để tính ( cộng, trừ, nhân, hoặc chia ): ")
    number4 = Fraction(input("Nhập số thứ hai để thực hiện phép tính: "))

    if operations == "cộng":
        result2 = number3 + number4
    elif operations == "trừ":
        result2 = number3 - number4
    elif operations == "nhân":
        result2 = number3 * number4
    elif operations == "chia":
        result2 = number3 / number4
    print("kết quả là:", result2)
    
    return result2