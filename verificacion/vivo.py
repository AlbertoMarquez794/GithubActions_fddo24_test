def greet_user(name: str) -> str:
    """
    Return a greeting message for the user.

    Parameters:
        name (str): The name of the user.

    Returns:
        str: A greeting message.
    """
    if not name:
        raise ValueError("The name cannot be empty")
    return f"Hello, {name}!"


def calculate_sum(numbers: list[int]) -> int:
    """
    Calculate the sum of a list of integers.

    Parameters:
        numbers (list[int]): A list of integers.

    Returns:
        int: The sum of the numbers in the list.
    """
    if not numbers:
        raise ValueError("The list cannot be empty")
    return sum(numbers)


def main() -> None:
    """
    Main function to run the script.
    """
    user_name = "Alice"
    numbers = [1, 2, 3, 4, 5]

    greeting = greet_user(user_name)
    total = calculate_sum(numbers)

    print(greeting)
    print(f"The sum of the numbers is: {total}")
