import os
import shutil
from textnode import TextNode, TextType
from htmlnode import LeafNode, HTMLNode
from copycontent import copy_content
from generatepage import generate_page, generate_pages_recursive


def main():
    copy_content("static", "public")
    generate_pages_recursive("content/", "template.html","public/")


if __name__ == "__main__":
    main()
