"""
9.Loop_Test
"""

# Even Numbers 1-20

COUNT1 = 0

# For Loop
for num in range(1, 21):
    if num % 2 == 0:
        COUNT1 += 1
print(f"We have {COUNT1} even numbers")

# or
COUNT2 = 0

for num in range(0, 21, 2):
    if num != 0:
        COUNT2 += 1
print(f"We have {COUNT2} even numbers")

# while
NUM = 0
COUNT3 = 0

while NUM <= 20:
    if NUM % 2 == 0 and NUM > 1:
        COUNT3 += 1
    NUM += 1
print(f"We have {COUNT3} even numbers")

# or

NUMBER = 0
COUNT4 = 0

while NUMBER <= 20:
    if NUMBER > 1:
        COUNT4 += 1
    NUMBER += 2
print(f"We have {COUNT4} even numbers")

# Infinite Loop
NUM_W = 0
COUNT5 = 0

while True:
    NUM_W += 1
    if NUM_W > 20:
        break
    if NUM_W % 2 == 0 and NUM_W > 1:
        COUNT5 += 1
print(f"We have {COUNT5} even numbers")
