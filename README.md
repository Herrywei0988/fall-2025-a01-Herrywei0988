# Problem Set - Python & Pandas Skills

You will be performing several Python exercises in this assignment to build and/or reinforce skills that will be used later in the semester.

You will be doing all the exercises on your laptop with your preferred Python setup. We recommend you use an IDE like VSCode or Jupyter Lab so you can develop iteratively and interactively.

## Setting Up Your Environment with uv

This project uses `uv` for fast, reliable Python package management. Follow these steps to get started:

### Installing uv

Install uv using the official installer (works on macOS and Linux):

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# After installation, you may need to restart your terminal or run:
source $HOME/.cargo/env
```

### Setting Up the Project

Once uv is installed, setting up the project is simple:

```bash
# Clone the repository
git clone <repository-url>
cd assignment-python-skills

# Run scripts directly - uv handles dependencies automatically
uv run python missing.py --n 5 --num-list "1 2 3 5"
uv run python words.py filename.txt
uv run python cars.py
```

**That's it!** uv automatically:
- Creates and manages virtual environments
- Installs project dependencies from `pyproject.toml`
- Runs your scripts in the correct environment

No need to manually create virtual environments or install dependencies.

## Requirements:

* Problems 1-2 use **core** Python libraries only (including `re`, `os`, `argparse`, `sys`, `pathlib`, `typing`, etc.)  
* Problem 3 uses Pandas for data analysis
* Python 3.9 or higher is required
* All dependencies are managed through `pyproject.toml`

## Coding Guidelines

This assignment follows modern Python best practices. You should adhere to these guidelines in your code:

### 1. Type Hints
Use type hints for all function parameters and return values:
```python
def find_missing(n: int, numbers: List[int]) -> int:
    """Find the missing number in a sequence."""
    pass
```

### 2. Logging Format
Use the standardized logging configuration:
```python
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s,p%(process)s,{%(filename)s:%(lineno)d},%(levelname)s,%(message)s",
)
```

### 3. Modern Python Features
- Use f-strings for string formatting: `f"Missing element is {value}"`
- Use pathlib for file operations: `Path("data") / "output" / "file.csv"`
- Use context managers for file operations: `with open(file, 'r') as f:`

### 4. Code Organization
- Keep functions focused and modular (30-50 lines max)
- Separate validation logic from business logic
- Use descriptive variable and function names

### 5. Error Handling
- Provide clear, actionable error messages
- Use specific exception types (ValueError, FileNotFoundError, etc.)
- Exit gracefully with appropriate error codes

### 6. Documentation
- Add docstrings to all functions
- Include brief comments for complex logic
- Document expected inputs and outputs

## Submission

You will follow the submission process for all labs and assignments:

1. Add all your requested files to the GitHub assignment repo for the appropriate deliverable.
2. Submit a final commit message called "final-submission" to your repo. This is critical so that instructional team can evaluate your work. **Do not change your GitHub repo after submitting the "final-submission" commit message**

Make sure you commit **only the files requested**.

The files to be committed and pushed to your repository for this assignment are:

* `missing.py`
* `words.py`
* `cars.py`
* `gutenberg-top50.txt`
* `data/output/audi.csv`
* `data/output/descriptive.csv`
* `data/output/hwy.csv`
* `pyproject.toml` (already provided)

## Instructions

1. Clone this repository
2. Change your current working directory into the repository
3. Set up your environment with uv (see setup instructions above)
4. Complete the skeleton code in `missing.py`, `words.py`, and `cars.py`
5. Test your solutions against the examples provided
6. Remember, all files must be within the repository directory otherwise git will not see them
7. Commit and push your work regularly

## Problem 1 (30 points)

**Point Breakdown:**
- Correct argument parsing with argparse: 10 points
- Input validation (all error conditions): 10 points
- Correct algorithm to find missing number: 10 points

Use the `missing.py` file provided in this repo and update it into a script that does the following:

1. Takes two command line arguments `--n` (integer) and `--num-list` (string). The `--n` argument specifies a positive integer greater than zero and the `--num-list` argument is a string containing a random list of `n-1` integers from the set `[1..n]` with one integer missing. You will need to use the `argparse` package for this, the [`Argparse Tutorial`](https://docs.python.org/3/howto/argparse.html) will provide you everything you need to know about `argparse` for this assignment. Here are a few examples of sample outputs.

    ```
    uv run python missing.py --n 5
    usage: missing.py [-h] --n N --num-list NUM_LIST
    missing.py: error: the following arguments are required: --num-list
    ```

    ```
    uv run python missing.py --n 5 --num-list "5 2 3 1" 
    2025-08-24 08:35:15.855,p12345,{missing.py:73},INFO,missing element is 4
    ```

1. Finds the missing integer and print it as an output.

1. Prints an error message and exits in any of the following conditions:
  - Either of the `--n` or `--num-list` arguments are missing or have an incorrect data type.
  - A non-integer value is provided in the first or as part of the second argument.
  - The number of items provided in the `--num-list` argument does not match `n-1`.
  - There are duplicate values provided in the `--num-list` argument.

## Problem 2 (30 points)

**Point Breakdown:**
- Reading from file OR stdin correctly: 10 points
- Proper word extraction (regex, case-insensitive): 10 points
- Correct alphabetical sorting and output: 10 points

Write a program `words.py` that reads **either** a text file **or** text from [`stdin`](https://en.wikipedia.org/wiki/Standard_streams) and writes to [`stdout`](https://en.wikipedia.org/wiki/Standard_streams) all the unique words in the input in alphabetical order (one per line.)

The program should be setup in such a way that if the program gets a command line argument, it expects it to be a file name, and if not it reads `stdin`.

You can use the following command to make sure it works right: `$ cat filename | uv run python words.py`. This should produce the same result as `$ uv run python words.py filename`.

The `filename` file to be used for this problem is on the internet at this location:

`http://www.gutenberg.org/files/11/11-0.txt`

**You need to download the file into your repository directory, but you must not commit it.**

Output the top fifty lines from the script into a text file called `gutenberg-top50.txt`. You can accomplish this task by running a command like `$ uv run python words.py filename | head -n 50 > gutenberg-top50.txt`

## Problem 3 (40 points)

**Point Breakdown:**
- Task 1 - Directory creation: 10 points
- Task 2 - Read data and save descriptive statistics: 10 points
- Task 3 - Filter Audi data correctly: 10 points
- Task 4 - Group by and sort highway MPG: 10 points

There are 4 tasks in this problem, each worth 10 points. The `pandas` package is already included in the project dependencies and will be installed when you set up with uv. The output of each of these tasks is to be saved in a file as per the instructions provided with each task.

Run the cars.py script to complete all tasks:

```bash
uv run python cars.py
```

1. [Task 1 - Create a new directory to store output files](#task-1---create-a-new-directory-to-store-output-files)
1. [Task 2 - Read the dataset and print basic information](#task-2---read-the-dataset-and-print-basic-information)
1. [Task 3 - Filter out information matching a criteria](#task-3---filter-out-information-matching-a-criteria)
1. [Task 4 - Group the data and find a summary statistic](#task-4---group-the-data-and-find-a-summary-statistic)

### Task 1 - Create a new directory to store output files (10 points)

The tasks in this assignment will be generating output files and we would like to save them in a separate directory structure.

1. Create a new directory [`data/output`](data/output). All the output files will be stored in this directory. This directory will be checked in as part of your assignment submission.

### Task 2 - Read the dataset and print basic information (10 points)

1. Read the [`cars.csv`](data/raw/cars.csv) available in the [`data/raw`](data/raw) directory into a pandas dataframe using [`read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) and print out the first 5 rows of the dataframe.

1. Print descriptive statistics for all the numerical columns in the dataframe. Use the [`describe`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html) function for doing this. Save the statistics in a new file called `descriptive.csv` in the `data/output` directory using the [`to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html) function.

### Task 3 - Filter out information matching a criteria (10 points)

1. Filter the cars dataframe to create a new dataframe that only contains rows matching the following criteria: `manufacturer` is `audi` and `model` is `a4` and `cyl==4`. You can use [this tutorial](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html) for reference.

1. Save the filtered dataframe into a new file called `audi.csv` in the `data/output` directory.

### Task 4 - Group the data and find a summary statistic (10 points)

1. For each `class` for each `manufacturer` find out the average value of `hwy` miles. You can use the [`GroupBy.mean`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.GroupBy.mean.html) to do this.

1. Sort the output by `hwy` in ***descending*** order. You might have to use the [`reset_index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html) and [`sort_values`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html) functions to do this.

1. Save the resulting dataframe into a new file called `hwy.csv` in the `data/output` directory.

## Grading Rubric

**Total Points: 100** (see point breakdown in each problem above)

Points will be deducted for:

### Code Quality & Requirements
* Code does not follow the specified coding guidelines
* Missing or inadequate error handling
* Incorrect algorithm implementation
* Code does not produce expected outputs

### Submission Requirements  
* Missing required files or incorrect file names
* Files committed that were not requested
* Repository structure altered from original
* Final commit not labeled "final-submission"

### Code Organization
* Functions longer than 50 lines
* Missing docstrings on functions
* Hard-coded file paths (use relative paths)
* Poor variable/function naming
