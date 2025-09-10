#!/usr/bin/env python3
"""
Problem 1: Find the missing number in a sequence.

Requirements:
- Takes two command line arguments: --n (integer) and --num-list (string)
- Finds the missing integer from a sequence [1..n]
- Handles errors appropriately
"""

from __future__ import annotations

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
    parser.add_argument("--n", type=int, required=True, help="Upper bound n (>0)")
    parser.add_argument(
        "--num-list",
        type=str,
        required=True,
        help='Whitespace-separated list of n-1 integers, e.g. "5 2 3 1"',
    )
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
    if n is None or n <= 0:
        raise ValueError("--n must be a positive integer (> 0)")

    # parse numbers
    try:
        numbers = [int(tok) for tok in num_list.split()]
    except ValueError as e:
        raise ValueError("Invalid value in --num-list: all items must be integers") from e

    # count check
    if len(numbers) != n - 1:
        raise ValueError(
            f"--num-list must contain exactly {n-1} numbers, got {len(numbers)}"
        )

    # duplicates
    if len(set(numbers)) != len(numbers):
        raise ValueError("--num-list contains duplicate values")

    # range check
    if not all(1 <= x <= n for x in numbers):
        raise ValueError(f"All numbers must be within [1..{n}]")

    return numbers


def find_missing(n: int, numbers: List[int]) -> int:
    """
    Find the missing number.
    
    TODO: Implement the algorithm to find the missing number.
    Hint: Consider using set operations for efficiency.
    """
    expected = set(range(1, n + 1))
    actual = set(numbers)
    missing = expected - actual
    if len(missing) != 1:
        raise ValueError("Invalid input: expected exactly one missing value")
    return next(iter(missing))


def main(args=None):
    """Main function."""
    try:
        config = parse_args(args)
        numbers = validate_input(config.n, config.num_list)
        missing = find_missing(config.n, numbers)
        logger.info(f"missing element is {missing}")
        
    except ValueError as e:
        logger.error(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
