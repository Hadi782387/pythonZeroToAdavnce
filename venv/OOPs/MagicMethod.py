# magic methods are methods to customize the class and object
class Book:
    def __init__(self,title,author,num_pages):
        self.title=title
        self.author=author
        self.num_pages=num_pages
    def __str__(self):
        return f"{self.title} {self.author} {self.num_pages}"
    def __eq__(self, other):
        return self.title==other.title and self.author==other.author
    def __lt__(self, other):
        return self.num_pages<other.num_pages
    def __gt__(self, other):
        return self.num_pages>other.num_pages
    def __add__(self, other):
        return self.num_pages+other.num_pages
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    def __getitem__(self, item):
        if item=='title':
            return self.title
        elif item=='author':
            return self.author
        elif item=='num_pages':
            return self.num_pages
        else:
            return "error"


Book1=Book("harry potter","jk rowlin",123)
Book2=Book("harry potter","jk rowlin",223)
Book3=Book("parry potter 3","jk rowlin",323)
print(Book1,"\n",Book2,"\n",Book3)
print(Book1==Book2)
print(Book3>Book2)
print(Book1<Book2)
print(Book1+Book3)
print("harry" in Book3)
print(Book3['num_pages'])