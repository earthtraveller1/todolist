from flask import Flask
from element import Element
import components

app = Flask(__name__)


@app.route("/")
def index() -> str:
    output =\
        Element()\
        .add_child(
            Element(
                "!DOCTYPE"
            )
            .flag(
                "html"
            )
        )\
        .add_child(
            Element(
                "html"
            )
            .add_child(
                components.head(
                    "Hello World"
                )
            )
            .add_child(
                Element(
                    "body"
                )
                .class_names(
                    "bg-slate-900 text-slate-300"
                )
                .add_child(
                    Element(
                        "h1"
                    )
                    .inner_text(
                        "ToDo List"
                    )
                    .class_names(
                        "font-sans font-bold text-center text-8xl my-8"
                    )
                )
                .add_child(
                    Element(
                        "p"
                    )
                    .inner_text(
                        "Yes, a ToDo list. I know, right?"
                    )
                    .class_names(
                        "font-sans text-base text-center"
                    )
                )
                .add_child(
                    Element(
                        "div"
                    )
                    .id(
                        "test-target"
                    )
                )
                .add_child(
                    components.todolist_container()
                    .id(
                        "todolist-container"
                    )
                    .add_child(
                        components.todolist_item(
                            "Neng Li is the President of China",
                            False
                        )
                    )
                    .add_child(
                        components.todolist_item(
                            "Shiva is the King of the Universe!",
                            True
                        )
                    )
                    .add_child(
                        components.button()
                        .hx_get("/neng/newitemform")
                        .hx_swap("outerHTML")
                    )
                )
            )
        )

    return output.render()


@app.route("/neng/newitemform")
def new_item_form() -> str:
    result = components.create_item_form()
    return result.render()


@app.route("/neng/empty")
def empty_div() -> str:
    result =\
        Element("div")\
        .id("test-target")

    return result.render()
