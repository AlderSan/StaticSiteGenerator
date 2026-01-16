from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

headings = ("# ", "## ", "### ", "#### ", "##### ", "###### ")

def markdown_to_blocks(markdown: str) -> list[str]:
    blocks_list = markdown.split("\n\n")
    cleaned_block_list = []
    for block in blocks_list:
        cleaned_block = block.strip().lstrip("\n").rstrip("\n")
        if cleaned_block != "":
            cleaned_block_list.append(cleaned_block)
    return cleaned_block_list

def block_to_block_type(markdown_block: str) -> BlockType:
    block_type = BlockType.PARAGRAPH
    if markdown_block.startswith(headings):
        block_type = BlockType.HEADING
    if markdown_block.startswith("```\n") and markdown_block.endswith("```"):
        block_type = BlockType.CODE
    block_lines = markdown_block.split("\n")
    if len(block_lines) == len(list(filter(lambda l: l.strip("\n").startswith(">"), block_lines))):
        block_type = BlockType.QUOTE
    if len(block_lines) == len(list(filter(lambda l: l.startswith("- "), block_lines))):
        block_type = BlockType.UNORDERED_LIST

    def ordered_helper(list_of_lines: list[str]) -> bool:
        for i in range(len(block_lines)):
            if not block_lines[i].startswith(f"{i+1}. "):
                return False
        return True
    if ordered_helper(block_lines):
        block_type = BlockType.ORDERED_LIST
    return block_type
                    
     