#accessing file
# w+ truncate the file from the beginning which means it will delete all the content of the file

data = open("E:\\Aditya\\Notes\\Python\\File IO\\Files\\demo.txt", "w+")

data.write("Javascript is used for backend development")

print(data.read())

data.close()