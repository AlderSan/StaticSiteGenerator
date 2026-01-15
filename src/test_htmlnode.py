import unittest
from htmlnode import HTMLNode



class TestTextNode(unittest.TestCase):
    def test_params(self) -> None:
        node = HTMLNode("p", "This is a Paragraph", [], {"Color": "Red"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is a Paragraph")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"Color": "Red"})

    def test_none(self) -> None:
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_multiple_children(self) -> None:
        node = HTMLNode("p", "This is a Paragraph", [], {"Color": "Red"})
        node2 = HTMLNode("p", "This is a Paragraph", [], {"Color": "Blue"})
        node3 = HTMLNode("p", "This is a Paragraph", [node, node2], {"Color": "Yellow"})
        self.assertEqual(node3.children, [node, node2])

    def test_multiple_props(self) -> None:
        node = HTMLNode("p", "This is a Paragraph", [], {"Color": "Red"})
        node2 = HTMLNode("p", "This is a Paragraph", [], {"Color": "Blue"})
        node3 = HTMLNode("p", "This is a Paragraph", [node, node2], {"Color": "Yellow", "Size": "16", "href": "https://google.com"})
        self.assertEqual(node3.props, {"Color": "Yellow", "Size": "16", "href": "https://google.com"})
        self.assertEqual(node3.props_to_html(), ' Color="Yellow" Size="16" href="https://google.com"')


if __name__ == "__main__":
    unittest.main()