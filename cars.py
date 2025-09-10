#!/usr/bin/env python3
"""
Problem 3: Analyze car data using Pandas.

Tasks:
1. Create data/output directory
2. Read cars.csv and save descriptive statistics
3. Filter for specific Audi models
4. Group by manufacturer/class and analyze highway MPG
"""

import pandas as pd
from pathlib import Path
import logging


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s,p%(process)s,{%(filename)s:%(lineno)d},%(levelname)s,%(message)s",
)
logger = logging.getLogger(__name__)


def create_output_directory() -> Path:
    """
    Task 1: Create output directory if it doesn't exist.
    
    TODO: Create 'data/output' directory
    Hint: Use Path.mkdir(parents=True, exist_ok=True)
    """
    pass  # Your code here


def read_and_describe_data(input_path: Path, output_dir: Path) -> pd.DataFrame:
    """
    Task 2: Read dataset and save descriptive statistics.
    
    TODO:
    1. Read the CSV file using pd.read_csv()
    2. Print first 5 rows using .head()
    3. Get descriptive statistics using .describe()
    4. Save statistics to 'descriptive.csv'
    """
    pass  # Your code here


def filter_audi_data(df: pd.DataFrame, output_dir: Path) -> pd.DataFrame:
    """
    Task 3: Filter for specific Audi models.
    
    TODO: Filter where:
    - manufacturer == 'audi'
    - model == 'a4'  
    - cyl == 4
    Save to 'audi.csv' (remember index=False)
    
    Hint: You can use .query() method or boolean indexing
    """
    pass  # Your code here


def analyze_highway_mpg(df: pd.DataFrame, output_dir: Path) -> pd.DataFrame:
    """
    Task 4: Group data and calculate average highway MPG.
    
    TODO:
    1. Group by ['manufacturer', 'class']
    2. Calculate mean of 'hwy' column
    3. Reset index to convert MultiIndex to regular columns
    4. Sort by 'hwy' in descending order
    5. Save to 'hwy.csv'
    """
    pass  # Your code here


def main():
    """Main function to run all tasks."""
    # Define paths
    input_path = Path("data") / "raw" / "cars.csv"
    
    # Check if input file exists
    if not input_path.exists():
        logger.error(f"Input file not found: {input_path}")
        return
    
    # TODO: Call all task functions in order
    # Remember to store return values and pass them to next functions
    

if __name__ == '__main__':
    main()