# Base class Publisher
class Publisher:
    def __init__(self, publisher_id, publisher_name):
        self.publisher_id = publisher_id
        self.publisher_name = publisher_name

# Derived class Book
class Book(Publisher):
    def __init__(self, publisher_id, publisher_name, title, author):
        super().__init__(publisher_id, publisher_name)
        self.title = title
        self.author = author

# Derived class Python (from Book)
class Python(Book):
    def __init__(self, publisher_id, publisher_name, title, author, price, no_of_pages):
        super().__init__(publisher_id, publisher_name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages

    def display(self):
        return f"Publisher ID: {self.publisher_id}, Publisher Name: {self.publisher_name}, Title: {self.title}, Author: {self.author}, Price: {self.price}, Pages: {self.no_of_pages}"

# Main function to take user input and display Python book information
def main():
    publisher_id = input("Enter Publisher ID: ")
    publisher_name = input("Enter Publisher Name: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    price = float(input("Enter Price of the Book: "))
    no_of_pages = int(input("Enter Number of Pages: "))
    
    # Create Python book object
    python_book = Python(publisher_id, publisher_name, title, author, price, no_of_pages)
    
    # Display the information
    print("\nPython Book Information:")
    print(python_book.display())

# Run the program
if __name__ == "__main__":
    main()

