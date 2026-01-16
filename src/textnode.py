from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other) -> bool:
        return (
                self.text_type.value == other.text_type.value
            and self.text == other.text
            and self.url == other.url
        )
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case text_node.text_type.TEXT:
            return LeafNode(None, text_node.text)
        case text_node.text_type.BOLD:
            return LeafNode("b", text_node.text)
        case text_node.text_type.ITALIC:
            return LeafNode("i", text_node.text)
        case text_node.text_type.CODE:
            return LeafNode("code", text_node.text)
        case text_node.text_type.LINK:
            if text_node.url is not None:
                return LeafNode("a", text_node.text, {"href": text_node.url})  
            else:
                raise Exception("missing URL for link") 
        case text_node.text_type.IMAGE:
            if text_node.url is not None:
                return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text}) 
            else:
                raise Exception("missing URL for img")
        case _: 
            raise Exception("invalid text type")