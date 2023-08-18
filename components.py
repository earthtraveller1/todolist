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
