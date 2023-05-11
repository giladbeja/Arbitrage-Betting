from scrape import scrape, matchOdds
from helper import convert, checkArbitrage

def calculateProfits(stake,odds):
    lower = 0
    higher = 0
    if(odds[0]>odds[1]):
        lower=odds[1]
        higher=odds[0]
    else:
        lower=odds[0]
        higher=odds[1]
    lowerBet = round((higher/(lower+higher))*stake,2)
    higherBet = round((lower/(higher+lower))*stake,2)
    profit = round((higherBet*(higher-1))-lowerBet,2)
    return profit, lowerBet, higherBet

def output(bestOdds,stake,oddsObject):
    if(checkArbitrage(bestOdds[0],bestOdds[1])):
        profit, lowerBet, higherBet = calculateProfits(stake,bestOdds)
        print("Arbitrage Exists")
        print("Case 1: "+str(bestOdds[0])+" Case 2: "+str(bestOdds[1]))
        print("If you staked: "+str(stake)+", you could bet "+str(lowerBet)+ " on "+ oddsObject.favorite +" through "+oddsObject.lowSportsbook+" and "+str(higherBet)+" on "+oddsObject.underdog+" through "+oddsObject.highSportsbook)
        print("The guaranteed profit would be: "+str(profit))
    else:
        print("Arbitrage does not exist for: "+ oddsObject.favorite +" vs "+ oddsObject.underdog)

oddsObjects = scrape("2023","05","13","atp")

for i in oddsObjects:
    arbs = []
    case1 = convert(i.low)
    case2 = convert(i.high)
    bestOdds = [case1,case2]
    output(bestOdds,100,i)