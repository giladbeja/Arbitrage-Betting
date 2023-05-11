import math

def convert(odds):
    if(math.fabs(odds)<100):
        return odds
    if(odds<0):
        return round((1-(100/odds)),2)
    return round(((odds/100)+1),2)

def checkArbitrage(odds1,odds2):
    if(odds1==0 or odds2==0):
        return False
    impliedOdds = ((1/odds1)+(1/odds2))
    if impliedOdds<1:
        return True
    return False

