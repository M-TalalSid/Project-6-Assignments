class Book:
    total_books = 0                                # Class variable jo total books ka count rakhta hai
    
    def __init__(self, title):                     # Constructor jo book ka title set karega
        self.title = title
        Book.increment_book_count()                # Nayi book ke liye count barhaya hai
    
    @classmethod 
    def increment_book_count(cls):                 # Class method jo total books ka count barhaye ga
        cls.total_books += 1
    
    @classmethod
    def display_count(cls):                        # Class method jo total books ka count display karega
        print(f"Total books: {cls.total_books}")

book1 = Book("Harry Potter")                       # Pehli book ka object banaya hai
book2 = Book("The Witcher")                        # Dusri book ka object banaya hai

Book.display_count()                               # Total books ka count display karega