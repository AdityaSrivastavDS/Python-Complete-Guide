from tkinter import END, Tk, Label, Entry, Button, Text, StringVar

# Data storage (dictionary)
books = {}


def add_book():
  title = title_var.get()
  author = author_var.get()
  if not title or not author:
    message_var.set("Please fill both Title and Author fields.")
    return
  book_id = len(books) + 1
  books[book_id] = {"title": title, "author": author, "available": True}
  message_var.set(f"Book '{title}' added successfully (ID: {book_id})")
  title_var.set("")
  author_var.set("")
  update_book_list()


def view_books():
  book_list.delete(0.0, END)
  if not books:
    book_list.insert(END, "No books found in the library.")
    return
  for book_id, book_details in books.items():
    availability = "Available" if book_details["available"] else "Not Available"
    book_list.insert(END, f"ID: {book_id} - Title: {book_details['title']}, Author: {book_details['author']}, Availability: {availability}")


def search_book():
  title = title_var.get().lower()
  found_books = []
  for book_id, book_details in books.items():
    if title in book_details["title"].lower():
      found_books.append(f"ID: {book_id}, Title: {book_details['title']}")
  book_list.delete(0.0, END)
  if found_books:
    book_list.insert(END, f"Found books matching '{title}':")
    for book in found_books:
      book_list.insert(END, book)
  else:
    book_list.insert(END, f"No book found with title '{title}'.")
  title_var.set("")


def update_book_list():
  view_books()


# Initialize Tkinter window
window = Tk()
window.title("Library Management System")

# Title and Author labels and entries
title_label = Label(window, text="Book Title:")
title_label.grid(row=0, column=0, padx=5, pady=5)
title_var = StringVar()
title_entry = Entry(window, textvariable=title_var)
title_entry.grid(row=0, column=1, padx=5, pady=5)

author_label = Label(window, text="Book Author:")
author_label.grid(row=1, column=0, padx=5, pady=5)
author_var = StringVar()
author_entry = Entry(window, textvariable=author_var)
author_entry.grid(row=1, column=1, padx=5, pady=5)

# Add book button
add_button = Button(window, text="Add Book", command=add_book)
add_button.grid(row=2, columnspan=2, padx=5, pady=5)

# Message label
message_var = StringVar()
message_label = Label(window, textvariable=message_var, fg="red")
message_label.grid(row=3, columnspan=2, padx=5, pady=5)

# Book list Text widget
book_list = Text(window, height=10, width=50)
book_list.grid(row=4, columnspan=2, padx=5, pady=5)

# View books button
view_books_button = Button(window, text="View Books", command=view_books)
view_books_button.grid(row=5, column=0, padx=5, pady=5)

# Search book button
search_button = Button(window, text="Search Book", command=search_book)
search_button.grid(row=5, column=1, padx=5, pady=5)

# Run the main loop
window.mainloop()
