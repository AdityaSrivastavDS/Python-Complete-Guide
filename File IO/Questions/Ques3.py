#search if the word learning exists in the file or not

with open("E:\\Aditya\\Notes\\Python\\File IO\\Files\\practice.txt", "r") as f:
    data = f.read()
    
    #find() used to search for a word in a string
    #if the index of the word is not equal to -1, then the word does exist in the string
    if(data.find("learning") != -1):
        print("Word learning exists in the file")
    else:
        print("Word learning does not exist in the file")