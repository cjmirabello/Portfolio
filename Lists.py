groceries = ["apples", "bananas", "lemons"]
groceries_cost = []
groceries.append("grapes")
budget = float(5)
print("Welcome to the Python Supermarket.  You have a total of 5 dollars to spend.")
print(groceries)

while True:
    grab_item = input("Choose one grocery item.\n")
    if grab_item in groceries:
        groceries.remove(grab_item)
        break
    else:
        print("Choose a valid item")
        continue
while True:
    price = eval(input("What is the price of your chosen item in dollars and cents?\n"))
    new_budget = budget - price
    if new_budget <= 0:
        print("You are out of money")
        quit()
    if type(price) == float:
        print("what item will you take next?")
        print(groceries)
        break
    else:
        print("Please choose a dollar amount and the amount of cents")
        continue

print("The amount of money you have left is")
print('{0:.2f}'.format(new_budget))

while True:
    grab_item2 = input("Choose another grocery item.\n")
    if grab_item2 in groceries:
        groceries.remove(grab_item2)
        break
    else:
        print("Choose a valid item")
        continue
while True:
    price = eval(input("What is the price of your chosen item in dollars and cents?\n"))
    new_budget2 = new_budget - price
    if new_budget2 <= 0:
        print("You are out of money")
        quit()
    if type(price) == float or type(price) != int:
        print("Thanks for shopping with us!")
        print(groceries)
        break
    else:
        print("Please choose a dollar amount and the amount of cents")
        continue
print("The amount of money you have left is")
print('{0:.2f}'.format(new_budget))
