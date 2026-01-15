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
    

class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str , props: dict[str, str] | None = None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("leaf node has no value")
        if self.tag is None:
            return self.value
        else:
            open_tag = f'<{self.tag}{self.props_to_html()}>'
            close_tag = f'</{self.tag}>'
            return open_tag + self.value + close_tag
        
    def __repr__(self) -> str:
        results = {
            "tag": self.tag,
            "value": self.value,
            "props": self.props,
        }
        return str(results)    
    
class ParentNode(HTMLNode):
    def __init__(self, tag: str | None, children: list[HTMLNode] | None, props: dict[str, str] | None = None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        html_string = ''
        open_tag = f'<{self.tag}{self.props_to_html()}>'
        close_tag = f'</{self.tag}>'
        if self.tag is None:
            raise ValueError("parent node has no tag")
        if self.children is None:
            raise ValueError("Parent node has no children")
        else:
            for child in self.children:
                if child.value is None and type(child) == LeafNode:
                    raise ValueError(f'Child node {child} is missing a value')
                html_string += child.to_html()
        html_string = open_tag + html_string + close_tag
        return html_string
