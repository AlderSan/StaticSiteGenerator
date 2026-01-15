from textnode import TextNode, TextType

print("Hello world")

def main():
    test = TextNode("This is some anchor text", TextType("link") , "https://boot.dev")
    print(test)

if __name__ == "__main__":
    main()
