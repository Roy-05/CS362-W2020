# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 4:05 AM

@author: Saket Roy
"""
import testUtility

#Get player names
player_names = testUtility.getPlayerNames()

#number of curses and victory cards
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

def main():
    testUtility.play(supply, supply_order, players)


if __name__ == "__main__":
    main()