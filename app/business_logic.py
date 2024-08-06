from .data_access import Book, Order, User, db
from werkzeug.security import generate_password_hash, check_password_hash

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

def add_book(title, author, price, stock, image):
    new_book = Book(title=title, author=author, price=price, stock=stock, image = image)
    try:
        db.session.add(new_book)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        db.session.rollback()
        return False

def register_user(username, password):
    if User.query.filter_by(username=username).first() is not None:
        return False
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)
    try:
        db.session.add(new_user)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        db.session.rollback()
        return False

def verify_login(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return True
    return False
