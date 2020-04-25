VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer(object):
    
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
        
    def addMoney(self, amt):
        self.prizeMoney += amt
    
    def goBankrupt(self):
        self.prizeMoney = 0
    
    def addPrize(self, prize):
        self.prizes.append(prize)
    
    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)

# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    
    def getMove(self, category, obscuredPhrase, guessed):
        sentence = "{} has ${}".format(self.name, self.prizeMoney)
        sentence += "\n\n"
        sentence += """
Category: {}
Phrase:   {}
Guessed:  {}""".format(category, obscuredPhrase, ', '.join(sorted(guessed)))
        sentence += "\n\n"
        print(sentence)
        move = input("Guess a letter, phrase, or type 'exit' or 'pass':")
        return move
        
# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.prizeMoney = 0
        self.prizes = []
     
    def smartCoinFlip(self):
        if random.randint(1, 10) > self.difficulty:
            return True
        else: 
            return False
    
    def getPossibleLetters(self, guessed):
        lst = []
        if self.prizeMoney >= 250: 
            for l in LETTERS:
                lst.append(l)
        else:
            for l in LETTERS:
                if l not in VOWELS:
                    lst.append(l)
        return lst

    def getMove(self, category, obscuredPhrase, guessed):
        lst = self.getPossibleLetters(guessed)
        FlipResult = self.smartCoinFlip()
        if len(lst) == 0:
            return 'pass'
        else:
            if FlipResult==True:
                for l in self.SORTED_FREQUENCIES:
                    if l in lst:
                        return l
            elif FlipResult==False:
                return random.choice(lst)