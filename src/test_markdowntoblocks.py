import unittest
from markdowntoblocks import markdown_to_blocks, block_to_block_type, BlockType


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


class TestBlockToBlockTypes(unittest.TestCase):
    def test_heading_block(self) -> None:
        text = "## HEADING 1"
        text2 = "##### HEADING 2"
        test1 = block_to_block_type(text)
        test2 = block_to_block_type(text2)
        self.assertEqual(BlockType.HEADING, test1)
        self.assertEqual(BlockType.HEADING, test2)

    def test_code_block(self) -> None:
        text = """```
This is a line of code.
This is another line of code.
Beep boop.
```"""
        text2 = """```
Here are a few more lines of code.
Beep boop.
```"""
        test1 = block_to_block_type(text)
        test2 = block_to_block_type(text2)
        self.assertEqual(BlockType.CODE, test1)
        self.assertEqual(BlockType.CODE, test2)

    def test_quote_block(self) -> None:
        text = """> This is a quote
> There are several lines to this quote
> This line is included as well"""
        text2 = "> This is just a one-line quote."
        test1 = block_to_block_type(text)
        test2 = block_to_block_type(text2)
        self.assertEqual(BlockType.QUOTE, test1)
        self.assertEqual(BlockType.QUOTE, test2)

    def test_unordered_list_block(self) -> None:
        text = """- unordered list testing
- this is another item
- third item
- 4th item on the list"""
        text2 = "- list with just one item"
        test1 = block_to_block_type(text)
        test2 = block_to_block_type(text2)
        self.assertEqual(BlockType.UNORDERED_LIST, test1)
        self.assertEqual(BlockType.UNORDERED_LIST, test2)

    def test_ordered_list(self) -> None:
        text = """1. ordered list testing
2. this is another item
3. third item
4. 4th item on the list"""
        text2 = "1. lonely ordered list item"
        test1 = block_to_block_type(text)
        test2 = block_to_block_type(text2)
        self.assertEqual(BlockType.ORDERED_LIST, test1)
        self.assertEqual(BlockType.ORDERED_LIST, test2)

    def test_paragraph_block(self) -> None:
        text = "paragraph 1"
        text2 = """This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items"""
        test1 = block_to_block_type(text)
        test2 = block_to_block_type(text2)
        self.assertEqual(BlockType.PARAGRAPH, test1)
        self.assertEqual(BlockType.PARAGRAPH, test2)