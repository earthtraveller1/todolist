import sqlite3
from typing import Tuple, Optional

from element import Element


def htmx_script() -> Element:
    source = "https://unpkg.com/htmx.org@1.9.4"
    return Element("script")\
        .property("src", source)


def tailwind_script() -> Element:
    source = "https://cdn.tailwindcss.com"
    return Element("script")\
        .property("src", source)


def head(title: str) -> Element:
    return\
        Element("head")\
        .add_child(
            Element("meta")
            .property("charset", "UTF-8")
        )\
        .add_child(
            Element("meta")
            .property("name", "viewport")
            .property(
                "content", "width=device-width, initial-scale=1.0"
            )
        )\
        .add_child(tailwind_script())\
        .add_child(htmx_script())\
        .add_child(
            Element("title")
            .inner_text(title)
        )


def todolist_container() -> Element:
    return\
        Element("div")\
        .styles(["w-80", "mx-auto", "my-16", "flex", "flex-col"])


def todolist_item(text: str, is_done: bool) -> Element:
    classes = ["rounded-lg", "text-lime-100", "mb-8", "p-4", "select-none"]
    if is_done:
        classes += ["line-through", "bg-lime-900",
                    "hover:bg-lime-700", "active:bg-lime-950"]
    else:
        classes += ["bg-indigo-900",
                    "hover:bg-indigo-700", "active:bg-indigo-950"]

    return\
        Element("div")\
        .styles(classes)\
        .inner_text(text)


def button(text: str = "Add Item") -> Element:
    return\
        Element("button")\
        .styles([
            "mx-auto",
            "bg-green-900",
            "rounded-md",
            "px-5",
            "py-2",
            "hover:bg-green-800",
            "active:bg-green-950"
        ])\
        .inner_text(text)


def create_item_form(button: Element) -> Element:
    return\
        Element("div")\
        .styles(["flex", "justify-item-center", "mx-2"])\
        .add_child(
            Element("input")
            .styles([
                "bg-slate-900",
                "mr-5",
                "ml-0",
                "border-b-2",
                "focus:border-red-100",
                "duration-300",
                "focus:outline-none",
                "border-violet-800"
            ])
            .property("type", "text")
            .flag("required")
            .property("minlength", "8")
            .property("name", "new-item-name")
        )\
        .add_child(button)


def todolist() -> Element:
    result = todolist_container()

    db_connection = sqlite3.connect("todolist.db")
    db_cursor = db_connection.cursor()

    items = db_cursor.execute("SELECT content, is_completed FROM items")

    item: Optional[Tuple[str, bool]]
    while (item := items.fetchone()) is not None:
        result.add_child(todolist_item(item[0], item[1]))

    result.add_child(
        button()
        .hx_get("/neng/newitemform")
        .hx_swap("outerHTML")
    )

    return result
