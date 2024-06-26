#importing libraries
import requests
from bs4 import BeautifulSoup #BeautifulSoup

#read the file
with open("sample.html", "r") as f:
    html_doc = f.read()

# Parse the HTML content by creating soup object
soup = BeautifulSoup(html_doc, 'html.parser')

#print the prettified soup object
print(soup.prettify())


# print the title of the HTML document with its type
print(soup.title, type(soup.title))

#find_all() method to find all the tags in the HTML document which passed as argument
print(soup.find_all("div"))   #finding all the div tags in the HTML document
#we can also use index with find_all() for example: soup.find_all("div")[0]



#Finding all the anchor tags in the HTML document
for link in soup.find_all("a"):
    print(link.get("href")) #getting the href attribute of the anchor tag
    #getting the text associated with the anchor tag
    print(link.get_text())