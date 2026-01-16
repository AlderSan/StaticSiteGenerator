from textnode import TextNode, TextType
from htmlnode import LeafNode, HTMLNode

print("Hello world")

def main():
    test = TextNode("This is some anchor text", TextType("link") , "https://boot.dev")
    print(test)

def copy_content(source_directory: str, destination_directory: str) -> None:
    return

if __name__ == "__main__":
    main()
