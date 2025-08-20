"""
8.While_Loop
"""

NUMBER = 100

while NUMBER > 0:
    print(NUMBER)
    NUMBER //= 2


CMD = ""

while CMD.lower() != "exit":
    CMD = input("> 1.Type 'exit' to quit: ")
    print(f"> You entered: {CMD}")

# Or use Infinite Loop

while True:
    COMMAND = input("> 2.Type 'exit' to quit: ")
    print(f"> You entered: {COMMAND}")
    if COMMAND.lower() == "exit":
        break
