from element import Element


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
        .add_child(
            Element("script")
            .property("src", "https://cdn.tailwindcss.com")
        )\
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
        )\
        .add_child(
            Element("title")
            .inner_text(title)
        )


def todolist_container() -> Element:
    return\
        Element("div")\
        .class_names("w-80 mx-auto my-16 flex flex-col")


def todolist_item(text: str, is_done: bool) -> Element:
    classes = "rounded-lg text-lime-100 mb-8 p-4 select-none"
    if is_done:
        classes += " line-through bg-lime-900 hover:bg-lime-700 active:bg-lime-950"
    else:
        classes += " bg-indigo-900 hover:bg-indigo-700 active:bg-indigo-950"

    return\
        Element("div")\
        .class_names(classes)\
        .inner_text(text)


def button(text: str = "Add Item") -> Element:
    return\
        Element("button")\
        .class_names("mx-auto bg-green-900 rounded-md px-5 py-2 hover:bg-green-800 active:bg-green-950")\
        .inner_text(text)
