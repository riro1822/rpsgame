ROCK, PAPER, SCISSORS GAME
-----------------------------------
Overview of the Project

This is a simple, text-based application for playing the classic Rock, Paper, Scissors game against the computer. The user inputs their choice, and the computer makes a random choice. The program then determines the winner based on the standard rules and displays the outcome.

-----------------------------------------------------------------------------------------------------------------------
Features

User Input Validation:Ensures the user only enters one of the three valid options: "rock", "paper", or "scissors".
Random Computer Choice: Uses Python's "random" module to ensure the computer's choice is unpredictable.
Clear Winner Determination: Logic is implemented using a nested dictionary structure for quick and clear determination of the winning move.
Clear Output: Provides informative messages for the user's choice, the computer's choice, and the final result (Win, Lose, or Tie).

------------------------------------------------------------------------------------------------------------------------------------------------
Tools Used

Language:Python 3 
Modules:The built-in "random" module.
Environment: Terminal

----------------------------------------------
Steps to Install & Run the Project

1.  Save the Code: Save the provided Python code into a file named "rps.py" 
2.  Prerequisite: Ensure you have 'Python 3" installed on your machine. 
3.  Run the Game: Open your terminal , navigate to the directory where you saved "rps.py", and execute the script:
    "python game.py"
    
--------------------------------------------------------------------------------------------------------------------------
Instructions for Testing

Once the game is running, you will be prompted to make your choice:

1.  Enter a valid choice:
    Type rock and press Enter.
    Type paper and press Enter.
    Type scissors and press Enter.
2.  Observe the result: The program will output the computer's choice and then the final message:
       "Congratulations, you won!"
       "Oh, the computer won. It's ok."
       "Oh, it's a tie."
3.  Test invalid input: Try entering choices like `Rock`, `Sheet`, or `VIT`. The program should display the error message and reprompt you:
    > Expecting one of: 'rock', 'paper', or 'scissors' (lower case, without the quotation marks). Please try again.

-------------------------------------------------------------------------------------------------------------------------------------------------



