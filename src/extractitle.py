




def extract_title(markdown: str) -> str:
    marker = "# "
    index = markdown.find(marker)
    end_index = markdown.find("\n\n", index) + 1
    if end_index <= 0:
        end_index = len(markdown)
    title = markdown[index:end_index]
    clean_title = title.replace("#", " ").strip()
    if clean_title == "":
        raise Exception("no title found")
    return clean_title