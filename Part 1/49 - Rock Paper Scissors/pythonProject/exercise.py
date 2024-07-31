import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
player_choice = int(input('0 for rock, 1 for paper, 2 for scissors: '))

enemy_choice = int(random.randrange(3))

def choice(number):
    if number == 0:
      return rock
    elif number == 1:
      return paper
    elif number == 2:
      return scissors
    else:
        print('invalid choice')

print(choice(player_choice))
print('Enemy Choice ')
print(choice(enemy_choice))
if int(player_choice) == int(enemy_choice):
    print('It was a tie!')
elif player_choice == 1 and enemy_choice == 0:
    print('You win!')
elif player_choice == 2 and enemy_choice == 1:
    print('You win!')
elif player_choice == 0 and enemy_choice == 2:
    print('You win!')
else:
    print('You lose!')
