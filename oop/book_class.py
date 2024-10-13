class Book:
    def _init_(self, title, author, year):
        #Initialize a Book instance with title, author, and year.
        self.title = title
        self.author = author
        self.year = year

    def _del_(self):
        #Destructor method that prints a message when a Book instance is deleted.
        print(f"Deleting {self.title}")

    def _str_(self):
        #String representation of the Book instance for human-readable format.
        return f"{self.title} by {self.author}, published in {self.year}"

    def _repr_(self):
        #String representation of the Book instance for debugging purposes.
        return f"Book('{self.title}', '{self.author}', {self.year})"