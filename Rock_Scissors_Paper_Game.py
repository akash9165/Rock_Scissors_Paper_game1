###Rock vs Paper -> win = Paper
###Rock vs scissors -> = Rock
### Scissors vs Paper -> = Scissors

import random
li = ['rock','paper','scissors']
while True:
    Ccount = 0
    Ucount = 0
    userinput11 = int(input('''
--------Welcome to Rock Paper Scissors Game---------
1.Start Game
2.Exit Game
    '''))
    if userinput11==1:
            print("-----Start the Game-----")
            for i in range(1,6,+1):
                userinput=int(input('''
                1.Rock
                2.Scissors
                3.Paper 
                    '''))
                if userinput==1:
                        Uchoice = "rock"
                elif userinput==2:
                        Uchoice = "scissors"
                elif userinput==3:
                        Uchoice = "paper"  

                Ccomputer = random.choice(li)

                if Ccomputer==Uchoice:
                    print("------------------------Game Draw--------------------------")
                    print("Computer Choise=",Ccomputer)
                    print("Your Choise :- ",Uchoice)
                    Ucount = Ucount+1
                    Ccount = Ccount+1
                elif (Uchoice=="rock" and Ccomputer=="scissors") or (Uchoice=="paper" and Ccomputer=="rock") or (Uchoice=="scissors" and Ccomputer=="paper"):
                    print("_------------------------YOU WIN-----------------------------")
                    print("Computer Choise:-- ",Ccomputer)
                    print("Your Choise :-- ",Uchoice)
                    Ucount = Ucount+1
                else:
                    print("-------------------------COMPUTER WIN-------------------------")
                    print("Computer Choise:-- ",Ccomputer)
                    print("Your Choise :-- ",Uchoice)
                    Ccount = Ccount+1          
            if Ucount==Ccount:
                print("-----------------------------Draw the Game-------------------------")
                print("User Score:-- ",Ucount)
                print("Computer Score:-- ",Ccount)  
            else:
                print("----------------------------Final computer win----------------------")
                print("User Score:-- ",Ucount)
                print("Computer Score:-- ",Ccount)  
    else:
        break
