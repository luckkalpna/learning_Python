tup = (1,4,2,6,4,7,9, "Green", True)
# print(tup)
print(type(tup), tup)
# print(tup[0])
# print(tup[1])
# print(tup[2])
# print(tup[3])
print(len(tup))

if 4 in tup:
    print("Yes 4 is present in tuple")
else:
    print("This element is not in tuple")

tup2 = tup[1:5]   # this create a new tuple not change existing tuple
print(tup2)