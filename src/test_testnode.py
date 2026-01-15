import unittest

from textnode import TextNode,TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self) -> None:
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_params(self) -> None:
        node = TextNode("This is a text node", TextType.ITALIC, "https://localhost:8080")
        self.assertEqual(node.text, "This is a text node")
        self.assertEqual(node.text_type.value, "italic")
        self.assertEqual(node.url, "https://localhost:8080")

    def test_url_not_eq(self) -> None:
        node = TextNode("This is a text node", TextType.ITALIC, "https://localhost:8080")
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_text_not_eq(self) -> None:
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a test node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_type_not_eq(self) -> None:
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()