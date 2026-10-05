#A movie theater charges different ticket pricse depending on a person's age.
#If a person is under the age of 3, the ticket is free.
#If they are bewteen 3 and 12, the ticket is $10.
#If they are over the age of 12, the ticket is $15.
#Ask a family the age of each person who wants a ticket.
#Store the total cost of all the family's tickets and print it out.

ticket_cost = 0

while True: 
    age = input("Enter the age of the person or 'done' to finish: ")
    if age == 'done' or age == '':
        break
    age = int(age)
    if age < 3:
        print("This age is free.")
        continue
    elif age >=3 and age <= 12:
        print("This age costs $10.")
        ticket_cost =+ 10
    else:
        print("This age costs $15.")
        ticket_cost =+ 15

#Game example

#flag
winner = False

while not winner:
    position = input('enter the position between 1 to 9')