import unittest
from splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
    def test_code_split(self) -> None:
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)   
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT), 
                                     TextNode("code block", TextType.CODE), 
                                     TextNode(" word", TextType.TEXT),])
        
    def test_bold_split(self) -> None:
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)   
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT), 
                                     TextNode("bold", TextType.BOLD), 
                                     TextNode(" word", TextType.TEXT),])
        
    def test_italics_split(self) -> None:
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)   
        self.assertEqual(new_nodes, [TextNode("This is text with an ", TextType.TEXT), 
                                     TextNode("italic", TextType.ITALIC), 
                                     TextNode(" word", TextType.TEXT),])
        
    def test_no_split(self) -> None:
        node = TextNode("This is text with a word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)   
        self.assertEqual(new_nodes, [TextNode("This is text with a word", TextType.TEXT),])    

    def test_non_text(self) -> None:
        node = TextNode("This is text with a word", TextType.CODE)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)   
        self.assertEqual(new_nodes, [TextNode("This is text with a word", TextType.CODE),])   
    
    def test_multiple_code_split(self) -> None:
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode("This is text with `another code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2], "`", TextType.CODE)   
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT), 
                                     TextNode("code block", TextType.CODE), 
                                     TextNode(" word", TextType.TEXT),
                                     TextNode("This is text with ", TextType.TEXT), 
                                     TextNode("another code block", TextType.CODE), 
                                     TextNode(" word", TextType.TEXT),])
        
    def test_multiple_bold_split(self) -> None:
        node = TextNode("This is text **with** a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)   
        self.assertEqual(new_nodes, [TextNode("This is text ", TextType.TEXT), 
                                     TextNode("with", TextType.BOLD),
                                     TextNode(" a ", TextType.TEXT),
                                     TextNode("bold", TextType.BOLD), 
                                     TextNode(" word", TextType.TEXT),])
        

class TestSplitImages(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image of a cat](https://i.imgur.com/zjjcJKZ.png) and another ![image of a dog](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image of a cat", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "image of a dog", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

class TestSplitLinks(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with an [link to google](https://i.imgur.com/zjjcJKZ.png) and another [link to boot.dev](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link to google", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "link to boot.dev", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_split_no_links(self):
        node = TextNode(
            "This is text with an ![image of a cat](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ![image of a cat](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT),
            ],
            new_nodes,
        )

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self) -> None:
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes
        )        

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )