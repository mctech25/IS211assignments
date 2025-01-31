class Book:
    def __init__(self, author, title):
     self.author = author
     self.title = title

    def display(self):
        print(f"{self.title}, written by {self.author}")

# Instantiate two books
book1 = Book("J.K Rowling", "Harry Potter and the Goblet of Fire", )
book2 = Book("Water Scott", "Ivanhoe:A Romance", )

#Display book details
book1.display()
book2.display()
