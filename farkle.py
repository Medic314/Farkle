import random

dice_art={
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}


def re_roll(players, current):
    die=dice()
    die.roll()
    round_score=die.determine_points()
    total=players[current].score
    die.print_dice()
    print(f"You rolled a {die.indx[0]}, a {die.indx[1]}, and a {die.indx[2]}")
    print(f"Round score: {round_score}")
    return round_score, total


def turn(players, current):
    print(f"Player {players[current].name}, you're up!")
    while True:
        round_score, total=re_roll(players, current)
        if round_score>49:
            reroll=input(("Would you like to roll again? (y or n only or treated as a yes) ")).strip().lower()
        else:
            print("You Farkled!")
            break
        if reroll=="n" or reroll=="no":
            break
        else:
            print("Re-rolling...")

    print(f"Overall score: {total+round_score}")
    players[current].score+=round_score

    return players


def main():
    print("Welcome to Farkle!")
    print("If you dont know the rules, here is a pdf: https://www.playmonster.com/wp-content/uploads/2018/06/Farkle-Rules.pdf ")
    input("Press enter to continue")

    players = []
    win=False
    while True:
        try:
            player_count=int(input("How many players are there? "))
            score_cap=int(input("What score do you want to play to? "))
            break
        except:
            print("Make sure you are using numbers only, ", end=" ")
        print("please try again")
    
    for i in range(player_count):
        input_name = input(f"Enter player {i+1}'s name: ")
        players.append(player(input_name))
    
    gameloop=1
    while True:
        input(f"Yall ready for round {gameloop}? (press enter to continue)")
        gameloop+=1
        for i in range(len(players)):
            players=turn(players, i)
            if players[i].score>=score_cap:
                win=True
                winning_player=i
                break
        if win==True:
            break
    print("The winner of the game has been determined...")
    print(f"The winner of the game is player number {winning_player+1}, {players[winning_player].name}, you win!")
    winner=players[winning_player].name


class player:
    def __init__(self, name, score=0):
        self.name=name
        self.score=score


class dice:
    def __init__(self, amount=3):
        self.amount=amount
        self.indx=[0, 0, 0]

    def roll(self):
        for i in range(len(self.indx)):
            self.indx[i]=random.randint(1, 6)

    def get_total(self):
        total=0
        for i in range(len(self.indx)):
            total+=self.indx[i]
        return total
    
    def print_dice(self):
        for line in range(5):
            for die in self.indx:
                print(dice_art.get(die)[line], end=" ")
            print() #didn't use comments because the functions/ methods organized it well enough
    
    def determine_points(self):
        total=0
        for i in range(3):
            if self.indx[0]==self.indx[1] and self.indx[1]==self.indx[2]:
                total+=500
                break
            elif int(self.indx[i])==1:
                total+=100
            elif int(self.indx[i])==5:
                total+=50
            else:
                total+=0

        return total


if __name__=="__main__":
    main()