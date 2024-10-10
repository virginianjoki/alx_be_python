class Book:
    def __init__(self,tittle,author,year):
        self.tittle = tittle
        self.author = author
        self.year = year
  #deleting year

    def __del__ (self):
        self.tittle
        return "Deleting (tittle of the book)"
  #string representation

    def __str__(self):
        return  f"{self.title} by {self.author}, published in {self.year}".
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})".