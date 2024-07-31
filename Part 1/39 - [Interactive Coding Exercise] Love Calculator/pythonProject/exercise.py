print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name_string = (name1 + name2).lower()
true_string = 'true'
love_string = 'love'

true_total = 0
love_total = 0


def countLetter(letter):
    return name_string.count(letter)


for letter in true_string:
    true_total += countLetter(letter)
for letter in love_string:
    love_total += countLetter(letter)

score = str(true_total) + str(love_total)

if int(score) < 10 or int(score) > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score) >= 40 and int(score) <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")