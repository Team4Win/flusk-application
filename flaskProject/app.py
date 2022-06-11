# importing Flask and other modules
from flask import Flask, request, render_template
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


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
        # making requests instance
        reqs = requests.get(link)

        # using the BeautifulSoup module
        soup = BeautifulSoup(reqs.text, 'html.parser')

        # displaying the title
        print("Title of the website is : ")
        for title in soup.find_all('h1'):
          print(title.get_text())
        lista = []
        for data in soup.find_all('p'):
            lista.append(data.get_text())
        response = title.get_text() + '\n'
        response += "\n".join(lista)
        return response
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
