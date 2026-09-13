import requests
import json
import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt
import math

url = 'https://fantasy.premierleague.com/api'

#command line input of teamID, if you do not have a teamID, feel free to try with mine: 8746052
print("FPL Rank Summary ")
try:
    teamID = int(input("Please Enter your team ID: "))
except ValueError:
    print("\nPlease enter an Interger ID")


# instructions on how to get your FPL team id can be found here: https://fpl.team/find-fpl-team-id/
managerHistory = f'/entry/{teamID}/history/'
managerName = f'/entry/{teamID}/'

# getting requests for FPL data
r = requests.get(url+managerHistory).json()
sum = pd.json_normalize(r['current'])
l = requests.get(url+managerName).json()
fplName = l['name']


#forming a dataset for the FPL data
gameWeeks = []
gwRank = []
#Dictionary to stored name for chips with display names on plot
chipsDict = {'wildcard': 'Wildcard', 'freehit': 'Free Hit', 'bboost': 'Bench Boost', '3xc': 'Triple Captain'}

for week in sum['event']:
    rank = sum.loc[sum['event'] == week, 'overall_rank'].item()
    gwRank.append(rank)
    gameWeeks.append(week)

data = {'Gameweek': gameWeeks, 'Gameweek Rank': gwRank}
df = pd.DataFrame(data=data)
# uncomment this to view your data in table form
#print(df)


# plotting and titling
plt.plot(df['Gameweek'], df['Gameweek Rank'], color = 'black')
plt.title(f"FPL Rank for {fplName} this season") 

# tick and axis altering
plt.ylim(bottom=0) # sets the range of the y-axis to start from 0
plt.gca().invert_yaxis()  #inverts the rank so 0 is the top

#alters y ticks to have commas representing thousands and millions
current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])

#displays the x axis ticks (gameeweeks) as integers rather than decimals
integer_ticks = range(math.floor(min(df['Gameweek'])), math.ceil(max(df['Gameweek']))+ 1)
plt.xticks(integer_ticks)

#labeling
plt.xlabel("Gameweek")
plt.ylabel("Rank")

#annotation for chips used
for chip in r['chips']:
    name = chip['name']
    event = chip['event']
    rank = sum.loc[sum['event'] == event, 'overall_rank'].item()
    plt.annotate(
                 text = chipsDict.get(name), 
                 color = 'C0', 
                 fontsize= 10,
                 xy = (event, rank), textcoords = 'offset points', 
                 xytext = (0, 10),
                 ha = 'center'
                 )
    print (name, event, rank)
plt.grid()
plt.show()
