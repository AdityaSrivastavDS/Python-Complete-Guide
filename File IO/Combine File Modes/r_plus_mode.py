#accessing file 
# r+ means read and write mode
# r+ overwrite the file from the beginning

data = open("E:\\Aditya\\Notes\\Python\\File IO\\Files\\demo.txt", "r+")


#writing to file
data.write("You")

print(data.read())


data.close()