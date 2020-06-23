while True:
    print("\nYou have begun a two-player game of Rock-Paper-Scissors")
    play1 = input("\nPlayer 1: Please provide a move: ").title()
    play2 = input("Player 2: Please provide a move: ").title()
    
    if play1 == play2:
        print("It is a draw!")
    
    elif (play1 == "Rock" and play2 == "Scissors"):
        print("Rock (Player 1) beats Scissors (Player 2). Player 1 Wins!")
        
    elif (play1 == "Scissors" and play2 == "Rock"):
        print("Rock (Player 2) beats Scissors (Player 1). Player 2 Wins!")

    elif (play1 == "Paper" and play2 == "Rock"):
        print("Paper (Player 1) beats Rock (Player 2). Player 1 Wins!")
    
    elif (play1 == "Rock" and play2 == "Paper"):
        print("Paper (Player 2) beats Rock (Player 1). Player 2 Wins!")
    
    elif (play1 == "Scissors" and play2 == "Paper"):
        print("Scissors (Player 1) beats Paper (Player 2). Player 1 Wins!")

    elif (play1 == "Paper" and play2 == "Rock"):
        print("Scissors (Player 2) beats Paper (Player 1). Player 2 Wins!")
    else:
        print("Invalid input! You have not entered rock, paper or scissors.")

    playagain = input("\nPlay again? (Y/N): ").title() 
    if playagain == 'Y':
        continue
    else:
        break






