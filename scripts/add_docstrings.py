#!/usr/bin/env python3

import os
import re
from pathlib import Path

def add_module_level_docstring(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    if not content.strip():
        return
    if content.startswith('"' '"') or content.startswith("'''"):
        return
    new_content = """
    {module_name}
    {file_path}
    {date}
    {author}
    {description}
    """.format(
        module_name=os.path.basename(file_path).replace('.py', ''),
        file_path=file_path,
        date=os.date('%Y-%m-%d'),
        author='Your Name',
        description='Module level docstring for {}'.format(os.path.basename(file_path))
    ) + content
    with open(file_path, 'w') as file:
        file.write(new_content)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('Usage: python3 add_docstrings.py <file_path>')
        sys.exit(1)
    add_module_level_docstring(Path(sys.argv[1]))