from flask import Flask

from typing import Dict, List


class Element:
    def __init__(self, name: str):
        self._name: str = name
        self._properties: Dict[str, str] = {}
        self._inner_text: str = ""
        self._children: List['Element'] = []

    def property(self, prop_name: str, prop: str) -> 'Element':
        self._properties[prop_name] = prop
        return self

    def add_child(self, child: 'Element') -> 'Element':
        self._children.append(child)
        return self

    def inner_text(self, text: str) -> 'Element':
        self._inner_text = text
        return self

    def render(self) -> str:
        output = f"<{self._name}"

        for prop_name, prop in self._properties:
            output += f" {prop_name}=\"{prop}\""

        output += f">{self.inner_text}"

        if len(self._children) != 0:
            for child in self._children:
                output += child.render()

            output += f"</{self._name}>"

        return output


app = Flask(__name__)


@app.route("/")
def index() -> str:
    output = Element("html")\
        .add_child(Element("h1") .inner_text("Hello!"))\
        .add_child(Element("p").inner_text("This is a test!"))

    return output.render()
