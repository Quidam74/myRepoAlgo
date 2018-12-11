##
#
# @author Florian BELLANGER, Fyne DC, Annecy, FRANCE
# @brief a set of generic functions for data management



from random import randrange

def humanTurn():
    """
        permit to the human to play
    arg:
            
    return:
        the score during this turn
    """
    score = 0
    wantToPlay = input("lancer le dé ? : (o/n) ")
    while wantToPlay =="o":
           diceResulte = randrange(1,6)
           print (diceResulte)
           score += diceResulte
           if(diceResulte==1):
               score = 0
               print("dommage !")
               break
           else:
               print("score : "+str(score))
               wantToPlay = input("lancer le dé ? : (o/n) ")
    return score
    

def botTurn():
    """
        permit to the bot to play witout display
    arg:
            
    return:
        the score during this turn
    """
    score = 0
    diceResulte = 6
    while diceResulte !=0:
        diceResulte = randrange(0,6)
        score += diceResulte
        if(diceResulte==1):
            score = 0
            break
    print("score marqué par le bot cette manche : "+str(score))
    return score
    
    

def shuffle(list_in):
    """
       a dice gamewho follow those rules
       At the beginning, each player has a null score and the winner is the first obtaining at least 100 points.
       Participants play in turn but the user always starts.
       Each player throws a dice as many times as he wants until he obtains '1' or he wants to stop
       When stopping, if the player obtained ’1’ then score does not increase. In the other case, the score is increased by the sum of all the dice values obtained this turn.
    Arg:
        list_in : a list where each index is a player, bot or human
    return:
        return the final score
    """
    player = 0
    gameIsRunning = True
    while  gameIsRunning:
        player = 0
        for player in  range(len(list_in)):   
            if(player+1 == len(list_in)):
                print("c'est le tour du bot")
                list_in[player] += botTurn()
            else:
                print("c'est le tour de l'humain")
                list_in[player] += humanTurn()
            
            print("score total de joueur "+str(player+1)+" : "+ str(list_in[player]))
            if(list_in[player] >=100):
                gameIsRunning = False
                print("le joueur "+str(player+1)+" a gagné")
                break
    return list_in


begin =[0,0]
shuffle(begin)


