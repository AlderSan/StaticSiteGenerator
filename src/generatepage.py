import os
from markdowntohtml import markdown_to_html_node
from extractitle import extract_title


def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    cwd = os.getcwd()
    abs_from = os.path.join(cwd, from_path)
    abs_dest = os.path.join(cwd, dest_path)
    abs_template = os.path.join(cwd, template_path)
    markdown_content = ""
    template_content = ""
    title = ""
    with open(abs_from) as markdown_file:
        markdown_content = markdown_file.read()
    with open(abs_template) as template_file:
        template_content = template_file.read()

    converted_markdown_content = markdown_to_html_node(markdown_content)
    html_content = converted_markdown_content.to_html()
    title = extract_title(markdown_content)
    final_content = template_content.replace("{{ Title }}", title)
    final_content = final_content.replace("{{ Content }}", html_content)

    try:
        with open(abs_dest, "w") as f:
            f.write(final_content)
    except IOError as e:
        print(f"An error occured: {e}")

    return