
# ---------------------------Sets in Python---------------------------

# s = {2, 4, 6, 8}
# print(s)

# info = {"Hello", 2, 5, True, 2.21}
# print(info)

# # For access any empty set

# empty = set()
# print(type(empty))

# for value in info:
#     print(value)




# ------------------------Dictionary in python--------------------

dic = {
    "name": "Karan",
    "age": 20,
    "eligible": True
}
# print(dic)
# print(dic["name"])
# print(dic.keys())

# for key in dic.keys():
#     print(f"The value of corrosponding to the key {key} is {dic[key]}")

print(dic.items())

for key, value in dic.items():
    print(f"The value of corrosponding to the key {key} is {value}")