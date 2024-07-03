# MAP

def  cube(x):
    return x * x * x

print(cube(2))



l = [1,2,3,4,5,6]
newl = list(map(cube,l))
print(newl)


# FILTER

def filter_function(a):
    return a>4

newnewl = list(filter(filter_function, l))
print(newnewl)


# REDUCE Function

from functools import reduce

number = [1,2,3,4,5]

sum = reduce(lambda x, y: x + y, number)
print(sum)