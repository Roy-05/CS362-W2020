# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 4:05 AM

@author: Saket Roy
"""
import testUtility
import random


def bug(supply_order):
    """
    The supply order is a key-value object relating
    the cost of a card to the names of the card. The 
    following bug generates a new supply order object by
    replacing each cost with a random ASCII character between
    65-90 [A-Z] and assigns to it the cards associated with the initial cost
    """

    for value in list(supply_order):
        supply_order[chr(random.randint(65,90))] = supply_order.pop(value)

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
    
    bug(supply_order)
    testUtility.play(supply, supply_order, players)

if __name__ == "__main__":
    main()