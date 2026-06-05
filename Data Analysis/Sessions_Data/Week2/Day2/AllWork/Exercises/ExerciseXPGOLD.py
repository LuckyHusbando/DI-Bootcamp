#Exercise XP Gold - Week 2 - Day 2

# Hard-coded current date
CURRENT_YEAR = 2025
CURRENT_MONTH = 8
CURRENT_DAY = 3

def get_age(birth_year, birth_month, birth_day):
    """
    Calculates the age of a person based on their date of birth.
    Returns the age as an integer.
    """
    age = CURRENT_YEAR - birth_year
    
    # Adjust age if the birthday hasn't occurred yet this year
    if birth_month > CURRENT_MONTH:
        age -= 1
    elif birth_month == CURRENT_MONTH and birth_day > CURRENT_DAY:
        age -= 1
        
    return age

def can_retire(gender, date_of_birth):
    """
    Determines if a person can retire based on their gender and date of birth.
    Returns True if they can retire, False otherwise.
    """
    # Parse the date of birth string
    try:
        birth_year_str, birth_month_str, birth_day_str = date_of_birth.split('/')
        birth_year = int(birth_year_str)
        birth_month = int(birth_month_str)
        birth_day = int(birth_day_str)
    except (ValueError, IndexError):
        print("Invalid date format. Please use 'yyyy/mm/dd'.")
        return False
        
    # Get the person's age
    age = get_age(birth_year, birth_month, birth_day)
    
    # Define retirement ages
    retirement_age_men = 67
    retirement_age_women = 62
    
    # Check if the person can retire based on gender and age
    if gender.lower() == 'm':
        return age >= retirement_age_men
    elif gender.lower() == 'f':
        # Assuming women were born after April, 1947
        return age >= retirement_age_women
    else:
        print("Invalid gender. Please use 'm' or 'f'.")
        return False

# --- Main program flow ---

# Ask for user input
user_gender = input("Enter your gender (m/f): ")
user_dob = input("Enter your date of birth (yyyy/mm/dd): ")

# Call can_retire to get the result
is_eligible = can_retire(user_gender, user_dob)

# Display a message to the user
if is_eligible:
    print("Congratulations! You are eligible to retire.")
else:
    print("Sorry, you are not yet eligible to retire.")

# --- Test cases (uncomment to test) ---
# print("\n--- Test Cases ---")
#
# # Test case 1: A man who is 68 years old (eligible)
# print(f"Man, 1957/01/01 can retire: {can_retire('m', '1957/01/01')}")
# # Test case 2: A man who is 66 years old (not eligible)
# print(f"Man, 1959/01/01 can retire: {can_retire('m', '1959/01/01')}")
#
# # Test case 3: A woman who is 63 years old (eligible)
# print(f"Woman, 1962/01/01 can retire: {can_retire('f', '1962/01/01')}")
# # Test case 4: A woman who is 61 years old (not eligible)
# print(f"Woman, 1964/01/01 can retire: {can_retire('f', '1964/01/01')}")
#
# # Test case 5: A woman who is turning 62 later this year (not eligible yet)
# print(f"Woman, 1963/12/31 can retire: {can_retire('f', '1963/12/31')}")
#
# # Test case 6: A woman who just turned 62 (eligible)
# print(f"Woman, 1963/01/01 can retire: {can_retire('f', '1963/01/01')}")