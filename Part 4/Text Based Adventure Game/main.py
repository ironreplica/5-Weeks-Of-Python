# Text adventure game
# Trevor childs 7/30/2024

print("""
      
   _____       .___                    __                         ________                          __   
  /  _  \    __| _/__  __ ____   _____/  |_ __ _________   ____   \_____  \  __ __   ____   _______/  |_ 
 /  /_\  \  / __ |\  \/ // __ \ /    \   __\  |  \_  __ \_/ __ \   /  / \  \|  |  \_/ __ \ /  ___/\   __|
/    |    \/ /_/ | \   /\  ___/|   |  \  | |  |  /|  | \/\  ___/  /   \_/.  \  |  /\  ___/ \___ \  |  |  
\____|__  /\____ |  \_/  \___  >___|  /__| |____/ |__|    \___  > \_____\ \_/____/  \___  >____  > |__|  
        \/      \/           \/     \/                        \/         \__>           \/     \/        

""")

health = 100

def portal():
    print('Purchase the adventure quest DLC to discover what happens next...')
def takeDmg(dmg):
    health - dmg
    if health > 100:
        print(f'You took {dmg}. Try to avoid doing what you just did.')
    else:
        print('\nThanks for playing, you somehow just got yourself killed.')

quest = input("\nYou find yourself in a dusty attic filled with ancient artifacts. A strange glow emanates from a small wooden chest in the corner. What do you do? (1: Run away, 2: Take it, 3: Scream) ")

if quest == '1':
    # Run
    quest = input('\nYou run away like a coward, but on your way out of the attic, you fall through a magical portal! What will you do? 1: Go through it, 2: Run, 3: Throw a rock at it.' )
    if quest == '1':
        # Go through portal
        portal()
    elif quest == '2':
        # Run 
        print('\nThis game is not for cowards. Thanks for playing. ')
    elif quest == '3':
        # Throw a rock
        print('\nYou toss a rock into the portal, but it shoots right back and hits you right in the head! ')
        quest = input("\nWhat will you do now? 1: Throw another rock, 2: Go through the portal and stop being a coward. ")
        if quest == '1':
            print('\nIt came back and hit you really hard. You just got yourself killed, thanks for playing I guess.')
        elif quest == '2':
            portal()
elif quest == '2':
    print('The object BLOWS UP IN YOUR HANDS! Game over.')
    pass
elif quest == '3':
    print('You scream for help but nobody hears you. You are a coward. Thank you for playing coward. ')
    # scream
    pass
