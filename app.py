from flask import Flask
import html

app = Flask(__name__)


@app.route("/")
def index() -> str:
    output = html.Element("html")\
        .add_child(html.Element("h1") .inner_text("Hello!"))\
        .add_child(html.Element("p").inner_text("This is a test!"))

    return output.render()
