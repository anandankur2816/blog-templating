from flask import Flask, render_template
from post import Post
import requests

posts = requests.get("https://api.npoint.io/ed99320662742443cc5b").json()
# post_objects = []
# for post in posts:
#     post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
#     post_objects.append(post_obj)

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)