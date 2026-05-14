def truycap(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element
input_tuple = eval(input("Nhập tuple: "))
first, last = truycap(input_tuple)
print("PhầN tử đàu tiên: ", first)
print("PhầN tử cuối cùng: ", last)