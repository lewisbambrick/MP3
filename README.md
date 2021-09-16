# Battleship!

Battleship is just a simplified version of the standard boardgame Battleship. In this version however it only contains a single ship to hit and is played entirely on the command console.

The aim of the game is to find the computers battleship before you run out of turns.
## [Click here to see if you can sink the computers Battleship](https://battleship-pro3.herokuapp.com/)
---

## Playing ther game
    The rules of the game are really quite simple, You only have to guess where the computers Battleship is.
    The console will display for you a Row of 5 by 5, and ask you what row and colum you would like to select. You just have to guess right to sink the computers ship and claim victory.However you only have 4 turns in which to do it, so make your choices wisely.
---

## Features

### Existing Features
- Random board generation
    - the computer has a battleship hidden on the 5 by 5 board that is given a random position.
- Accepts user interface, such as selecting the row and colum that they would like to chose.
- Informs players when they make a maistake such as guessing coordinates outside the playable board.
- Allows the player to compete against a computer.
- Gives player 4 turns to best the computer.

### Future Features
- Allowing the player to input their name
- Giving the player battleships to hide that the computer will try to guess.
- Making it a multiple battleship game, with the option to set difficulty to decide how many ships there are.
- Possibly have single ships that are mre than just 1 space.

## Design
- I decided to use a single board type of layout for the game board as i seen that as the best way to ensure that there was no confusion with the user.
- For the unguessed spaces i decided to use an "O" as it seemed like the clearest way of showing the user that it was a space that hasnt been guessed yet.
- Similarily i decided to use an "X" to show the spots that were previously guessed for the same reasons, and to help the user avoid choosing the same space and wasting a turn.

## Testing
- I have tested the code myself by selecting the possible inputs and scenarios that could be chosen by a user and ensuring that the code works without issue.
    However I was not able to test the code on PEP8 as I have tried it on multiple devices but everytime I try to load it up it keeps timing out.

## Deployment 
    The steps I have taken for deployment are:
    - Create a new app on Heroku.
    - Set the Buildpacks for Python and NodeJS, in that exact order.
    - link the Heroku app to the GitHub repo.
    - Deploy.

## Credits
- Code Institute, Fore the python essentials template.
- multiple sources across youtube for inspiration.