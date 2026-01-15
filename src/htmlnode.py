from typing import Any




class HTMLNode():
    def __init__(self, tag: str | None = None, value: str | None = None, children: list["HTMLNode"] | None = None, props: dict[str, str] | None = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> Any:
        raise NotImplementedError("not implemented")
    
    def props_to_html(self) -> str:
        results = ""
        if self.props is not None:
            for key in self.props.keys():
                results = f'{results} {key}="{self.props[key]}"'
        return results

    def __repr__(self) -> str:
        results = {
            "tag": self.tag,
            "value": self.value,
            "children": self.children,
            "props": self.props,
        }
        return str(results)