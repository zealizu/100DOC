from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, desc
from flask_wtf import FlaskForm
from wtforms import FloatField,StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange, InputRequired
from dotenv import load_dotenv
import os
import requests

load_dotenv()

ACCESS_TOKEN = os.environ["API_TOKEN"]
API_KEY = os.environ["API_KEY"]
class EditForm(FlaskForm):
    rating = FloatField(label="Your Rating out of 10 Eg 7.5", validators=[InputRequired(), NumberRange(0,10)])
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")

class AddForm(FlaskForm):
    title = StringField(label="Add Movie", validators=[InputRequired()])
    submit = SubmitField(label="Submit")
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstap = Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///movies.db"
db.init_app(app)
# CREATE TABLE
class Movie(db.Model):
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    title:Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description:Mapped[str] = mapped_column(String, nullable=False)
    rating:Mapped[float] = mapped_column(Float, nullable=True)
    ranking:Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
with app.app_context():
    db.create_all()


# with app.app_context():
#     new_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#     )
#     # db.session.add(new_movie)
#     # db.session.commit()

@app.route("/")
def home():
    movies = list(db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars())
    movie_id = request.args.get("id")
    if movie_id:
        print("populated")
        configuration_url = "https://api.themoviedb.org/3/configuration"
        movie_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        header = {
            'Authorization': f"Bearer {ACCESS_TOKEN}",
            'accept': 'application/json'
        }
        configuration_response= requests.get(url=configuration_url, headers=header)
        MOVIE_DB_IMAGE_URL= f"{configuration_response.json()['images']['base_url']}original"
        response = requests.get(url=movie_url, headers=header)
        data = response.json()
        new_movie = Movie(
            title=data["original_title"],
            year=data["release_date"].split("-")[0],
            description=data["overview"],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data["poster_path"]}"
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit', id=new_movie.id))
    
    for i in range(len((movies))):
        movies[i].ranking = i + 1
        db.session.commit()
    
    return render_template("index.html", movies=movies)

@app.route("/edit", methods=["POST", "GET"])
def edit():
    form=EditForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.data["rating"])
        movie.review = form.data["review"]
        db.session.commit()
        return redirect(url_for("home"))
    
    return render_template("edit.html", form=form, movie_title= movie.title)

@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["POST", "GET"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        header = {
            'Authorization': f"Bearer {ACCESS_TOKEN}",
            'accept': 'application/json'
        }
        params = {
            "query": form.data["title"]
        }
        movie_url = "https://api.themoviedb.org/3/search/movie"
        response = requests.get(url=movie_url, params=params, headers=header)
        movies = response.json()["results"]
        return render_template('select.html', movies=movies)
    return render_template('add.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)
