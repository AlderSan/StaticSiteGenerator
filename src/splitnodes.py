from textnode import TextNode, TextType
from markdownextract import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            try:
                delimiter_length = len(delimiter)
                start_index = node.text.index(delimiter)
                end_index = node.text.index(delimiter, start_index + delimiter_length) + delimiter_length

                before_split = TextNode(node.text[0:start_index], TextType.TEXT)
                split = TextNode(node.text[start_index:end_index].strip(delimiter), text_type)
                after_split = TextNode(node.text[end_index:], TextType.TEXT)

                if before_split.text != "":
                    new_nodes.append(before_split)

                new_nodes.append(split)

                if after_split.text != "":                           
                    if delimiter in after_split.text:
                        more_new_nodes = split_nodes_delimiter([after_split], delimiter, text_type)
                        new_nodes.extend(more_new_nodes)
                    else:
                        new_nodes.append(after_split)
            except ValueError:
                new_nodes.append(node)

    return new_nodes
        
def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        elif extract_markdown_images(node.text) == []:
            new_nodes.append(node)
        else:
            list_of_images = extract_markdown_images(node.text)
            remaining_text = node.text
            for i in range(0, len(list_of_images)):
                length = len(list_of_images[i][0]) + len(list_of_images[i][1]) + 5 #including ![]()
                start_index = remaining_text.index(list_of_images[i][0]) - 2 #including ![
                end_index = start_index + length

                pre_img_node = TextNode(remaining_text[:start_index], TextType.TEXT)
                img_node = TextNode(list_of_images[i][0], TextType.IMAGE, list_of_images[i][1])

                remaining_text = remaining_text[end_index:]

                new_nodes.extend([pre_img_node, img_node])
            if remaining_text != "":
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        elif extract_markdown_links(node.text) == []:
            new_nodes.append(node)
        else:
            list_of_links = extract_markdown_links(node.text)
            remaining_text = node.text
            for i in range(0, len(list_of_links)):
                length = len(list_of_links[i][0]) + len(list_of_links[i][1]) + 4 #including []()
                start_index = remaining_text.index(list_of_links[i][0]) - 1 #including [
                end_index = start_index + length

                pre_link_node = TextNode(remaining_text[:start_index], TextType.TEXT)
                link_node = TextNode(list_of_links[i][0], TextType.LINK, list_of_links[i][1])

                remaining_text = remaining_text[end_index:]
                
                new_nodes.extend([pre_link_node, link_node])
            if remaining_text != "":
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes


def text_to_textnodes(text: str) -> list[TextNode]:
    processed_text = [TextNode(text, TextType.TEXT)]
    processed_text = split_nodes_delimiter(processed_text, "**", TextType.BOLD)
    processed_text = split_nodes_delimiter(processed_text, "_", TextType.ITALIC)
    processed_text = split_nodes_delimiter(processed_text, "`", TextType.CODE)
    processed_text = split_nodes_image(processed_text)
    processed_text = split_nodes_link(processed_text)
    return processed_text