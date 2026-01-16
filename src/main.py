import os
import shutil
from textnode import TextNode, TextType
from htmlnode import LeafNode, HTMLNode
from copycontent import copy_content
from generatepage import generate_page


def main():
    copy_content("static", "public")
    generate_page("content/index.md", "template.html","public/index.html")


if __name__ == "__main__":
    main()
