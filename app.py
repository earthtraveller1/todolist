from flask import Flask
from element import Element

app = Flask(__name__)


@app.route("/")
def index() -> str:
    output =\
        Element()\
        .add_child(Element("!DOCTYPE").flag("html"))\
        .add_child(
            Element("html")
            .add_child(
                Element("head")
                .add_child(
                    Element("meta")
                    .property("charset", "UTF-8")
                )
                .add_child(
                    Element("meta")
                    .property("name", "viewport")
                    .property(
                        "content", "width=device-width, initial-scale=1.0"
                    )
                )
                .add_child(
                    Element("script")
                    .property("src", "https://cdn.tailwindcss.com")
                )
                .add_child(
                    Element("script")
                    .property(
                        "src",
                        "https://unpkg.com/htmx.org@1.9.4"
                    )
                    .property(
                        "integrity",
                        "sha384-zUfuhFKKZCbHTY6aRR46gxiqszMk5tcHjsVFxnUo8VMus4kHGVdIYVbOYYNlKmHV"
                    )
                    .property(
                        "crossorigin",
                        "anyonymous"
                    )
                )
                .add_child(
                    Element("title")
                    .inner_text("Hello World!")
                )
            )
            .add_child(
                Element("body")
                .add_child(
                    Element("h1")
                    .inner_text("Hello!")
                    .class_names("font-sans text-center text-8xl my-8")
                )
                .add_child(
                    Element("p")
                    .inner_text("Click this!")
                    .hx_target("#test-target")
                    .hx_get("/neng")
                    .hx_trigger("click")
                    .class_names("font-sans text-base text-center")
                )
                .add_child(
                    Element("div")
                    .id("test-target")
                )
            )
        )

    return output.render()


@app.route("/neng")
def neng() -> str:
    result =\
        Element("p")\
        .class_names("font-sans text-base text-center text-red-600")\
        .id("test-target")\
        .hx_get("/neng/empty")\
        .inner_text("Neng Li is the President of China!")

    return result.render()


@app.route("/neng/empty")
def empty_div() -> str:
    result =\
        Element("div")\
        .id("test-target")

    return result.render()
