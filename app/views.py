from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from .business_logic import get_books, search_books, place_order, add_book

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

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
            
            if 'image' in request.files:
                file = request.files['image']
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    ext = filename.split(".")[-1]
                    name_img = title + "." + ext
                    file.save(os.path.join('static/images', name_img))
                    
            if add_book(title, author, price, stock, name_img):
                flash('Book added successfully!')
                return redirect(url_for('index'))
            else:
                flash('Error adding book.')
    
        return render_template('enter_collection.html')
    
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
    @app.route('/search', methods=['POST'])
    def search():
        title = request.form.get('title')
        results = search_books(title)
        return render_template('search_results.html', results=results, query=title)

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
