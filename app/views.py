from flask import render_template, request, redirect, url_for, flash
from . import create_app
from .business_logic import get_books, search_books, place_order, add_book

def init_app(app):
    @app.route('/')
    def index():
        books = get_books()
        return render_template('index.html', books=books)

    @app.route('/enter_collection', methods=['GET', 'POST'])
    def enter_collection():
        if request.method == 'POST':
            title = request.form['title']
            author = request.form['author']
            price = float(request.form['price'])
            stock = int(request.form['stock'])
            
            if add_book(title, author, price, stock):
                flash('Book added successfully!')
                return redirect(url_for('index'))
            else:
                flash('Error adding book.')
    
        return render_template('enter_collection.html')
    
    @app.route('/search', methods=['POST'])
    def search():
        title = request.form.get('title')
        results = search_books(title)
        return render_template('search_results.html', results=results)

    @app.route('/order/<int:book_id>', methods=['GET', 'POST'])
    def order(book_id):
        if request.method == 'POST':
            quantity = int(request.form.get('quantity'))
            success = place_order(book_id, quantity)
            if success:
                return redirect(url_for('index'))
            else:
                return "Not enough stock", 400
        return render_template('order.html', book_id=book_id)
