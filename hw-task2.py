import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """
    Generate a sorted list of unique random numbers within specified range.
    
    Parameters:
    - min (int): The minimum possible number in the set (must be >= 1).
    - max (int): The maximum possible number in the set (must be <= 1000).
    - quantity (int): The number of values to pick.
    
    Returns:
    - list: A sorted list of unique random integers, or an empty list if parameters are invalid.
    """
    # Validate the input parameters:
    # 1. Check basic limits: 1 <= min <= max <= 1000
    # 2. Check quantity: must be at least 1, and cannot exceed the total count of numbers in the range (max - min + 1)
    if not (1 <= min <= max <= 1000) or not (1 <= quantity <= (max - min + 1)):
        return []
    
    # Generate a set of unique random numbers to avoid duplicates
    numbers_set = set()
    while len(numbers_set) < quantity:
        numbers_set.add(random.randint(min, max))
        
    # Convert the set to a sorted list and return it
    return sorted(list(numbers_set))


# ==========================================
# Testing block
# ==========================================
if __name__ == "__main__":
    # Test case 1: Standard valid lottery parameters (e.g., 2 numbers from 1 to 49)
    lottery_numbers = get_numbers_ticket(6, 49, 2)
    print("Your lottery numbers:", lottery_numbers)
    
    # Test case 2: Edge case with invalid parameters (quantity greater than the range)
    invalid_test = get_numbers_ticket(1, 5, 10)
    print("Invalid parameters test (should be empty):", invalid_test)
    
    # Test case 3: Another valid test (5 numbers from 1 to 36)
    another_draw = get_numbers_ticket(10, 20, 5)
    print("Another lottery draw:", another_draw)