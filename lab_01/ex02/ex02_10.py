def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
input_string = input("Mời nhậP chuỗi càn đảo: ")
print("chuỗi đảo ngược là: ", dao_nguoc_chuoi(input_string))