def tuplelist(lst):
    return tuple(lst)
input_list = input("Nhập danh sách các số, các nhau bằng dấu phẩY: ")
numbers = list(map(int, input_list.split(',')))
my_tuple = tuplelist(numbers)
print("list: ", numbers)
print("Tuple từ list: ", my_tuple)