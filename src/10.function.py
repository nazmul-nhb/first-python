"""
10.Function
"""


def greet_user(name: str):
    """
    Greets the user with the provided name.
    """

    print(f"Hello, {name}!")


greet_user("NHB")


def get_greeting(name: str) -> str:
    """
    Returns a greeting message for the provided name.
    """

    return f"Hello, {name}!"


with open("greet.txt", "w+", encoding="utf-8") as file:
    MSG = get_greeting("NHB")
    file.write(MSG)
    file.seek(0)
    print(file.read().lower())
    print(MSG)
