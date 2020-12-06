"""
context.py

To set the file path context to allow the files in this directory to access the files inside ../src
"""

import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import src