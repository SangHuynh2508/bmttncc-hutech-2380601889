def delptu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
my_dict = {'a': 1,'b': 2,'c': 3,'d': 4,}
keytodel = "b"
result = delptu(my_dict, keytodel)
if result:
    print("Phần tử đã đc xoá từ dict: ", my_dict)
else:
    print("Không tìm thấY phần tử cần xoá trong dict")