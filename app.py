import sqlite3
import time

from flask import Flask, request

import components
from element import Element

app = Flask(__name__)


@app.route("/")
def index() -> str:
    output =\
        Element()\
        .add_child(
            Element("!DOCTYPE")
            .flag("html")
        )\
        .add_child(
            Element("html")
            .add_child(
                components.head("Hello World")
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
                    Element("p")
                    .inner_text("Yes, a ToDo list. I know, right?")
                    .styles(["font-sans", "text-base", "text-center"])
                )
                .add_child(
                    Element("div")
                    .id("test-target")
                )
                .add_child(components.todolist().id("todolist"))
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
            .hx_target("#todolist")
        )\
        .id("new-item-form")\

    return result.render()


@app.route("/shiva/additem", methods=["POST"])
def add_item() -> str:
    database_connection = sqlite3.connect("todolist.db")
    database_cursor = database_connection.cursor()

    id = int(time.time_ns() / 1000)

    content = request.form["new-item-name"]
    database_cursor.execute(
        "INSERT INTO items VALUES (?, ?, false);", (id, content))
    database_connection.commit()

    return components.todolist().id("todolist").render()


@app.route("/shiva/items/<item_id>", methods=["DELETE"])
def remove_item(item_id: str) -> str:
    database_connection = sqlite3.connect("todolist.db")
    database_cursor = database_connection.cursor()
    database_cursor.execute("DELETE FROM items WHERE id=?", (item_id,))
    database_connection.commit()

    return components.todolist().id("todolist").render()


@app.route("/neng/empty")
def empty_div() -> str:
    result =\
        Element("div")\
        .id("test-target")

    return result.render()


def init():
    db_connection = sqlite3.connect("todolist.db")
    db_cursor = db_connection.cursor()

    table_schema = "(id BIGINT, content VARCHAR(1028), is_completed BOOL)"
    db_cursor.execute(
        f"CREATE TABLE IF NOT EXISTS items {table_schema}"
    )

    db_connection.commit()


init()
