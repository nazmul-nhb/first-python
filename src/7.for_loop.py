"""
7.For_Loop
"""

for num in range(7):
    print(f"Hello {num+1}{(num+1)*"!"}")

# Same
for num in range(1, 7):
    print(f"Hello {num}{(num)*"!"}")

# Only the even numbers
for num in range(2, 9, 2):
    print(f"Hello {num}{(num)*"!"}")


SUCCESSFUL = False

for num in range(3):
    print(f"Attempt {num+1}")
    if SUCCESSFUL:
        print("Successful!")
        break
else:
    print("Failed after 3 attempts")


# Nested Loop
for i in range(4):
    for j in range(3):
        print(f"{i}:{j}")

print(type(range(4)))

# range() is returns an Iterable
