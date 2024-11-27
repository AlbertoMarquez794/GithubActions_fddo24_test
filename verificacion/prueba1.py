def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"


def main():
    """Main function to execute the greeting."""
    name = "World"
    message = greet(name)
    print(message)


if __name__ == "__main__":
    main()
