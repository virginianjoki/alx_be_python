class Book:
    def __init__(self,tittle,author,year):
        self.tittle = tittle
        self.author = author
        self.year = year
  
  #string representation

    def __str__(self):
        return  f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
  #deleting
    def __del__(self):
        self.tittle
        return f"Deleting{self.tittle}"