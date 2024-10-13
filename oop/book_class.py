class Book:
    def _init_(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
 #deleting
    def _del_(self):
        return f"Deleting{self.title}"
        
  
  #string representation

    def _str_(self):
        return  f"{self.title} by {self.author}, published in {self.year}"
    
    def _repr_(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
