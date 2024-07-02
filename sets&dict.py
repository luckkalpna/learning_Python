
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

# dic = {
#     "name": "Karan",
#     "age": 20,
#     "eligible": True
# }
# # print(dic)
# # print(dic["name"])
# # print(dic.keys())

# # for key in dic.keys():
# #     print(f"The value of corrosponding to the key {key} is {dic[key]}")

# print(dic.items())

# for key, value in dic.items():
#     print(f"The value of corrosponding to the keys {key} is {value}")

# -----------------------Methods in dict-------------------

ep1 = {122: 45, 125: 67, 138: 45, 670: 97}
ep2 = {534: 95, 445: 89}
# ep1.update(ep2)     # update method
# ep1.clear()         # for clear any dict
ep1.popitem()         # for remove any last key in the liist
print(ep1)




