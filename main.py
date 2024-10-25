bill = float(input("Welcome to the tip calculator!\nWhat was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
cost_per_person = (bill * (1 + tip/100) / people)


print("Each person should pay {:.2f}".format(cost_per_person))