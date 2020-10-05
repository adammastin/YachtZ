from  Die import Die,D6,D5
from roll import YachtZDice,Dice
from scoresheet import Scoresheet

die1 = D6()
die2 = D6()
die3 = D5()
die4 = D6()
die5 = D6()

# Initialize a new game
def start_game():
    scoresheet = Scoresheet()
    game_dice = YachtZDice(die1, die2, die3, die4, die5)
    return scoresheet, game_dice

# Logic for each round of the game. Input Scoresheet class, YachtZDice class
def round(player,dice):
    reroll_dice=True
    num_rolls = 1
    dice.initial_roll()

    while reroll_dice == True and num_rolls<=3:
        reroll_dice = dice.reroll()
        num_rolls += 1

    print(player.available_score_categories)
    categories_left = player.available_score_categories
    while True:
        try:
            category_answer = int(
                input('Enter the number of the above available categories you would to record your score in:'))
            if category_answer in categories_left:
                break
            print('Category entered not valid.')

        except Exception as e:
            print(e)

    player.current_score[category_answer] = player.record_score(category_answer,dice)
    player.display_scorecard
    return


player1, dice=start_game()
round_number = 1

while round_number < 14:
    print("\n***\nRound {}\n***\n".format(round_number))
    round(player1,dice)
    round_number += 1


print("\nThank you for playing.")






