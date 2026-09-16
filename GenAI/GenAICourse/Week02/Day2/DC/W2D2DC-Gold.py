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
lines = [line for line in MATRIX_STR.split("\n") if line]
matrix = [list(line) for line in lines]


# ==========================================
# Step 2: Processing Columns
# [Feedback #1 & #4] Handles varying row lengths & improves string performance
# ==========================================
num_rows = len(matrix)
# Find max length to safely handle rows of varying lengths
max_cols = max((len(row) for row in matrix), default=0)

raw_chars = []

# Loop column-by-column
for col in range(max_cols):
    for row in matrix:
        # Check boundary to avoid IndexError on shorter rows
        if col < len(row):
            raw_chars.append(row[col])

# Use join() instead of repeated += inside loops for O(N) performance
raw_column_string = "".join(raw_chars)


# ==========================================
# Steps 3 & 4: Filtering & Decoding
# [Feedback #2 & #3] Uses Regex lookarounds to simplify logic and preserve edges
# ==========================================
# Lookbehind (?<=\w) ensures an alphanumeric character precedes the group.
# Lookahead (?=\w) ensures an alphanumeric character follows the group.
# Non-alphanumeric groups NOT between two alphanumeric characters (leading/trailing) are ignored.
decoded_message = re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', raw_column_string)


# ==========================================
# Step 5: Output
# ==========================================
print(decoded_message)