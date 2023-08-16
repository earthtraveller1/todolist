from flask import Flask
import markupsafe

from typing import Dict, List


def escape_string(input: str) -> str:
    output = ""
    for c in input:
        if c == "\"" or c == "'":
            output += "\\"
        output += c
    return output


class Element:
    def __init__(self, name: str = ""):
        self._name: str = name
        self._properties: Dict[str, str] = {}
        self._flags: List[str] = []
        self._inner_text: str = ""
        self._children: List['Element'] = []

    def property(self, prop_name: str, prop: str) -> 'Element':
        self._properties[prop_name] = escape_string(prop)
        return self

    def flag(self, flag: str) -> 'Element':
        self._flags.append(flag)
        return self

    def add_child(self, child: 'Element') -> 'Element':
        self._children.append(child)
        return self

    def inner_text(self, text: str) -> 'Element':
        self._inner_text = markupsafe.escape(text)
        return self

    def render(self) -> str:
        output = ""

        if self._name != "":
            output += f"<{self._name}"

            for prop_name, prop in self._properties.items():
                output += f" {prop_name}=\"{prop}\""

            for flag in self._flags:
                output += f" {flag}"

            output += ">"

        output += f"{self._inner_text}"

        for child in self._children:
            output += child.render()

        no_close_elements = ["", "br", "meta", "link", "img", "!DOCTYPE"]

        if self._name not in no_close_elements:
            output += f"</{self._name}>"

        return output


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
                    Element("title")
                    .inner_text("Hello World!")
                )
            )
            .add_child(
                Element("body")
                .add_child(
                    Element("h1")
                    .inner_text("Hello!")
                )
                .add_child(
                    Element("p")
                    .inner_text("This is a test!")
                )
            )
        )

    return output.render()
