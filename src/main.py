from copycontent import copy_content
from generatepage import generate_pages_recursive
import sys
import os


def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    copy_content("static", "docs")
    generate_pages_recursive("content/", "template.html", "docs/", basepath)


if __name__ == "__main__":
    main()
