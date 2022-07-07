# ************** Compulsory Task **************
'''
This is aprogram for a application used to manage a database
books of ebooks
'''
import sqlite3

# Populating table with existing books
book_ = [
    (3001, "A Tale of Two Cities", "Charles Dickens", 30),
    (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40),
    (3003, "The Lion, the Witch and the Wardrobe", "C. S. Lewis", 25),
    (3004, "The Lord of the Rings", "J.R.R Tolkien", 37),
    (3005, "Alice in Wonderland", "Lewis Carroll", 12),
]




class Database:
    """
    This class defines a record for an ebook in a database called
    ebookstore. This class initializes the cursor for the instance
    """

    def __init__(self):
        self.ebookstore = sqlite3.connect("database_file")
        self.cursor = self.ebookstore.cursor()

    def enter(self, id, Title, Author, Qty):
        """
        Enter new book
        """
        self.cursor.execute(
            """INSERT OR IGNORE INTO books(id, Title, Author, Qty)
                               VALUES(:id,:Title,:Author,:Qty)""",
            {"id": id, "Title": Title, "Author": Author, "Qty": Qty},
        )

    def enter_multiple(self, new_books):
        self.cursor.executemany(
            """INSERT OR IGNORE INTO books(id, Title, Author, Qty)
                               VALUES(?,?,?,?)""",
            new_books,
        )

    def update(self, Qty, id):
        """
        Change record of book
        """
        self.cursor.execute("""UPDATE books SET Qty = ? WHERE id = ?""", (Qty, id))

    def delete(self, id):
        """
        Remove record
        """
        self.cursor.execute("""DELETE FROM books WHERE id = ?""", (id,))

    def search(self, id):
        """
        find record
        """
        self.cursor.execute(
            """SELECT id, Title, Author, Qty FROM books WHERE
        id = ?""",
            (id,),
        )
        book = self.cursor.fetchone()
        print(book)
        print('\n')

    def exit(self):
        """
        close database
        """
        self.cursor.execute('DROP TABLE books')
        self.ebookstore.close()

    def create(self):
        """
        Create database if non existant
        """
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY,
            Title TEXT, Author TEXT, Qty INTEGER)"""
        )

    def commit(self):
        """
        Commit changes to database
        """
        self.ebookstore.commit()


# Creating instance of books databae
books_ = Database()
books_.create()
books_.enter_multiple(book_)
books_.commit()

Prompt = 1  # Initializing option
while int(Prompt) != 0:
    Prompt = int(
        input(
            """\nChoose option 1,2,3,4 and 0 to exit
               1. Enter book
               2. Update book
               3. Delete book
               4. Search books
               0. Exit
               : """
        )
    )

    if int(Prompt) == 1:
        id = int(input("\nEnter unique ID of to identify the book"))
        title = input("\nEnter the title of the book : ")
        author = input(f"\nEnter the author of {title}: ")
        qty = int(
            input(f"\nHow many copies of stock are available for the book {title} : ")
        )
        books_.enter(id, title, author, qty)
        books_.commit()

    elif Prompt == 2:
        id = int(
            input("\nWhat is the ID identifier of book stock availability to be update: ")
        )
        qty = int(input(f"\nHow many books are available of book with ID: {id} : "))
        books_.update(qty, id)
        books_.commit()

    elif Prompt == 3:
        id = int(
            input(
                "\nPlease enter ID of book you would like to remove from the database: "
            )
        )
        books_.delete(id)
        books_.commit()

    elif Prompt == 4:
        id = int(input("\nEnter ID of book you would like to check availability of: "))
        books_.search(id)
books_.commit()
books_.exit()

