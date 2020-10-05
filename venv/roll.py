from Die import Die, D6

class Dice(list):
    def __init__(self, *args, **kwargs):
        self.size = 0
        for arg in args:
            if not isinstance(arg,Die):
                raise ValueError("Argument must be of the Die class")
            self.append(arg)
            self.size += 1

    def initial_roll(self):
        for die in self:
            die.roll()
        print("You rolled")
        print(self)

    def reroll(self):
        reroll_answer = ['n']*self.size
        dieNum = 1
        for die in self:
             print('Would you like to reroll die #{}  with a value of: {}'.format(dieNum,die))
             while True:
                 try:
                     x = input('y or n?')
                     ans = x.lower()
                     if ans == 'y' or ans == 'n':
                         break
                     print('Invalid input. Please enter y or n ...')

                 except Exception as e:
                     print(e)

             print('\n')
             reroll_answer[dieNum-1]=ans
             dieNum += 1

             if ans == 'y':
                 die.roll()

        if reroll_answer.count('n')==self.size:
            print("Your dice are")
            print(self)
            return False
        else:
            print("You rolled")
            print(self)
            return True

class YachtZDice(Dice):
    def __init__(self, *args,  **kwargs):
        super().__init__( *args, **kwargs)
        if self.size != 5:
            raise ValueError('YachtZ uses 5 dice to play')
        for arg in args:
            if arg.sides != 6:
                raise ValueError("YachtZ uses 6 sided dice to play. {} is not a 6 sided die".format(arg))

    @property
    def ones(self):
        return self.count(1)

    @property
    def twos(self):
        return self.count(2)

    @property
    def threes(self):
        return self.count(3)

    @property
    def fours(self):
        return self.count(4)

    @property
    def fives(self):
        return self.count(5)

    @property
    def sixes(self):
        return self.count(6)

    @property
    #list of how many dice landed on what side
    def dice_count(self):
        return [
            self.ones,
            self.twos,
            self.threes,
            self.fours,
            self.fives,
            self.sixes
        ]