import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode



class TestHTMLNode(unittest.TestCase):
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

class TestLeafNode(unittest.TestCase):
    def test_params(self) -> None:
        node = LeafNode("p", "This is a Paragraph", {"Color": "Red"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is a Paragraph")
        self.assertEqual(node.props, {"Color": "Red"})

    def test_no_tag_to_html(self) -> None:
        node = LeafNode(None, "Hello")
        self.assertEqual(node.to_html(), "Hello")

    def test_to_html(self) -> None:
        node = LeafNode("p", "This is a Paragraph")
        self.assertEqual(node.to_html(), '<p>This is a Paragraph</p>')

    def test_to_html_with_props(self) -> None:
        node = LeafNode("p", "This is a Paragraph", {"Color": "Yellow", "Size": "16", "href": "https://google.com"})
        self.assertEqual(node.to_html(), '<p Color="Yellow" Size="16" href="https://google.com">This is a Paragraph</p>')

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):  
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


if __name__ == "__main__":
    unittest.main()