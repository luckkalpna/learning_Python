# ----Clasess and objects--------

# class Person:
#   name= "Kalpna"
#   occ= "Software Developer"
#   neworth = 10

#   # def info(self):
#   #   print(f"{self.name} is a {self.occ}")

# a = Person()

# a.name = "Ravi"
# a.occ = "Tester"
# print(a.name, a.occ)

# --------------------------------------------------------------------

# -----Constructors------

# class Person:
#   def __init__(self, n, o):
#     print("Hey I am a Person")
#     self.name = n
#     self.occ = o

#   def info(self):
#     print(f"{self.name} is a {self.occ}")

# a = Person("Kalpna", "Developer")
# b = Person("Divya", "HR")
# a.info()
# b.info()

# --------------------------------------------------------------------

# -------Decorators---------

def greet(fx):
  def mfx():
    print("Good Morning")
    fx()
    print("Thanks for using this function")
  return mfx
  
@greet
def hello():
  print("Hello World")

hello()