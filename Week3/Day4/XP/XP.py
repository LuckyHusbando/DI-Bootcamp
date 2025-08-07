#Exercises - Week 3/Day 4

#Exercise 1 - Currencies

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __repr__(self):
        return f'{self.amount} {self.currency}s'
    
    def __int__(self):
        return self.amount
    
    def __add__(self, other):
        if isinstance(other, int):
            return Currency(self.currency, self.amount + other)
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f'Cannot add between Currency type <{self.currency}> and <{other.currency}>')
            self.amount += other.amount
            return self
        else:
            return NotImplemented

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

#Expected Outputs below:

print(c1)
# '5 dollars'

print(int(c1))
# 5

print(repr(c1))
# '5 dollars'

print(c1 + 5)
# 10

print(c1 + c2)
# 15

print(c1) 
# 5 dollars

c1 += 5
print(c1)
# 10 dollars

c1 += c2
print(c1)
# 20 dollars

# print(c1 + c3)
# TypeError: Cannot add between Currency type <dollar> and <shekel>

try:
    c1 + c3
except TypeError as e:
    print(e)

#Exercise 2: Import

from func import sum_and_print
sum_and_print(10, 25)

#Exercise 3: String Module

import string
import random

all_letters = string.ascii_letters

random_string = ''
for _ in range(5):
    random_char = random.choice(all_letters)
    random_string += random_char

print(random_string)

#Exercise 4: Current Date

import datetime
current_date = datetime.date.today()
print(current_date)

#Exercise 5: Amount of Time Left Until January 1st

import datetime
now = datetime.datetime.now()
print(now)

Jan1 = datetime.datetime(2026, 1, 1)
print (Jan1)

time_difference = Jan1 - now
print(time_difference)

#Exercise 6: Birthday And Minutes

from datetime import datetime

def minutes_lived(birthdate_str):
    try:
        birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')

        now = datetime.now()
        time_difference = now - birthdate
        minutes = time_difference.total_seconds() / 60

        print(f"You have lived for approximately {int(minutes):,} minutes.")
    except ValueError:
        print("Invalid date format. Please use 'YYYY-MM-D'.")

(minutes_lived('1990-01-01'))

#Exercise 7: The Faker Module

from faker import Faker
fake = Faker()

Users = []

def add_users(num_users):
    for _ in range(num_users):
        User = {
            'name': fake.name(),
            'address': fake.address(),
            'language_code': fake.language_code()
        }
        Users.append(User)

add_users(3)
print(Users)