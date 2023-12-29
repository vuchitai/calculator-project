import os
def cls(): 
    os.system("cls" if os.name == "nt" else "clear")
import random



print("bạn đã chọn dạng bài tập thêm \nbạn muốn làm dạng bài nào?")
print("1. hình học \n2. số học")
choose = int(input("nhập số để lựa chọn: "))
print("1. trắc nghiệm \n2. tự luận")
choose1 = int(input("nhập số để lựa chọn: "))
print("1. dễ \n2. vừa \n3. khó")
choose2 = int(input("nhập số để lựa chọn: "))

if choose == 1 and choose1 == 1 and choose2 == 1:
    cls()
    print("bạn đã chọn dạng bài tập hình học kiểu trắc nghiệm mức độ dễ")
    
    