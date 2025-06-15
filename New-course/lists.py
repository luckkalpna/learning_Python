friends = ["Apple", "Orange", 2, 3.04, False, "Akash", "Rohan"]
# print(friends)
# print(type(friends))
# print(friends[0])
# print(friends[1:4])

friends[0] = "Grapes"
# print(friends[0]) # Lists are mutable we can change easily

# -----------Methods of lists--------------

friends.append("Kalpana") # adding element in the end of list
# print(friends)

l1 = [1, 23, 34, 4345, 4, 9, 234]
# l1.sort()
# l1.reverse()
# l1.insert(3, 111) # Insert any value in between the list as per given index
# l1.pop(2) # remove any value fron the list items
print(l1.pop(2))
print(l1)


