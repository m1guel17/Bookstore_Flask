# Bookstore Web Application

This is a simple bookstore web application built using Flask, following a layered architecture design pattern. The application is structured to separate concerns and improve maintainability by organizing code into different layers, such as presentation, business logic, and data access.

## Project Structure

Below is the directory structure of the project:
```
bookstore/
├── app/
│   ├── __init__.py
│   ├── views.py
│   ├── business_logic.py 
│   ├── data_access.py
├── templates/
│   ├── index.html
│   ├── search_results.html
│   ├── order.html
│   ├── enter_collection.html
├── static/
│   ├── style.css
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

- **templates/**: This folder contains HTML templates used to render the web pages. Each HTML file corresponds to a different page of the web application.
  - **`index.html`**: The homepage of the bookstore.
  - **`search_results.html`**: Displays the results of a book search.
  - **`order.html`**: Manages the book ordering process.
  - **`enter_collection.html`**: Register new books to the database.

- **static/**: Contains static files like CSS, JavaScript, and images.
  - **`style.css`**: Stylesheet for the web application's design and layout.

- **config.py**: Holds configuration settings for the application, such as database URIs and secret keys.

- **run.py**: The entry point for the application, used to start the Flask server.

- **requirements.txt**: Lists the Python dependencies needed to run the application. These can be installed using `pip` or `pip3.12`.

## Getting Started

### Prerequisites

- Python 3.12
- Flask
- Other dependencies listed in `requirements.txt`

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/m1guel17/Bookstore_Flask
   cd Bookstore_Flask