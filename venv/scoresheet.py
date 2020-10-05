class Scoresheet:

    def __init__(self):
        #Flag to determine in player has used score catergory in a previous turn
        self.category_used = dict.fromkeys(range(1,14),False)

        #Dictionary to keep track of current score values
        self.current_score = dict.fromkeys(range(1,14),0)

        #Dictionary for score name category and number for user to pick which category to score
        self.score_category = {
            1:'Ones',
            2:'Twos',
            3:'Threes',
            4:'Fours',
            5:'Fives',
            6:'Sixes',
            7:'3 of a kind',
            8:'4 of a kind',
            9:'Full house',
            10:'Small Straight',
            11:'Large Straight',
            12:'YachtZ',
            13:'Chance'
        }

    @property
    def display_categories(self):
        for index in range(1, 14):
            print('{}: {}'.format(index, self.score_category[index]))

    @property
    #Displays scorecard with scores
    def display_scorecard(self):
        print("\nScoresheet\n")
        for index in range(1, 14):
            if self.category_used[index]==True:
                print("{}: {}".format(self.score_category[index], self.current_score[index]))
            else:
                print('{}: '.format(self.score_category[index]))

            if index == 6:
                bonus_condition = [self.current_score[i] for i in range(1,7)]
                if sum(bonus_condition) >= 63 :
                    bonus=35
                else:
                    bonus = 0
                print("Bonus: {}".format(bonus))

            if index == 13:
                total = sum(self.current_score.values()) + bonus
                print("Total: {}".format(total))

    @property
    #Displays categories that have not already been used
    def available_score_categories(self):
        available_categories = {}
        for cat_num in self.category_used:
            if self.category_used[cat_num] == False:
                available_categories[cat_num] = self.score_category[cat_num]
        return available_categories

    #Calculate score for the ones category. Input is  of the YachtZDice class
    def score_ones(self, dice):
        self.category_used[1]=True
        return dice.ones * 1

    def score_twos(self, dice):
        self.category_used[2] = True
        return dice.twos * 2

    def score_threes(self, dice):
        self.category_used[3] = True
        return dice.threes * 3

    def score_fours(self, dice):
        self.category_used[4] = True
        return dice.fours * 4

    def score_fives(self, dice):
        self.category_used[5] = True
        return dice.fives * 5

    def score_sixes(self, dice):
        self.category_used[6] = True
        return dice.sixes * 6

    def score_three_of_a_kind(self,dice):
        self.category_used[7] = True
        for count_ in dice.dice_count:
            if count_ >= 3:
                return sum(dice)
        return 0

    def score_four_of_a_kind(self, dice):
        self.category_used[8] = True
        for count_ in dice.dice_count:
            if count_ >= 4:
                return sum(dice)
        return 0

    def score_full_house(self, dice):
        self.category_used[9] = True
        if dice.dice_count.count(0) == 4:
            for count_ in dice.dice_count:
                if count_ == 3:
                    return 25
        if dice.dice_count.count(0) == 5:
            return 25
        return 0

    def score_small_straight(self,dice):
        self.category_used[10] = True
        if dice.dice_count.count(0) == 2:
            if (dice.fives == 0 and dice.sixes == 0) \
                or (dice.ones == 0 and dice.sixes == 0) \
                or (dice.ones == 0 and dice.twos == 0):
                return 30
        if dice.dice_count.count(0) == 1:
            if dice.threes != 0 or dice.fours != 0:
                return 30
        return 0

    def score_large_straight(self, dice):
        self.category_used[11] = True
        if dice.dice_count.count(0) == 1:
            if dice.ones != 0 or dice.sixes != 0:
                return 40
        return 0


    def score_yachtz(self, dice):
        self.category_used[12] = True
        for count_ in dice.dice_count:
            if count_ == 5:
                return 50
        return 0

    def score_chance(self,dice):
        self.category_used[13] = True
        return sum(dice)

    score = {
        1: score_ones,
        2: score_twos,
        3: score_threes,
        4: score_fours,
        5: score_fives,
        6: score_sixes,
        7: score_three_of_a_kind,
        8: score_four_of_a_kind,
        9: score_full_house,
        10: score_small_straight,
        11: score_large_straight,
        12: score_yachtz,
        13: score_chance
    }

    def record_score(self,cat,dice):
        return self.score[cat](self,dice)
