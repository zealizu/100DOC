from flask import Flask, render_template, request, redirect, url_for  # Import Flask and related modules
from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy for database operations
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column  # Import SQLAlchemy ORM tools
from sqlalchemy import Integer, String, Float  # Import data types for columns

app = Flask(__name__)  # Create a Flask web application instance

all_books = []  # (Unused) List to store books if not using a database

# Define a base class for SQLAlchemy models
class Base(DeclarativeBase):
    pass

# Configure the SQLite database URI for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"

# Initialize the SQLAlchemy object with the custom base class
db = SQLAlchemy(model_class=Base)
db.init_app(app)  # Bind the database to the Flask app

# Define the Book model/table
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Primary key column
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)  # Book title (unique, required)
    author: Mapped[str] = mapped_column(String(250), nullable=False)  # Author name (required)
    rating: Mapped[float] = mapped_column(Float, nullable=False)  # Book rating (required)

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()

# Home route: display all books in the database, ordered by title
@app.route('/')
def home():
    return render_template(
        "index.html",
        books=db.session.execute(db.select(Book).order_by(Book.title)).scalars()
    )

# Add route: handle GET (show form) and POST (add book) requests
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        data = request.form  # Get form data from the request
        title = data["title"]
        author = data["author"]
        rating = float(data["rating"])
        new_book = Book(title=title, author=author, rating=rating)  # Create a new Book object
        db.session.add(new_book)  # Add the new book to the session
        db.session.commit()  # Commit the session to save the book
        print(all_books)  # (Unused) Print the all_books list
        return redirect(url_for('home'))  # Redirect to the home page after adding
    return render_template("add.html")  # Show the add book form

# Edit route: handle GET (show form) and POST (update rating) requests
@app.route("/edit", methods=["POST", "GET"])
def edit():
    id = request.args.get("id")  # Get the book ID from the URL query string
    book = db.get_or_404(Book, id)  # Get the book from the database or return 404 if not found
    if request.method == "POST":
        rating = request.form["rating"]  # Get the new rating from the form
        book.rating = float(rating)  # Update the book's rating
        db.session.commit()  # Save changes to the database
        return redirect(url_for("home"))  # Redirect to the home page after editing
    return render_template("edit.html", book=book)  # Show the edit form with the book's data

# Delete route: delete a book by ID
@app.route("/delete")
def delete():
    id = request.args.get('id')  # Get the book ID from the URL query string
    book = db.get_or_404(Book, id)  # Get the book from the database or return 404 if not found
    print(book.title)  # Print the title of the book being deleted (for debugging)
    db.session.delete(book)  # Delete the book from the session
    db.session.commit()  # Commit the session to delete the book from the database
    return redirect(url_for('home'))  # Redirect to the home page after deletion

# Run the Flask app in debug mode if this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)

