#!/usr/bin/env python3
"""
Problem 2: Extract unique words from text and sort alphabetically.

Requirements:
- Read from a file (if filename provided) OR from stdin
- Output all unique words in alphabetical order (one per line)
- Words should be case-insensitive
"""

import sys
import re
from pathlib import Path
from typing import Set, List


def extract_words(text: str) -> Set[str]:
    """
    Extract unique words from text.
    
    TODO: Implement word extraction
    Hint: Use regex pattern r'\b[a-zA-Z]+\b' to find words
    Remember to convert to lowercase for case-insensitive comparison
    """
    pass  # Your code here


def process_file(filepath: Path) -> List[str]:
    """
    Read file and extract sorted unique words.
    
    TODO: 
    1. Read the file (handle errors)
    2. Extract unique words
    3. Return sorted list
    """
    pass  # Your code here


def process_stdin() -> List[str]:
    """
    Read from stdin and extract sorted unique words.
    
    TODO:
    1. Read from sys.stdin
    2. Extract unique words
    3. Return sorted list
    """
    pass  # Your code here


def main():
    """
    Main function to process input and output unique words.
    
    TODO:
    1. Check if command line argument provided (sys.argv)
    2. If yes, treat as filename and process file
    3. If no, read from stdin
    4. Output words one per line
    """
    pass  # Your code here


if __name__ == '__main__':
    main()