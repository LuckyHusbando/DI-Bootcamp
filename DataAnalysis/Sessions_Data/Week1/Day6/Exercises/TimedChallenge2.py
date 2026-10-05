#Timed Challenge 2

x = int(input('Enter the Number:')) #write down your logic here

# A perfect number is a positive integer that is equal to the sum of its proper divisors. This logic is for positive integers only.

sum_of_divisors = 0

# Loop from 1 up to the number itself (exclusive) to find all proper divisors
for i in range(1, x):
    # Check if 'i' is a divisor of 'x'
    if x % i == 0:
        sum_of_divisors += i

# Check if the sum of divisors is equal to the original number
# The output is a boolean (True or False) based on this comparison
print(sum_of_divisors == x)