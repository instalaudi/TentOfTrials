#!/usr/bin/env python3

import os
import re
from pathlib import Path
from datetime import datetime

def add_module_level_docstring(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    if not content.strip():
        return
    if content.startswith('"' '"') or content.startswith("'''"):
        return
    new_content = f'"""
This module contains utility functions for adding docstrings to Python files.
Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""
{content}
    with open(file_path, 'w') as file:
        file.write(new_content)

if __name__ == '__main__':
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.py') and not file.startswith('__init__.py'):
                add_module_level_docstring(os.path.join(root, file))