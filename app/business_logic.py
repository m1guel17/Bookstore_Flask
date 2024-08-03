from .data_access import Book, Order, db

def get_books():
    return Book.query.all()

def search_books(title):
    return Book.query.filter(Book.title.contains(title)).all()

def place_order(book_id, quantity):
    book = Book.query.get(book_id)
    if book and book.stock >= quantity:
        book.stock -= quantity
        total_price = book.price * quantity
        order = Order(book_id=book.id, quantity=quantity, total_price=total_price)
        db.session.add(order)
        db.session.commit()
        return True
    return False

def add_book(title, author, price, stock):
    new_book = Book(title=title, author=author, price=price, stock=stock)
    try:
        db.session.add(new_book)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        db.session.rollback()
        return False