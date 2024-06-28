# Write a function that replace occurences of "python" with java in above file

def replace_word():
    with open("E:\\Aditya\\Notes\\Python\\File IO\\Files\\practice.txt", "r") as f:
        data = f.read()

    new_data = data.replace("Python", "Java")

    with open("E:\\Aditya\\Notes\\Python\\File IO\\Files\\practice.txt", "w") as f:
        f.write(new_data)

    print(new_data)

# Call the function
replace_word()