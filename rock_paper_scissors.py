#Alireza Tavakoli
#2019-08-26

# 1 > scissors
# 2 > stone
# 3 > paper

win1 = 0 
win2 = 0

print ( ' exit condition -- >> player1 = 0 and player2 = 0\n\n\n')

while True :
    print ( ' scissors > 1 \t stone > 2 \t paper > 3\n========+++++++===========')

    player1     =   int ( input ( 'player1:enter the number : '))
    player2     =   int ( input ( 'player2:enter the number : '))
    print ()
    
    if   ( player1 == 1 and player2 == 2) or ( player1 == 2 and player2 ==3) or ( player1 == 3 and player2 == 1):
        print ( 'win player 2')
        win2 += 1
        print ()
    
    elif ( player1 == 2 and player2 == 1) or ( player1 == 1 and player2 == 3) or ( player1 == 3 and player2 == 2):
        print ( 'win player 1')
        win1 += 1
        print ()

    elif player1 == 0 and player2 == 0: #exit condition
        break

if win1 > win2:
    print ( 'winer is player1')
elif win2 > win1:
    print ( 'winer is player2')
else :
    print ( "equal!!")
