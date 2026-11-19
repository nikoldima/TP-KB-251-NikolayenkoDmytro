class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Книга '{self.title}' (автор: {self.author}, {self.year} р.)"


def main():
    book1 = Book("Кобзар", "Тарас Шевченко", 1840)
    book2 = Book("33 стратегії війни", "Роберт Грін", 2006)

    print(book1)
    print(book2)



if __name__ == "__main__":
    main()