class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
  
  #string representation

    def __str__(self):
        return  f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
  #deleting
    def __del__(self):
        self.title
        return f"Deleting{self.title}"