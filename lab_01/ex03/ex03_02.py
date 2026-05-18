def daonguoclist(lst):
    return lst[::-1]
input_list = input("Nhập danh sách các số, các nhau bằng dấu phẩY: ")
numbers = list(map(int, input_list.split(',')))
listdaonguoc = daonguoclist(numbers)
print("List sau khi đảo: ", listdaonguoc)