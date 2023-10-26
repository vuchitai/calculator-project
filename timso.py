def tim_uoc_chung_va_boi_chung_cua_nhieu_so():
  
  import math

  # Nhập danh sách các số từ người dùng
  num_list = input("Nhập các số cách nhau bằng dấu cách: ").split()
  num_list = [int(num) for num in num_list]

  # Tìm ước chung lớn nhất (GCD) của danh sách các số
  gcd_result = num_list[0]
  for num in num_list[1:]:
      gcd_result = math.gcd(gcd_result, num)

  # Tìm bội chung nhỏ nhất chung (LCM) của danh sách các số
  lcm_result = num_list[0]
  for num in num_list[1:]:
      lcm_result = lcm_result * num // math.gcd(lcm_result, num)

  print(f"Ước chung lớn nhất (GCD) của danh sách là: {gcd_result}")
  print(f"Bội chung nhỏ nhất (LCM) của danh sách là: {lcm_result}")


