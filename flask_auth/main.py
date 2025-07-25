from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory  # Import Flask and related modules
from werkzeug.security import generate_password_hash, check_password_hash  # For password hashing and verification
from flask_sqlalchemy import SQLAlchemy  # For database operations
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column  # SQLAlchemy ORM tools
from sqlalchemy import Integer, String  # Data types for columns
from sqlalchemy.exc import IntegrityError  # For handling unique constraint errors
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user  # For user session management

app = Flask(__name__)  # Create Flask app instance
app.config['SECRET_KEY'] = 'secret-key-goes-here'  # Secret key for session and security

# CREATE DATABASE


class Base(DeclarativeBase):
    pass  # Base class for SQLAlchemy models


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite database URI
db = SQLAlchemy(model_class=Base)  # Initialize SQLAlchemy with custom base
db.init_app(app)  # Bind database to Flask app

# CREATE TABLE IN DB


class User(UserMixin, db.Model):
    # User model for authentication
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Primary key
    email: Mapped[str] = mapped_column(String(100), unique=True)  # User email (unique)
    password: Mapped[str] = mapped_column(String(100))  # Hashed password
    name: Mapped[str] = mapped_column(String(1000))  # User's name


with app.app_context():
    db.create_all()  # Create tables in the database if they don't exist

login_manager = LoginManager()  # Initialize Flask-Login manager
login_manager.init_app(app)  # Bind login manager to Flask app


@login_manager.user_loader
def load_user(user_id):
    # Callback to reload the user object from the user ID stored in the session
    return db.get_or_404(User, user_id)


@app.route('/')
def home():
    # Home page route
    return render_template("index.html")


@app.route('/register', methods=["POST", "GET"])
def register():
    # Registration route for new users
    data = request.form
    if request.method == "POST":
        try:
            # Hash the password before storing
            password = generate_password_hash(password=data["password"], method="pbkdf2:sha256", salt_length=8)
            new_user = User(email=data["email"], password=password, name=data["name"])
            db.session.add(new_user)  # Add new user to the database
            db.session.commit()  # Commit changes
            login_user(new_user)  # Log in the new user
            return redirect(url_for("secrets"))  # Redirect to secrets page
        except IntegrityError:
            # Handle duplicate user registration
            flash("User Already Exists in the Database Please Login")
    return render_template("register.html")  # Show registration form


@app.route('/login', methods=["POST", "GET"])
def login():
    # Login route for existing users
    if request.method == "POST":
        data = request.form
        # Find user by email
        user = db.session.execute(db.select(User).where(User.email == data["email"])).scalar()
        if user:
            # Check password
            if check_password_hash(user.password, data["password"]):
                login_user(user)  # Log in user
                return redirect(url_for('secrets'))  # Redirect to secrets page
            else:
                flash("wrong password")  # Incorrect password
        else:
            flash("You need to create an account")  # User not found
    return render_template("login.html")  # Show login form


@app.route('/secrets')
@login_required
def secrets():
    # Protected route, only accessible to logged-in users
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
def logout():
    # Log out the current user and redirect to home
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    # Protected route to download a file
    directory = 'static/files'  # Directory containing files to download
    return send_from_directory(directory, "cheat_sheet.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app in debug mode
