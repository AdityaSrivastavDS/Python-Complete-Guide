
# Open the file in read mode
f = open("E:\\Aditya\\Notes\\Python\\File IO\\Files\\demo.txt", 'r')


# Read some characters from file by passing specific number of characters
content = f.read(9)
print(content)

#closing file
f.close()