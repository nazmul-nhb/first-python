"""
6.Logical_Operators
"""

HIGH_INCOME = True
POLITICAL_LEADER = False
GOOD_CREDIT = True

if HIGH_INCOME and GOOD_CREDIT:
    print("Eligible for loan!")
else:
    print("Not eligible for loan!")


if HIGH_INCOME or POLITICAL_LEADER:
    print("Eligible for loan!")


if not POLITICAL_LEADER:
    print("You should fucking get out of Banguland!")
