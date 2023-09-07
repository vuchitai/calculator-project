def tinh_so_thuong():
    number1 = float(input("Nhập số đầu tiên để thực hiện phép tính: "))
    operation = input("Nhập dấu để tính ( cộng, trừ, nhân, hoặc chia ): ")
    number2 = float(input("Nhập số thứ hai để thực hiện phép tính: "))

    if operation == "cộng":
        result = number1 + number2
    elif operation == "trừ":
        result = number1 - number2
    elif operation == "nhân":
        result = number1 * number2
    elif operation == "chia":
        result = number1 / number2
            
    return result