import unittest
from extractitle import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_1(self) -> None:
        title = extract_title("# Hello")
        self.assertEqual("Hello", title)

    def text_extract_2(self) -> None:
        title = extract_title("""# Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.""")
        self.assertEqual("Tolkien Fan CLub", title)