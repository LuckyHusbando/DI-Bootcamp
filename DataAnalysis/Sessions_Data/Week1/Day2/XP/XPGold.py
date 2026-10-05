#Exercise 2 XP Gold

print("Hello world" * 4 + "I love python" * 4)

try:
    month = int(input("Enter a month (1 to 12): "))

    # Determine and display the season
    if 3 <= month <= 5:
        print("Spring")
    elif 6 <= month <= 8:
        print("Summer")
    elif 9 <= month <= 11:
        print("Autumn")
    elif month == 12 or 1 <= month <= 2:
        print("Winter")
    else:
        print("Invalid month entered. Please enter a number between 1 and 12.")
except ValueError:
    print("Invalid input. Please enter a number.")