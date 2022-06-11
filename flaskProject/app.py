# importing Flask and other modules
from flask import Flask, request, render_template

# Flask constructor
app = Flask(__name__)


# @app.route('/', methods=["GET"])
# def hello_world():
#     return "Hello, world!"


# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods=["GET", "POST"])
def get_form():
    if request.method == "POST":
        # getting input with link = linkname in HTML form
        link = request.form.get("link_name")
        return "Your link is : " + link

    return render_template("index.html")


if __name__ == '__main__':
    app.run()
