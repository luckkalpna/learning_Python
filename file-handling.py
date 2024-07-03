# READING A FILE

# f = open("myfile.txt", "r")
# text = f.read()  # For reading text
# print(text)
# f.close()        # For closing file

# WRITING A FILE & CREATE A NEW FILE

# f = open("myfile2.txt", "w")
# f.write("Hello World")
# f.close()

# APPEND ANY FILE

# f = open("myfile.txt", "a")
# f.write(" Hello World")
# f.close()

# USING WITH METHOD FOR ALL METHODS

with open("myfile.txt", "a") as f:
    f.write(" Hey I am here")