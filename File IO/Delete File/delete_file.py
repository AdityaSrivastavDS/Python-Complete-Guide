'''We can't directly remove files from the computer using Python. We need to import the os module and use the os.remove() method to delete a file. The os.remove() method deletes the file path you provide as an argument. If the file does not exist, it raises an error. To avoid this error, you can use the os.path.exists() method to check if the file exists before deleting it. If the file exists, you can delete it using the os.remove() method. Here is an example that demonstrates how to delete a file using Python.
For that we have to use os module of Python. os module provides a way of using operating system dependent functionality. The functions that the OS module provides allows you to interface with the underlying operating system that Python is running on – be that Windows, Mac or Linux.'''


#importing os module
import os


#deleting file
os.remove("E:\\Aditya\\Notes\\Python\\File IO\\Files\\sample.txt")