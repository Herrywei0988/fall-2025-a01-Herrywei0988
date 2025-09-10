#!/usr/bin/env python3
"""
Problem 3: Analyze car data using Pandas.

Tasks:
1. Create data/output directory
2. Read cars.csv and save descriptive statistics
3. Filter for specific Audi models
4. Group by manufacturer/class and analyze highway MPG
"""


from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

import pandas as pd


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
    out_dir = Path("data") / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    logger.info(f"output directory ready at: {out_dir}")
    return out_dir


def read_and_describe_data(input_path: Path, output_dir: Path) -> pd.DataFrame:
    """
    Task 2: Read dataset and save descriptive statistics.
    
    TODO:
    1. Read the CSV file using pd.read_csv()
    2. Print first 5 rows using .head()
    3. Get descriptive statistics using .describe()
    4. Save statistics to 'descriptive.csv'
    """
    try:
        df = pd.read_csv(input_path)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Input file not found: {input_path}") from e

    # Show first 5 rows to stdout
    print(df.head())

    desc = df.select_dtypes(include="number").describe()
    desc_path = output_dir / "descriptive.csv"
    desc.to_csv(desc_path)
    logger.info(f"saved descriptive statistics to: {desc_path}")
    return df


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
    filt = (df["manufacturer"] == "audi") & (df["model"] == "a4") & (df["cyl"] == 4)
    audi = df.loc[filt].copy()
    out_path = output_dir / "audi.csv"
    audi.to_csv(out_path, index=False)
    logger.info(f"saved filtered Audi data to: {out_path} (rows={len(audi)})")
    return audi


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
    grouped = (
        df.groupby(["class", "manufacturer"])["hwy"]
        .mean()
        .reset_index()
        .sort_values(by="hwy", ascending=False)
    )
    out_path = output_dir / "hwy.csv"
    grouped.to_csv(out_path, index=False)
    logger.info(f"saved grouped hwy means to: {out_path} (rows={len(grouped)})")
    return grouped


def main():
    """Main function to run all tasks."""
    # Define paths
    input_path = Path("data") / "raw" / "cars.csv"
    
    # Check if input file exists
    if not input_path.exists():
        logger.error(f"Input file not found: {input_path}")
        return
    
    out_dir = create_output_directory()
    df = read_and_describe_data(input_path, out_dir)
    filter_audi_data(df, out_dir)
    analyze_highway_mpg(df, out_dir)
    

if __name__ == '__main__':
    main()