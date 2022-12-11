name = input("Enter your name: ")
amount_correct = 0
question2 = "What word becomes shorter when you add two letters to it"
print("Hello " + name + " Lets play a riddle game! \n""Do you want to play?""\ntype yes or no")

answer = input()
if answer.lower() == "yes":
    print("First question. \n" "The more I dry the wetter I get.  What am I?")
else:
    print("Have a great day then!")
    exit()
answer1 = input()
if answer1.lower() == "towel":
    print("Correct!")
    print("Second question.\n" + question2 + " ")
    amount_correct += 1
else:
    print("Good try!\n" + question2 + " ")
    print()
answer2 = input()
if answer2.lower() == "short":
    print("Correct!")
    amount_correct += 1
else:
    print("Good try!")

print("The amount you got correct is: " + str(amount_correct))
