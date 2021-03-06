#Dictionaries
Female = ['female', 'F', 'f', 'girl', 'Girl', 'woman', 'Woman', 'w','W','G','g','GIRL','FEMALE','WOMAN']
Male = ['male','M','m','boy','Boy','B','b','man','Man','MAN','BOY']
Yes = ['y', 'Yes', 'Y', 'yes', 'yeah', 'yus','yea','ye','YES']
No = ['no','N','n','No','NO']
Tavern = ['Tavern','TAVERN', 'tavern','Pub','pub','bar','Bar','BAR','PUB']
College = ['COLLEGE','College','college']
Shop = ['shop','SHOP','Shop']
info = ['info', 'information', 'inform']#list of info
yes = ['yes','YES','Yes','Y', 'y']#list of yes
no = ['no','No','NO']#list of no
info = ['info', 'information', 'inform']#list of info
shopList = []#shopList list added to throughout program


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
        continue

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
budget = 50
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
pubstory = False
collegestory = False

if _PlayerRace == 1:
    print("You have spent all your life within the walls of Duncan\'s Rest and have grown tired of the day to day"
    + " boredom of being in a small rural town. You decide that with the savings you've managed to save up"
    + " you will leave the only home you've ever known to seek your fortune elsewhere. You have ", budget, " gold"
    + " currently and can spend it at the tavern, the college or the shop.")
    _ChoiceDR = input("Where will you go?  ")
    
    while _PlayerChoice is False:
        if _ChoiceDR in Tavern:
            print("You decide to go to the tavern")
            pubstory = True
            break
        elif _ChoiceDR in College:
            print("You decide to go to the college")
            collegestory = True
            break
        elif _ChoiceDR in Shop:
            print("You decide to go to the shop")
            _Shopping = True
            break
        else:
            print("You look far and wide for such a place, but Duncan's Rest is only a small town with very limited"
              + " access to such things.")
            _ChoiceDR = input("Please try again: ")

#To the tavern!

while pubstory is True:            
    if _ChoiceDR in Tavern:
        _DrinkDR = input("The local tavern is one you\'ve frequented plenty of times over the years with your friends. It's a small"
               + " establishment but is filled with plenty of men and women that you've known throughout the course of your"
               + " life. As you enter, the barman smiles widely:\n Your usual, I presume? ")
        if _DrinkDR in Yes  and _PlayerSex in Male:
                print("The barman begins to pour your favourite drink into a tankard, speaking as it fills and froths\n")
                _Barman = input('"How\'s your father, lad? Doing well, I hope?"')
                if _Barman in Yes:
                          print('"Good to hear, lad!" He replies. "That\'ll be two gold."')
                          budget -= 2
                          print("You spend 2 gold and have a drink. Your eye catches a stranger drinking at the end of the bar. "
                                + "He looks haunted, scared out of his wits and trembling with each sip of his beer. You wonder"
                                + " is he lost? Did he come from the war? You're considering talking to him, but you don't know if that's wise"
                                + " especially when you have a fair bit of gold on your person.")
                elif _Barman in No:
                          print('His smile drops. "He\'s caught the fever, then? Tis a shame, lad... You have my condolences."'
                                + ' He pushes the pint to you, when you go to pay, he waves his hand. "You and your father were'
                                + ' fine regulars. Never got into fights or broke my windows. Have it on me."')
                          break             
        else:
                print('"Ah, not in the mood for drinking, eh? Can\'t say I blame you, especially when there are men like him reminding us why it\'s a sin."'
                      + " He points out a strange drunkard at the end of the bar, mumbling into"
                      + " his drink. He looks like he went through hell and back, with all the scars to prove his tale.")
                break
_ApproachCrazy = input("You don\'t know if you should approach him while he\'s so preoccupied. Will you? ")
    if _ApproachCrazy in Yes:
        
            
#To the shop!

print("Welcome to the shop! You have ",budget," gold to spend!")

shopTotal = 0 #shopTotal shows total amount spent

def bread(n):
    y = 5.0 * n
    return y
def cheese(n):
    y = 3.0 * n
    return y
def sword(n):
    y = 20.0 * n
    return y
def whet(n):
    y = 10.0 * n
    return y

while _Shopping is True:
    while _Shopping is True:
        print("If you want to learn information about the item, type 'info'")
        try:
            purchase = input("Do you want to buy bread? Y or N or info?")
            if(purchase in yes):
                amount = int(input("How many do you want?"))
                shopTotal += bread(amount)
                if(budget - shopTotal >= 0):
                    shopList.append('Bread')
                    budget -= shopTotal
                    break
                else:
                    print("You cannot afford this. You have ", budget, " gold.")
                    break
                break
            elif(purchase in no):
                break
            elif(purchase in info):
                print("The bread will last 5 days, will replenish 10HP and will cost 5 gold")
                continue
            else:
                print("Input error, please type yes or no as your answer")
                continue
        except ValueError:
            print("Please enter a valid integer.")
            continue
    while _Shopping is True:
        try:
            purchase = input("Do you want to buy cheese? Y or N or info?")
            if(purchase in yes):
                amount = int(input("How many do you want?"))
                shopTotal += cheese(amount)
                if(budget - shopTotal >= 0):
                    shopList.append('Cheese')
                    budget -= shopTotal
                    break
                else:
                    print("You cannot afford this. You have ", budget, " gold.")
                    break
                break
            elif(purchase in no):
                break
            elif(purchase in info):
                print("The cheese will last 10 days, will replenish 5HP and will cost 3 gold")
                continue
            else:
                print("Input error, please type yes or no as your answer")
                continue
        except ValueError:
            print("Please enter a valid integer.")
            continue
    while _Shopping is True:
        print("If you want to learn information about the item, type 'info'")
        try:
            purchase = input("Do you want to buy a sword? Y or N or info?")
            if(purchase in yes):
                amount = int(input("How many do you want?"))
                shopTotal += sword(amount)
                if(budget - shopTotal >= 0):
                    shopList.append('Sword')
                    budget -= shopTotal
                    break
                else:
                    print("You cannot afford this. You have ", budget, " gold.")
                    break
                break
            elif(purchase in no):
                break
            elif(purchase in info):
                print("The sword will last 10 fights without the need to be sharpened. This will cost 20 gold")
                continue
            else:
                print("Input error, please type yes or no as your answer")
                continue
        except ValueError:
            print("Please enter a valid integer.")
            continue
    while _Shopping is True:
        print("If you want to learn information about the item, type 'info'")
        try:
            purchase = input("Do you want to buy whetstone? Y or N or info?")
            if(purchase in yes):
                amount = int(input("How many do you want?"))
                shopTotal += whet(amount)
                if(budget - shopTotal >= 0):
                    shopList.append('Whetstone')
                    budget -= shopTotal
                    break
                else:
                    print("You cannot afford this. You have ", budget, " gold.")
                    break
                break
            elif(purchase in no):
                break
            elif(purchase in info):
                print("The whetstone will be able to sharpen your sword whenever you make camp. This will last forever and will cost only 10 gold! A steal!")
                continue
            else:
                print("Input error, please type yes or no as your answer")
                continue
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
    purchase = input("Do you want to do any more shopping? Y or N?")
    if purchase in yes:
        continue
    else:
        break

print("Here are your final purchases: ", shopList)
print("They cost £", shopTotal, " and you have £", budget, " left over.")
print("Thank you for shopping with us.")
