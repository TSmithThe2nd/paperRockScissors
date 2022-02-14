#paper rock scicors simulator for those too busy to play a game of paper rock sciccors.
#brings in random number module
import random

#def places everything within its indent within its domain. One program that will run together.

def game():
    #varibles for the code, array containing rock papper scicors, varibles for players hand, number of games with winner
    #defined as games. Total number of games played and number wins by each player. 
    
    hands=['rock', 'paper', 'sciccors']
    p1=hands[random.randrange(3)]
    p2=hands[random.randrange(3)]
    games=0
    numberOfGames=0
    p1wins=0
    p2wins=0
    gamesToPlay=int(input("How many games will you play?"))

#as long as 'games' is less than the number entered by user, the program will run.
#Each run will add to the 'numberOfGames' but only rounds with a winner will add to 'games'
    while games<gamesToPlay:
        
        p1=hands[random.randrange(3)]
        p2=hands[random.randrange(3)]
      
 
        if p1==p2:
            numberOfGames+=1
                      
        elif  p1=='rock' and p2=='sciccors' or p1=='paper' and p2=='rock' or p1=='sciccors' and p2=='rock':
            p1=hands[random.randrange(3)]
            p2=hands[random.randrange(3)]
            p1wins+=1
            numberOfGames+=1
            games+=1
            
        else:
            p1=hands[random.randrange(3)]
            p2=hands[random.randrange(3)]
            p2wins+=1
            numberOfGames+=1
            games+=1
    if p1wins>p2wins:
        print ('Total of games played:'+'  '+str(numberOfGames))
        print ('Games with winner:'+'  '+str(games))
        print ('Player 1 score:'+str(p1wins)+'  '+'Player 2 score:'+str(p2wins))
        print("Player 1 wins!")
    else:
        print ('Total of games played:'+'  '+str(numberOfGames))
        print ('Games with winner:'+'  '+str(games))
        print('Player 1 score:'+str(p1wins)+'  '+'Player 2 score:'+str(p2wins))
        print("Player 2 wins!")
    

    answer=input('play again? y/n')
    if answer=='n':
        print('Thanks for playing')
    else:
        
        game()    


game()

       
