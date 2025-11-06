import json


def parse_jsonl(file_path):
    """
    Parse a JSONL file and return a list of dictionaries.
    
    Args:
        file_path: Path to the JSONL file
    
    Returns:
        List of dictionaries
    """
    pass


def calculate_average_salary(data):
    """
    Calculate the average salary from the data.
    
    Args:
        data: List of dictionaries with 'salary' key
    
    Returns:
        Average salary as a float
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


def find_people_over_age(data, min_age):
    """
    Find all people older than the specified age.
    
    Args:
        data: List of dictionaries with 'age' key
        min_age: Minimum age (exclusive)
    
    Returns:
        List of dictionaries for people older than min_age
    """
    pass
