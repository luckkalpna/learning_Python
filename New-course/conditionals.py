a = int(input("Enter your age: "))

# if(a>=18):
#   print("Your are above the age of consent")
#   print("Good To Go")

# else:
#   print("Your are below the age of consent")

if(a>=18):
  print("Your are above the age of consent")
  print("Good To Go")

elif(a<0):
  print("You are entering an invalid negative age")

elif(a==0):
  print("Your are entering 0 which is not a valid age")

else:
  print("Your are below the age of consent")

print("End of Program")