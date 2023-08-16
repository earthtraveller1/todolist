from typing import Dict, List


class Element:
    def __init__(self, name: str):
        self.name: str = name
        self.properties: Dict[str, str] = {}
        self.children: List['Element'] = []

    def property(self, prop_name: str, prop: str) -> 'Element':
        self.properties[prop_name] = prop
        return self

    def add_child(self, child: 'Element') -> 'Element':
        self.children.append(child)
        return self

    def render(self) -> str:
        output = f"<{self.name}"

        for prop_name, prop in self.properties:
            output += f" {prop_name}=\"{prop}\""

        output += ">"

        if len(self.children) != 0:
            for child in self.children:
                output += child.render()

            output += f"</{self.name}>"

        return output
