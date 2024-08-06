# Bookstore Web Application

This is a simple bookstore web application built using Flask, following a layered architecture design pattern. The application is structured to separate concerns and improve maintainability by organizing code into different layers, such as presentation, business logic, and data access.

<p align="center">
<img src="https://github.com/user-attachments/assets/c6e89c40-8455-46d6-ae21-a6c64c440c30" width="720">
</p>

## Project Structure

Below is the directory structure of the project:
```
bookstore/
├── app/
│   ┠── __init__.py
│   ┠── views.py
│   ┠── business_logic.py 
│   ┖── data_access.py
|
├── instance/
│   ┖── bookstore.db
|
├── templates/
│   ┖─ html files
|
├── static/
│   ┠── styles/
│   ┃   ┖── css files
│   ┠── scripts/
│   ┃   ┖── javascript files
│   ┖── images/
├── config.py
├── run.py
└── requirements.txt
```
### Description of Key Components

- **app/**: This directory contains the core application files.
  - **`__init__.py`**: Initializes the Flask application and sets up configurations.
  - **`views.py`**: Handles the routes and HTTP requests. This is the presentation layer where the user interface logic resides.
  - **`business_logic.py`**: Contains the business rules and application logic, ensuring that all operations are performed as expected.
  - **`data_access.py`**: Responsible for data management and interactions with the database. This layer abstracts the database operations from the rest of the application.

- **instance/**: This directory contains instance-specific files, such as the SQLite database. _This folder and its content will be created when you deploy this application_
  - **`bookstore.db`**: The SQLite database file for storing book information.

- **templates/**: This folder contains HTML templates used to render the web pages. Each HTML file corresponds to a different page of the web application.

- **static/**: Contains static files like CSS, JavaScript, and images.
  - **styles/**: This directory contains stylesheets for the web application's design and layout.
  - **scripts/**: This directory contains JavaScript files for client-side functionality.

  - **images/**: Directory for storing image assets.

- **config.py**: Holds configuration settings for the application, such as database URIs and secret keys.

- **run.py**: The entry point for the application, used to start the Flask server.

- **requirements.txt**: Lists the Python dependencies needed to run the application. These can be installed using `pip`.

## Getting Started

### Prerequisites

- Python 3.12
- Flask
- Other dependencies listed in `requirements.txt`

### Deployment

1. **Clone the repository:**
   ```bash
   git clone https://github.com/m1guel17/Bookstore_Flask
   ```
2. **Navigate to the project directory:**
   ```bash
   cd Bookstore_Flask
   ```
3. **Run the application:**
   ```bash
   python3.12 run.py
   ```
   The application will be accessible at http://localhost:80.

## Usage

- **Index**: Navigate to the homepage to view available books.
- **Search**: Use the search functionality to find specific books.
- **Order**: Follow the steps to order books from the collection.
- **Add Books**: Use the enter collection page to add new books to the database.
