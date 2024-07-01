list = [3,5,7,9,"New",11]
# print(list)
# print(type(list))
# print(list[0])
# print(list[1])
# print(list[2])

# -------------------Negative Indexing------------------
# print(list[-3])
# print(list[len(list)-3])
# print(list[5-3])
# print(list[2])


# -----------------Finding any element in the list------------------

# if 4 in list:
#     print("Yes")
# else:
#     print("NO")


# if "New" in list:
#     print("Yes")
# else:
#     print("NO")


# -------------------Comprehension list-----------------

# marks1 = [i for i in range(5)]
# print(marks1)

# marks2 = [i*i for i in range(5)]
# print(marks2)

# -------------------Comprehension list using For if condition-----------------

# marks = [i for i in range(20) if(i%2==0)]
# print(marks)


# ------------------------list methods-------------------------

l =[11, 34, 3, 6, 32, 2, 9, 9]
print(l)
# l.append(100)  # For adding an element

# l.sort(reverse=True)
# l.reverse()
# print(l.index(6))   # For finding any index position exist in list
print(l.count(6))     # For count any item in the list
# print(l)
