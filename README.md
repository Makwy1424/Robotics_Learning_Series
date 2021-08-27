# Robotics_Learning_Series(python_task_1.py is according to the rule)

## Rules of the game (2 Player Version):
                                      
1. One player writes down a secret 4-digit number.

2. Then, the other player tries to guess the number.

3. After each guess, the person that has written down the secret
number, tells them how many digits are correct and in the right
position and how many digits are correct but in the wrong place.

4. Players keep making guesses until they are able to guess the 4 digit
number correctly.

5. There can be a limit the number of guesses the 2nd player can have.

## Designing of the above game in python with the following specifications
                                      
> 1. The program should generate a random 4 digit number at the start.

> 2. The player starts with 20 points.

> 3. On each turn, the program asks for a number from the user.

> 4. After taking input, the program displays the digits that are correct and
     in the right position and how many digits are correct but in the wrong
     place. Also display the which digits are in correct position.

> 5. Program ends when:-
   >  a. The numbers of guesses reaches a number (Say 10) or
   >  b. The player guesses the number correctly.

> 6. For each correct guess +5 points are given and for each incorrect
>    guess -2 points are given.

> 7. On completion, Score for the user should be displayed and options to
   > play again should be provided.

Notes:

- Program must be fully function based
- Code should not be plagiarized


Example Program Run
-------------------
** Assume Random Number Generated is 1234 **

Guess a Number : 2349 (Player Input)
Output -
3 digits : [2, 3, 4] guessed correctly. 3 in the wrong position.
Turns remaining - 9

Guess a Number : 1235 (Player Input)
Output -
3 digits : [1, 2, 3] guessed correctly. 3 in the correct position.
Turns remaining - 8

Guess a Number : 1234 (Player Input)
Output -
All Digits in the Correct Place.
You have won the game!!
Your Score : 21

Do you want to play again?
