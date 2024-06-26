# Define a class named BookShelf
class BookShelf:
    # The constructor method that initializes the quantity of books on the shelf
    def __init__(self, quantity):
        self.quantity = quantity

    # The string representation method for a BookShelf object
    def __str__(self):
        return f"Book {self.name} with {self.quantity} books."

# Create an instance of BookShelf with 300 books
shelf = BookShelf(300)


# Define a class named Book that inherits from BookShelf
class Book(BookShelf):
    # The constructor method that initializes the name and quantity of a book
    def __init__(self, name, quantity):
        # Call the constructor of the parent class
        super().__init__(quantity)
        # Initialize the name of the book
        self.name = name

# Create an instance of Book with the name "Harry Potter" and 120 books
book = Book("Harry potter", 120)

print(book)
