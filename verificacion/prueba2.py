def greet(name: str) -> str:
    """Return a greeting message"""
    return f"Hello, {name}!"


def main():
    """Main function."""
    name = "World"  # Sin espacio alrededor del operador de asignación
    message = greet(name)
    print(message)  # Indentación incorrecta


if __name__ == "__main__":
    main()  # Todo en una sola línea
