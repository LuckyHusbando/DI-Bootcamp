#W2D2DC-Gold

import re

MATRIX_STR = """
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%"""

# ==========================================
# Step 1: Transforming the String into a 2D List
# ==========================================
# Split by newline and remove any empty padding lines
lines = [line for line in MATRIX_STR.split("\n") if line]

# Convert each line into a list of individual characters
matrix = [list(line) for line in lines]


# ==========================================
# Step 2: Processing Columns
# ==========================================
num_rows = len(matrix)
num_cols = len(matrix[0]) if num_rows > 0 else 0

raw_column_string = ""

# Loop through columns first, then rows (top-to-bottom, left-to-right)
for col in range(num_cols):
    for row in range(num_rows):
        raw_column_string += matrix[row][col]


# ==========================================
# Steps 3 & 4: Filtering Alpha Characters & Replacing Symbols
# ==========================================
decoded_message = ""
i = 0

while i < len(raw_column_string):
    # Step 3: Check if it's an alphabet letter using .isalpha()
    if raw_column_string[i].isalpha():
        decoded_message += raw_column_string[i]
        i += 1
    else:
        # Step 4: We hit a non-alpha character (or group of them)
        start = i
        while i < len(raw_column_string) and not raw_column_string[i].isalpha():
            i += 1
        end = i

        # Check if this group of symbols is strictly BETWEEN two alpha characters
        has_alpha_before = any(c.isalpha() for c in raw_column_string[:start])
        has_alpha_after = any(c.isalpha() for c in raw_column_string[end:])

        if has_alpha_before and has_alpha_after:
            # Replace the entire group of symbols with a single space
            decoded_message += " "
        else:
            # If they are at the very beginning or end, keep them as they are
            decoded_message += raw_column_string[start:end]


# ==========================================
# Step 5: Constructing and Printing the Secret Message
# ==========================================
print(decoded_message)