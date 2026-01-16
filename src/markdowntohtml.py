from htmlnode import HTMLNode, ParentNode, LeafNode
from markdowntoblocks import markdown_to_blocks, block_to_block_type, BlockType
from splitnodes import text_to_textnodes
from textnode import TextNode, text_node_to_html_node, TextType


def text_to_children(text: str) -> list[HTMLNode]:
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes

def list_text_to_children(text: str) -> list[HTMLNode]:
    unordered = text.strip().startswith("-")
    split = ""
    children_list = []
    split = text.split("\n")
    if unordered:
        for line in split:
            children_list.append(ParentNode("li",text_to_children(line[2:])))
    else:
        for i in range(1, len(split) + 1):
            line = split[i-1].replace(f"{i}. ", "")
            children_list.append(ParentNode("li",text_to_children(line)))
    return children_list

def markdown_to_html_node(markdown:str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            p_text = block.replace("\n", " ")
            html_nodes.append(ParentNode("p", text_to_children(p_text), ))
        if block_type == BlockType.CODE:
            code_text = block.strip("```").lstrip("\n").rstrip("\n")
            code_text = r"{}".format(code_text)
            html_nodes.append(ParentNode("pre", [text_node_to_html_node(TextNode(code_text, TextType.CODE))]))
        if block_type == BlockType.QUOTE:
            quote_text = block.replace(">", "").strip()
            quote_text = quote_text.replace("\n", "")
            html_nodes.append(ParentNode("blockquote", text_to_children(quote_text), ))
        if block_type == BlockType.UNORDERED_LIST:
            html_nodes.append(ParentNode("ul", list_text_to_children(block)))
        if block_type == BlockType.ORDERED_LIST:
            html_nodes.append(ParentNode("ol", list_text_to_children(block)))
        if block_type == BlockType.HEADING:
            h = block.count("#", 0, 5)
            heading_text = block.lstrip("#").lstrip()
            html_nodes.append(ParentNode(f"h{h}", text_to_children(heading_text), ))
    parent = ParentNode("div", html_nodes)
    return parent



