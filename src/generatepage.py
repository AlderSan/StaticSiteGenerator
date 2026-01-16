import os
from markdowntohtml import markdown_to_html_node
from extractitle import extract_title


def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    cwd = os.getcwd()
    abs_from = os.path.join(cwd, from_path)
    abs_dest = os.path.join(cwd, dest_path)
    abs_template = os.path.join(cwd, template_path)
    abs_from = from_path
    abs_dest = dest_path
    abs_template = template_path
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
    final_content = final_content.replace('href="/', f'href="{basepath}')
    final_content = final_content.replace('src="/', f'src="{basepath}')

    try:
        with open(abs_dest, "w") as f:
            f.write(final_content)
    except IOError as e:
        print(f"An error occured: {e}")

    return

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str, basepath:str) -> None:
    try:
        cwd = os.getcwd()
        abs_from = os.path.join(cwd, dir_path_content)
        abs_dest = os.path.join(cwd, dest_dir_path)
        abs_template = os.path.join(cwd, template_path)
        abs_from = dir_path_content
        abs_dest = dest_dir_path
        abs_template = template_path
        if not os.path.exists(abs_from):
            raise FileNotFoundError
        content_list = os.listdir(abs_from)
        file_list = []
        dir_list = []
        for content in content_list:
            content_path = os.path.join(abs_from, content)
            if os.path.isfile(content_path):
                file_list.append(content)
            else: 
                dir_list.append(content)
        for file in file_list:
            dest_file = os.path.join(dest_dir_path, file)
            dest_index = dest_file.rfind(".")
            corrected_dest_file = dest_file[:dest_index] + ".html"
            file_path = os.path.join(dir_path_content, file)
            generate_page(file_path, abs_template, corrected_dest_file, basepath)
        for dir in dir_list:
            new_src = os.path.join(abs_from, dir)
            new_dest = os.path.join(abs_dest, dir)
            if not os.path.exists(new_dest):
                os.mkdir(new_dest)
            generate_pages_recursive(new_src, template_path, new_dest, basepath)
    except FileNotFoundError:
        print("source directory does not exist")
    except Exception as e:
        print(f"An error has occured: {e}")
    return