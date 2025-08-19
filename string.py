"""
Python Practice: String
"""

FIRST = "Nazmul"
LAST = "Hassan"

FULL = FIRST + " " + LAST

FULL_FMT = f"{FIRST} {LAST}"

print(FULL, "Length:", len(FULL))

print(FULL_FMT.upper())
print(FULL_FMT.title())
print(FULL_FMT.lower())
print(FULL_FMT.capitalize())

print('    kid   '.strip())

print(FULL_FMT.find("Hassan"))

print(FULL_FMT.replace("ss", "zz"))

print('ss' in FULL_FMT)

print(FULL_FMT.startswith("N"))
print(FULL_FMT.startswith("H"))
