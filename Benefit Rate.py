# Program to calculate your weekly benefit amount if applying to CT unemployment
input_string = input('Enter in your total quarterly wages.  Each quarterly wage should be followed by a space.\n')

user_list = input_string.split()

print('Wages:\n', user_list)

# convert each item to int type
for i in range(len(user_list)):
    user_list[i] = int(user_list[i])


user_list.sort()
average = (user_list[2] + user_list[3]) // 2
benefit_amount = average / 26

if benefit_amount >= 705:
    print("Your benefit amount is at the max of 705 dollars a week")
else:
    print("your weekly benefit amount is")
    print('{0:.2f}'.format(benefit_amount))