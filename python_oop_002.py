# Define the Author class
class Author:
    def __init__(self, name: str, birth_year: int) -> None:
        self.name = name
        self.birth_year = birth_year

    def get_author_info(self) -> str:
        return f"{self.name} (born {self.birth_year})"

# Define the Book class


class Book:
    def __init__(self, title: str, publication_year: int, author: Author) -> None:
        self.title = title
        self.publication_year = publication_year
        self.author = author

    def get_book_info(self) -> str:
        return f"'{self.title}' by {self.author.get_author_info()}, published in {self.publication_year}"


# Create an Author object
author_obj = Author("George Orwell", 1903)

# Create a Book object with the Author object as a property
book_obj = Book("1984", 1949, author_obj)

# Print the book information, which includes author information
print(book_obj.get_book_info())
