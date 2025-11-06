import random
import time

# to-do: implement items:
    # magnifying glass: checks current round
    # cigarette pack: heals 1 hp
    # beer: ejects current round
    # handcuffs: skips one of the adversary's turns
    # hacksaw: makes the shotgun deal 2 damage for one turn

round_hp = random.randint(2, 4)
round_types = ["live", "blank"]

class Player:
    def __init__(self):
        self.hp = round_hp
        

    # returns True if player is gonna have another turn
    def shoot_self(self, shotgun):
        if(shotgun.rounds[-1] == "live"):
            shotgun.rounds.pop()
            self.hp -= 1
            return False
        else:
            shotgun.rounds.pop()
            return True
    
    # returns True if the dealer was shot with a live bullet
    def shoot_adversary(self, shotgun, adversary):
        if(shotgun.rounds[-1] == "live"):
            shotgun.rounds.pop()
            adversary.hp -= 1
            return True
        else:
            shotgun.rounds.pop()
            return False
        
        

class Shotgun:
    def __init__(self):
        print("loading...")
        time.sleep(2)
        self.rounds = round_types.copy()
        random.shuffle(self.rounds)
        for i in range(random.randint(0, 4)):
            self.rounds.append(random.choice(round_types))
        random.shuffle(self.rounds)

    def state(self):
        bullets = [self.rounds.count("live") ,self.rounds.count("blank")]
        return bullets

    def print_state(self):
        print(self.state()[0], "live.", self.state()[1], "blank.")

    def check_barrel(self):
        if self.rounds != []:
            return

        print("\nreloading...")
        time.sleep(2)
        self.rounds = round_types.copy()
        random.shuffle(self.rounds)
        for i in range(random.randint(0, 4)):
            self.rounds.append(random.choice(round_types))

        self.print_state()


def player_turn():
    time.sleep(2)
    print("\nPLAYER TURN")
    print("\ntype \"dealer\" to shoot the dealer or type \"self\" to shoot self")
    player_move = input()

    if(player_move == "dealer"):
        if player.shoot_adversary(shotgun, dealer):
            print('\nyou shot the dealer with a live bullet')
        else:
            print('\nyou shot the dealer with a blank bullet')

    elif(player_move == "self"):
        if player.shoot_self(shotgun):
            print('\nthe bullet was blank')
            player_turn()
        else:
            print('\nthe bullet was live')
    else:
        print("invalid input")
        player_turn()

def dealer_turn(shotgun):
    time.sleep(2)
    print("\nDEALER TURN")
    
    live = shotgun.state()[0]
    blank = shotgun.state()[1]

    if live >= blank:
        if dealer.shoot_adversary(shotgun, player):
            print("\nthe dealer shot you with a live bullet")
        else:
            print("\nthe dealer shot you with a blank bullet")
    
    elif blank > live:
        if not dealer.shoot_self(shotgun):
            print("\nthe dealer shot himself with a live bullet")
        else:
            print("\nthe dealer shot himself with a blank bullet")
            dealer_turn(shotgun) # erro aqui

def print_hp(player, dealer):
    print("\nplayer hp: ", player.hp)
    print("dealer hp: ", dealer.hp)

player = Player()
dealer = Player()
shotgun = Shotgun()

print("\nBACKSHOT ROULETTE")

shotgun.print_state()

print_hp(player, dealer)


while(player.hp > 0 and dealer.hp > 0):
    shotgun.check_barrel()

    player_turn()

    print_hp(player, dealer)

    shotgun.check_barrel()

    if player.hp == 0 or dealer.hp == 0:
        break

    dealer_turn(shotgun)

    print_hp(player, dealer)
    

if(dealer.hp == 0):
    print("\nmoggou")

else:
    print("\nfoi moggado")



