# Dice Thrower
### Description
A simple dice throwing program with a command line interface that lets you roll a chosen number of dice of various sizes.
In its current implementation, it can be used to roll multiple dice at a time and adds their score together for you. It displays the total to the user and then lets you continue rolling dice.

### Installation
Clone the repository: git clone `https://github.com/wrappedbaggage/dice_thrower.git`

Navigate to the project directory: `cd dice_thrower`

Install the required Python libraries: `pip install -r requirements.txt`

### Syntax
 Each set of dice is separated by a space and looks like this:
`1d4 1d6 2d10 3d20`

Each set is formatted like this: (number of dice)d(number ofsides on dice)

The code takes each of these sets of dice and parses them to produce the result of the roll.

![Dice Thrower CLI Interface](image.png)

### License
This project is licensed under the MIT license - see license.md for details

### Contact
Simen Gåsland, simengasland@gmail.com

Project Link: https://github.com/wrappedbaggage/dice_thrower