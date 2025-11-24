ROCK, PAPER, SCISSORS PROJECT STATEMENT

------------------------------------------
Problem Statement

The goal is to create a simple, functional, and user-friendly command-line game that allows a user to play the classic game of "Rock, Paper, Scissors" against a computer opponent. The solution must accurately implement the game's core logic, handle user input effectively, and clearly communicate the outcome of the match.

--------------------------------------------------------------------------------
Scope of the Project

The project is limited to a single-player, single-round "Rock, Paper, Scissors"

The scope includes:

Game Logic: Implementing the rules (Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock) to determine the winner between two choices.
Computer AI: Generating a "random choice" for the computer opponent using the standard set of options.
User Interface: Providing prompts for the user to enter their choice and displaying the results.
Input Validation: Ensuring the user's input is restricted to the valid choices ("rock", "paper", "scissors").

------------------------------------------------------------------------
Target Users

Novice Students: Individuals learning basic Python programming concepts, including functions, dictionaries, loops, and conditional logic.
Casual Users: Anyone looking for a quick, straightforward way to play the classic Rock, Paper, Scissors game without needing to install complex software.

-----------------------------------------------------------------------------------
High-Level Features

1.  Game Initialization: Prints a welcome and loading message upon startup.
2.  User Choice Input:Prompts the user to enter their selection and continues prompting until a valid choice ("rock", "paper", or "scissors") is provided.
3.  Computer Choice Generation: The computer randomly selects one of the three options.
4.  Winner Determination: A core function ("determine_winner") uses a mapping structure to efficiently identify the winning choice between the user and the             computer. 
5.  Result Output: Displays a clear, final message indicating a win, loss, or tie for the user.
