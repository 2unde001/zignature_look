"""
Rock paper scissors
"""
import random
import simplegui

# Global variables that all functions know about.
# DO NOT EDIT THESE GLOBAL VARIABLES
# OR YOUR GAME WILL BREAK.
COMPUTER_SCORE = 0
HUMAN_SCORE = 0
human_choice = ""
computer_choice = ""


def choice_to_number(choice):
    """Convert choice to number."""

    return {"rock": 0, "paper": 1, "scissors": 2}[choice]


def number_to_choice(number):
    """Convert number to choice."""

    return {0: 'rock', 1: 'paper', 2: 'scissors'}[number]


def random_computer_choice():
    """Choose randomly for computer."""

    return random.choice(['rock', 'paper', 'scissors'])


def choice_result(human_choice, computer_choice):
    """Return the result of who wins."""
    global  COMPUTER_SCORE
    global HUMAN_SCORE
    human_number = choice_to_number(human_choice)
    computer_number = choice_to_number(computer_choice)

    if (human_number - computer_number) % 3 == 1:
        COMPUTER_SCORE = COMPUTER_SCORE +1
    elif human_number == computer_number:
        print("Tie")
    else:
        HUMAN_SCORE = HUMAN_SCORE + 1
