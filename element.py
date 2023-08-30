from typing import Dict, List
import markupsafe


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

    def styles(self, classes: List[str]) -> 'Element':
        self.property("class", " ".join(classes))
        return self

    def id(self, id: str) -> 'Element':
        self.property("id", id)
        return self

    def hx_get(self, url: str) -> 'Element':
        self.property("hx-get", url)
        return self

    def hx_post(self, url: str) -> 'Element':
        self.property("hx-post", url)
        return self

    def hx_put(self, url: str) -> 'Element':
        self.property("hx-put", url)
        return self

    def hx_delete(self, url: str) -> 'Element':
        self.property("hx-delete", url)
        return self

    def hx_patch(self, url: str) -> 'Element':
        self.property("hx-patch", url)
        return self

    def hx_trigger(self, trigger: str) -> 'Element':
        self.property("hx-trigger", trigger)
        return self

    def hx_target(self, target: str) -> 'Element':
        self.property("hx-target", target)
        return self

    def hx_swap(self, swap: str) -> 'Element':
        self.property("hx-swap", swap)
        return self

    def hx_include(self, selector: str) -> 'Element':
        self.property("hx-include", selector)
        return self

    def add_child(self, child: 'Element') -> 'Element':
        self._children.append(child)
        return self

    def inner_text(self, text: str) -> 'Element':
        self._inner_text = markupsafe.escape(text)
        return self

    def raw_inner_text(self, text: str) -> 'Element':
        self._inner_text = text
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
