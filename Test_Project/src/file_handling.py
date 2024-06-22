# Open a file in write mode
file = open('newFile.txt', 'w')
file.write("This is a new File!!!\n")
file.close()

# Open a file in read mode
file = open('newFile.txt', 'r')
content = file.read()

print(content)
file.close()

# Open the file in append mode
file = open('newFile.txt', 'a')
file.write("This is my second line!!!")
file.close()