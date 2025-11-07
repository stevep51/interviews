import json
from pathlib import Path

## Load the data from the JSONL file
DATA_PATH = Path(__file__).resolve().parent / "data.jsonl"
with DATA_PATH.open("r", encoding="utf-8") as data_file:
    DATA = [json.loads(line) for line in data_file if line.strip()]


def parse_jsonl(file_path):
    """
    Parse a JSONL file and return a list of dictionaries.
    
    Args:
        file_path: Path to the JSONL file
    
    Returns:
        List of dictionaries
    """
    pass


def find_highest_salary(data):
    """
    Find the person with the highest salary.
    
    Args:
        data: List of dictionaries with 'salary' and 'name' keys
    
    Returns:
        Dictionary with the person's information
    """
    pass


def count_by_city(data):
    """
    Count how many people are in each city.
    
    Args:
        data: List of dictionaries with 'city' key
    
    Returns:
        Dictionary mapping city names to counts
    """
    pass

