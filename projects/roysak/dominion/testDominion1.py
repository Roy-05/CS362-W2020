# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 4:05 AM

@author: Saket Roy
"""
import testUtility
import random


def bug(supply):
    """
    The following bug changes the quantity of each card 
    that is present in the supply by a factor of 0-100.
    It further changes the quantity of Silver and Gold
    cards in the game to 0, resulting in the players to 
    only have Copper to play the game with.
    """ 

    for card in supply:
        supply[card] *= random.randint(0,100)
    
    cardsToRemove = ["Silver", "Gold"]
    for card in supply:
        if card in cardsToRemove:
            supply[card] *= 0

def main():
    #Set player names
    player_names = ["*Annie","*Ben","*Carla"]

    #number of Curses and Victory cards
    nV = testUtility.get_nV(player_names)
    nC = testUtility.get_nC(player_names)

    #Define box
    box = testUtility.getBoxes(nV)

    #Get Supply order
    supply_order = testUtility.getSupplyOrder()

    #Get Supply
    supply = testUtility.getSupply(box, player_names, nV, nC)

    #Get players for the game
    players = testUtility.getPlayers(player_names)

    bug(supply)
    testUtility.play(supply, supply_order, players)

if __name__ == "__main__":
    main()