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


# encoding is used as "keyword argument"
with open("greet.txt", "w+", encoding="utf-8") as file:
    MSG = get_greeting("NHB")
    file.write(MSG)
    file.seek(0)
    print(file.read().lower())
    print(MSG)


# pass variable number of arguments
def multiply_nums(*num: int) -> int:
    """
    Multiplies all the provided numbers and returns the result.
    * num: Variable number of integer arguments.
    """
    result = 1
    for n in num:
        result *= n
    return result


print(multiply_nums(1, 2, 3, 4, 5))


# variable number of keyword arguments
def save_user(**user: str):
    """
    Saves user information provided as keyword arguments.
    ** user: Variable number of keyword arguments representing user information.
    """
    print(user)


save_user(name="NHB", age="30", city="Sirajganj")
