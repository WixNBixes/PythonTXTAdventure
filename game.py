#Dictionaries
Female = ['female', 'F', 'f', 'girl', 'Girl', 'woman', 'Woman', 'w','W','G','g','GIRL','FEMALE','WOMAN']
Male = ['male','M','m','boy','Boy','B','b','man','Man','MAN','BOY']
Yes = ['y', 'Yes', 'Y', 'yes', 'yeah', 'yus','yea','ye','YES']
No = ['no','N','n','No','NO']
Tavern = ['Tavern','TAVERN', 'tavern','Pub','pub','bar','Bar','BAR','PUB']
College = ['COLLEGE','College','college']
Shop = ['shop','SHOP','Shop']

#Character creation
_PlayerName = input("Please enter your character\'s name:  ")

print("Human 1\nElf 2\nDwarf 3\nOrc 4")

_PlayerRace = 0

while _PlayerRace == 0 or _PlayerRace > 4:
    try:
        _PlayerRace = int(input("Please choose your race:  "));
        if _PlayerRace > 4:
                print("Invalid selection, please try again.")
        else:
                continue
    except ValueError:
        print("Sorry! Words aren\'t welcome here, please enter a number.")
    else:
        print()

if _PlayerRace == 1:
    print("You have chosen to be human! \nWelcome", _PlayerName, " the human, to the town of Duncan\'s Rest!")
elif _PlayerRace == 2:
    print("You have chosen to be an elf! \nWelcome", _PlayerName, " the elf, to Evergreen Forest!")
elif _PlayerRace == 3:
    print("You have chosen to be a dwarf! \nWelcome", _PlayerName, " the dwarf, to the caves of Brightspark!")
else:
    print("You have chosen to be an orc! \nWelcome", _PlayerName, " the orc, to the halls of Windhawk!")

_PlayerSex = 0

_PlayerInventory = []
_PlayerMoney = 50
_Shopping = False

while _PlayerSex == 0:
    _PlayerSex = str(input("Please choose your sex:  "))
    if _PlayerSex in Female:
        print("You have chosen female")
        continue
    elif _PlayerSex in Male:
        print("You have chosen male")
        continue
    else:
        print("Please choose male or female, I didn't have time to code all non binary extensions.")
        _PlayerSex = 0

#Human campaign

_PlayerChoice = False

if _PlayerRace == 1:
    print("You have spent all your life within the walls of Duncan\'s Rest and have grown tired of the day to day"
    + " boredom of being in a small rural town. You decide that with the savings you've managed to save up"
    + " you will leave the only home you've ever known to seek your fortune elsewhere. You have ", _PlayerMoney, "gold"
    + " currently and can spend it at the tavern, the college or the shop.")
    _ChoiceDR = input("Where will you go?  ")
    
    while _PlayerChoice is False:
        if _ChoiceDR in Tavern:
            print("You decide to go to the tavern")
            break
        elif _ChoiceDR in College:
            print("You decide to go to the college")
            break
        elif _ChoiceDR in Shop:
            print("You decide to go to the shop")
            break
        else:
            print("You look far and wide for such a place, but Duncan's Rest is only a small town with very limited"
              + " access to such things.")
            _ChoiceDR = input("Please try again: ")

#To the tavern!
if _ChoiceDR in Tavern and _PlayerSex in Male:
     print("The local tavern is one you\'ve frequented plenty of times over the years with your friends. It's a small"
           + " establishment but is filled with plenty of men and women that you've known throughout the course of your"
           + " life. As you enter, the barman smiles widely:\n")
_DrinkDR = input("Your usual, I presume? ")
if _DrinkDR in Yes:
        print("The barman begins to pour your favourite drink into a tankard, speaking as it fills and froths\n")
        _Barman = input('"How\'s your father, lad? Doing well, I hope?"')
        if _Barman in Yes:
                  print('"Good to hear, lad!" He replies. "That\'ll be two gold."')
        elif _Barman in No:
                  print('His smile drops. "He\'s caught the fever, then? Tis a shame, lad... You have my condolences."'
                        + ' He pushes the pint to you, when you go to pay, he waves his hand. "You and your father were'
                        + ' fine regulars. Never got into fights or broke my windows. Have it on me."')
                  
       
else:
        print('"Ah, not in the mood for drinking, eh? Can\'t say I blame you, especially when there are men like him"'
              + '" reminding us why it\'s a sin." He points out a strange drunkard at the end of the bar, mumbling into'
              + " his drink. He looks like he went through hell and back, with all the scars to prove his tale.")
        _ApproachCrazy = input("You don\'t know if you should approach him while he\'s so preoccupied. Will you? ")
        
            
#To the shop!


