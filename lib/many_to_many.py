class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return list({contract.author for contract in self.contracts()})

    def __repr__(self):
        return f"Book(title='{self.title}')"

class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return list({contract.book for contract in self.contracts()})

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

    def __repr__(self):
        return f"Author(name='{self.name}')"

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = None
        self.book = None
        self.date = None
        self.royalties = None

        self.set_author(author)
        self.set_book(book)
        self.set_date(date)
        self.set_royalties(royalties)

        Contract.all.append(self)

    def set_author(self, author):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        self.author = author

    def set_book(self, book):
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        self.book = book

    def set_date(self, date):
        if not isinstance(date, str):
            raise Exception("date must be a string")
        self.date = date

    def set_royalties(self, royalties):
        if not isinstance(royalties, (int, float)):
            raise Exception("royalties must be a number")
        self.royalties = royalties

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

    def __repr__(self):
        return f"Contract(author={self.author.name}, book={self.book.title}, date='{self.date}', royalties={self.royalties})"
