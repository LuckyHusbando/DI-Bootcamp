#Solve The Matrix

# Step 1: Transforming the String into a 2D List
MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''

# Clean up the string and split into rows
rows_str = MATRIX_STR.strip().splitlines()

# Determine the number of rows and columns for a rectangular grid
num_rows = len(rows_str)
num_cols = max(len(row) for row in rows_str)

# Create the 2D list (matrix) by padding shorter rows with spaces
matrix = [list(row.ljust(num_cols)) for row in rows_str]

# --- Processing the Matrix ---

# Step 2: Processing Columns
# Step 3: Filtering Alpha Characters
# Step 4: Replacing Symbols with Spaces

decoded_message = ""
is_last_char_alpha = False

# Iterate through columns, then rows
for col_idx in range(num_cols):
    for row_idx in range(num_rows):
        # Access the character at the current grid position
        char = matrix[row_idx][col_idx]
        
        # Check if the character is an alphabet letter
        if char.isalpha():
            decoded_message += char
            is_last_char_alpha = True
        else:
            # If the last character was an alphabet, and the current is not,
            # it indicates a transition that should be a space.
            if is_last_char_alpha:
                decoded_message += ' '
            is_last_char_alpha = False

# Step 5: Constructing the Secret Message
# The final decoded_message might have a trailing space, so we strip it.
decoded_message = decoded_message.strip()

# Print the decoded message
print(decoded_message)