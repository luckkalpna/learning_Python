x = 10   # Global variable

def my_function():
    global x
    x = 4
    y = 5  # Local variable
    print(y)

my_function()
print(x)