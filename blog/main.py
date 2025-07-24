from flask import Flask, render_template
import requests 


app = Flask(__name__)
blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
blog_posts = response.json()

@app.route('/')
def home():
    return render_template("index.html", blog_posts=blog_posts)

@app.route("/post/<id>")
def post(id):
    return render_template("post.html", id=int(id), blog_posts=blog_posts)

if __name__ == "__main__":
    app.run(debug=True)

