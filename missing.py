#!/usr/bin/env python3
"""
Problem 1: Find the missing number in a sequence.

Requirements:
- Takes two command line arguments: --n (integer) and --num-list (string)
- Finds the missing integer from a sequence [1..n]
- Handles errors appropriately
"""

import argparse
import logging
import sys
from typing import List


# Configure logging with the required format
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s,p%(process)s,{%(filename)s:%(lineno)d},%(levelname)s,%(message)s",
)
logger = logging.getLogger(__name__)


def parse_args(args=None):
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Find the missing number in a sequence from 1 to n"
    )
    
    # TODO: Add the required arguments
    # Hint: You need --n (integer) and --num-list (string)
    
    return parser.parse_args(args)


def validate_input(n: int, num_list: str) -> List[int]:
    """
    Validate the input arguments.
    
    TODO: Implement validation checks:
    - n must be positive (> 0)
    - Parse num_list into integers
    - Check for correct count (should be n-1 numbers)
    - Check for duplicates
    - Check all numbers are in range [1..n]
    
    Raise ValueError with descriptive message if validation fails.
    """
    pass  # Your code here


def find_missing(n: int, numbers: List[int]) -> int:
    """
    Find the missing number.
    
    TODO: Implement the algorithm to find the missing number.
    Hint: Consider using set operations for efficiency.
    """
    pass  # Your code here


def main(args=None):
    """Main function."""
    try:
        config = parse_args(args)
        
        # TODO: Complete the main logic:
        # 1. Validate input
        # 2. Find missing number
        # 3. Log the result using logger.info()
        
    except ValueError as e:
        logger.error(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
