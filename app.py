from flask import Flask, request
from element import Element, escape_string
import components

import sqlite3

database_connection = sqlite3.connect("todolist.db")
database_cursor = database_connection.cursor()

current_id: int = 0

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
                Element("body")
                .styles(["bg-slate-900", "text-slate-300"])
                .add_child(
                    Element("h1")
                    .inner_text("ToDo List")
                    .styles([
                        "font-sans",
                        "font-bold",
                        "text-center",
                        "text-8xl",
                        "my-8"
                    ])
                )
                .add_child(
                    Element(
                        "p"
                    )
                    .inner_text(
                        "Yes, a ToDo list. I know, right?"
                    )
                    .styles(
                        ["font-sans", "text-base", "text-center"]
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
                    .add_child(
                        components.todolist_item(
                            "Neng Li is the President of China",
                            False
                        )
                    )
                    .add_child(
                        components.todolist_item(
                            "Shiva is the King of the Universe!", True
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
    result = components\
        .create_item_form(
            components.button("Create")
            .hx_post("/shiva/additem")
            .hx_include("#new-item-form")
            .hx_swap("outerHTML")
            .hx_target("#new-item-form")
        )\
        .id("new-item-form")\

    return result.render()


@app.route("/shiva/additem", methods=["POST"])
def add_item() -> str:
    global current_id

    content = escape_string(request.form["new-item-name"])
    database_cursor.execute(
        f"INSERT INTO items VALUES (${current_id}, ${content}, true)"
    )
    current_id += 1

    return components.button()\
        .hx_get("/neng/newitemform")\
        .hx_swap("outerHTML")\
        .render()


@app.route("/neng/empty")
def empty_div() -> str:
    result =\
        Element("div")\
        .id("test-target")

    return result.render()
