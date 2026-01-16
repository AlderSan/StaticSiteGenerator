import os
import shutil
from textnode import TextNode, TextType
from htmlnode import LeafNode, HTMLNode


print("Hello world")

def main():
    test = TextNode("This is some anchor text", TextType("link") , "https://boot.dev")
    print(test)
    copy_content("static", "public")

def copy_content(source_directory: str, destination_directory: str) -> None:
    try:
        cwd = os.getcwd()
        abs_source = os.path.join(cwd, source_directory)
        abs_dest = os.path.join(cwd, destination_directory)
        if not os.path.exists(abs_source):
            raise FileNotFoundError
        if os.path.exists(abs_dest):
            shutil.rmtree(abs_dest)
        os.mkdir(abs_dest)
        content_list = os.listdir(abs_source)
        file_list = []
        dir_list = []
        
        for content in content_list:
            content_path = os.path.join(abs_source, content)
            if os.path.isfile(content_path):
                file_list.append(content_path)
            else: 
                dir_list.append(content)
        for file in file_list:
            shutil.copy(file, abs_dest)
        for dir in dir_list:
            new_src = os.path.join(abs_source, dir)
            new_dest = os.path.join(abs_dest, dir)
            copy_content(new_src, new_dest)
    except FileNotFoundError:
        print("source directory does not exist")
    except:
        print("copy content failed")
    return

if __name__ == "__main__":
    main()
