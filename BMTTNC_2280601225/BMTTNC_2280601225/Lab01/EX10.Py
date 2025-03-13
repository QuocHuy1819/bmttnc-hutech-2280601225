def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
# Sử dụng hàm và in kết quả
input_string = input("Mời nhập chuỗi cần dảo ngược: ")
print("Chuỗi dảo ngược là: ", dao_nguoc_chuoi(input_string))