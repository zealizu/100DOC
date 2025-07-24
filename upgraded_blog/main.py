from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, URL, InputRequired
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime
from flask_ckeditor.utils import cleanify
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap =Bootstrap5(app)
ckeditor = CKEditor(app)

class MakePost(FlaskForm):
    title = StringField(label="Blog Post Title", validators=[DataRequired()])
    subtitle = StringField(label="Subtitle", validators=[DataRequired()])
    name = StringField(label="Your Name", validators=[DataRequired()])
    blog_url = URLField(label="Blog Image URL", validators=[DataRequired(), URL()])
    blog_body = CKEditorField(label="Blog Content", validators=[DataRequired()])
    submit = SubmitField(label="Submit Post")
    

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    #Query the database for all the posts. Convert the data to a python list.
    posts = list(db.session.execute(db.select(BlogPost)).scalars())
    return render_template("index.html", all_posts=posts)

# Add a route so that you can click on individual posts.
@app.route('/post/<post_id>')
def show_post(post_id):
    # Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


#add_new_post() to create a new blog post
@app.route("/new-post", methods = ["POST", "GET"])
def make_post():
    form = MakePost()
    if form.validate_on_submit():
        now = datetime.now()
        formatted_date = now.strftime("%B %d, %Y")
        new_post = BlogPost(title=form.data["title"], subtitle=form.data["subtitle"], date=formatted_date, body=form.blog_body.data,author=form.data["name"],img_url=form.blog_url.data)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=form, page="New")

#edit_post() to change an existing blog post
@app.route("/edit-post/<post_id>", methods=["POST", "GET"])
def edit_post(post_id):
    blog = db.get_or_404(BlogPost, post_id)
    form = MakePost()
    if form.validate_on_submit():
        blog.title = form.title.data 
        blog.subtitle = form.subtitle.data 
        blog.body= form.blog_body.data 
        blog.author = form.name.data 
        blog.img_url = form.blog_url.data 
        db.session.commit()
        return redirect(url_for('show_post', post_id=post_id))
    form.title.data = blog.title
    form.subtitle.data = blog.subtitle
    form.blog_body.data = blog.body
    form.name.data = blog.author
    form.blog_url.data = blog.img_url
    return render_template("make-post.html", form=form, page="Edit")

    
#  delete_post() to remove a blog post from the database
@app.route("/delete/<post_id>")
def delete(post_id):
    post = db.get_or_404(BlogPost,post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
