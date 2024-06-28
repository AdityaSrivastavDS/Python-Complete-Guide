
#accessing file in a mode means append which refers to add at the end

f = open("E:\\Aditya\\Notes\\Python\\File IO\\Files\\demo.txt", 'a')

#appending to file
f.write("Javascript is used for backend development")
f.write("\n after learning Python I will learn Javascript")
f.close()