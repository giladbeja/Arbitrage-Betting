from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import datetime

l = datetime.datetime.now()
y = l.year
d = l.day
m = l.month

day = d
month = "0"+str(m)
year = y
competition = ""

class matchOdds:
    def __init__(self,low,high,favorite,underdog,lowSportsbook,highSportsbook):
        self.low = low
        self.high = high
        self.favorite = favorite
        self.underdog = underdog
        self.lowSportsbook =lowSportsbook
        self.highSportsbook = highSportsbook

def scrape(year,month,day,competition):
    options = Options()
    options.add_argument("--headless=new")
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.oddstrader.com/"+competition+"/?date="+year+month+day)
    driver.implicitly_wait(5)
    #try:
    x = driver.find_elements_by_class_name("best-line")
    z = driver.find_elements_by_class_name("subtitle")
    n = driver.find_elements_by_class_name("blueHover")
    #except:
    #raise Exception("No data available for this date/competition")
    bestOdds = []
    sportsbooks = []
    competitorNames = []
    oddsObjects = []
    # for i in (0,(len(x)+1)//2,2):
    #     bestOdds.append([x[i].text,x[i+1].text])
    for i in range(len(n)):
        if(i%2==0):
            competitorNames.append([n[i].text])
        else:
            competitorNames[i//2].append(n[i].text)
    for i in range(len(x)):
        if(i%2==0):
            bestOdds.append([x[i].text])
            sportsbooks.append([z[i].text])
        else:
            bestOdds[i//2].append(x[i].text)
            sportsbooks[i//2].append(z[i].text)
    for i in range(len(bestOdds)):
        for j in range(len(bestOdds[i])):
            if(bestOdds[i][j][0]=="-"):
                try:
                    bestOdds[i][j] = int(bestOdds[i][j][1:])*-1
                except:
                    bestOdds[i][j] = 0
            else:
                try:
                    bestOdds[i][j] = int(bestOdds[i][j][1:])
                except:
                    bestOdds[i][j] = 0
    for i in range(len(bestOdds)):
        if(bestOdds[i][0]>bestOdds[i][1]):
            oddsObject = matchOdds(bestOdds[i][1],bestOdds[i][0],competitorNames[i][1],competitorNames[i][0],sportsbooks[i][1],sportsbooks[i][0])
        else:
            oddsObject = matchOdds(bestOdds[i][0],bestOdds[i][1],competitorNames[i][0],competitorNames[i][1],sportsbooks[i][0],sportsbooks[i][1])
        oddsObjects.append(oddsObject)
    return oddsObjects

#print(scrape(year,month,day,competition))