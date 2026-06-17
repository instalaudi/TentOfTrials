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
    if content.startswith('