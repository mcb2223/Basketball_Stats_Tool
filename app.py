from ntpath import join
from operator import index
from os import name
from re import A

from numpy import average
import constants
from copy import deepcopy
import sys



teams=deepcopy(constants.TEAMS)
players=deepcopy(constants.PLAYERS)
team_name= """

Team name: """
spacer = "-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-"
exit_message = "Exiting Application. Thank you for visiting!"
experienced=[]
not_experienced=[]
bandits = {
    "players": [],
    "experienced": 0,
    "inexperienced": 0,
    "player_heights": [],
    "average_height": None,
    "guardians":[]
}

panthers = {
    "players": [],
    "experienced": 0,
    "inexperienced": 0,
    "player_heights": [],
    "average_height": None,
    "guardians": []
}

warriors = {
    "players": [],
    "experienced": 0,
    "inexperienced": 0,
    "player_heights": [],
    "average_height": None,
    "guardians": []
}

def clean_data():
    for player in players:
        height= player["height"].split()
        player["height"]=int(height[0])
        player["guardians"]=player["guardians"].split(" and ")
        if player["experience"] == "YES":
            player["experience"] = True
            experienced.append(player)
        elif player["experience"] == "NO":
            player["experience"] = False
            not_experienced.append(player)
    return not_experienced, experienced


def team_balancer():
    
    exp_per_team= int(len(experienced))/len(teams)
    not_exp_per_team= int(len(not_experienced))/len(teams)
    tot_per_team= exp_per_team+not_exp_per_team

    for player in experienced:
        if len (bandits["players"])<exp_per_team:
            bandits["players"].append(player["name"].split("'"))
            bandits["experienced"] +=1
            bandits["player_heights"].append(player["height"])
            bandits["guardians"].append(player["guardians"])
        elif len(panthers["players"]) < exp_per_team:
            panthers["players"].append(player["name"].split("'"))
            panthers["experienced"] += 1
            panthers["player_heights"].append(player["height"])
            panthers["guardians"].append(player["guardians"])
        elif len(warriors["players"]) < exp_per_team:
            warriors["players"].append(player["name"].split("'"))
            warriors["experienced"] += 1
            warriors["player_heights"].append(player["height"])
            warriors["guardians"].append(player["guardians"])
    for player in not_experienced:
        if len(bandits["players"]) < tot_per_team:
            bandits["players"].append(player["name"].split(","))
            bandits["inexperienced"] += 1
            bandits["player_heights"].append(player["height"])
            bandits["guardians"].append(player["guardians"])
        elif len(panthers["players"]) < tot_per_team:
            panthers["players"].append(player["name"].split(","))
            panthers["inexperienced"] += 1
            panthers["player_heights"].append(player["height"])
            panthers["guardians"].append(player["guardians"])
        elif len(warriors["players"]) < tot_per_team:
            warriors["players"].append(player["name"].split(","))
            warriors["inexperienced"] += 1
            warriors["player_heights"].append(player["height"])
            warriors["guardians"].append(player["guardians"])
            
    team_cleaner(panthers)
    team_cleaner(bandits)
    team_cleaner(warriors)

    


#additional stuff here to order players by height
    #start empty list
    #loop throught original list
    #find shortest
    #variable that contains lowest height or name or index, then after loop pop him into ordered list.    

    
    return bandits, panthers, warriors
    



def console_menu():
    
    
    team_1= "Panthers"
    team_2= "Bandits"
    team_3= "Warriors"
    print("""
                               Basketball Stats Tool                    
          I am designed to help analyze players and create balanced teams.
          
        """)
    print("-_-_-_-_- MENU -_-_-_-_-")
    print("""
        Options:
    A) Team Stats
    B) Exit
    """)
    options= input("Please select an Option: ")
    while True:
        try:
            if options.upper() == "A":
                print("""
Select a Team to display their stats.
                      """)
                print("""    A) Panthers
    B) Bandits
    C) Warriors
    D) Exit Program""")
                break
            elif options.upper()== "B":
                print(exit_message)
                quit()
            else:
                print('Not recognised as a valid option, please enter a valid letter value')
                console_menu()
                raise ValueError
        except ValueError as err:
            print('Not recognised as a valid option, please enter a valid letter value')
            return console_menu()
    while True:
        try:
            team= input("""
Enter the letter of which team you would like to analyze """)
            if team.upper()== "A":
                print(team_name + team_1)
                print(spacer)
                player_stats(panthers)
                other_teams()
            elif team.upper()== "B":
                print(team_name + team_2)
                print(spacer)
                player_stats(bandits)
                other_teams()    
            elif team.upper() == "C":
                print(team_name + team_3)
                print(spacer)
                player_stats(warriors)
                other_teams()
            elif team == "D":
                print(exit_message)
                quit()
            else:
                print('Not recognised as a valid option, please enter a valid letter value')
                console_menu()
                raise ValueError
        except ValueError as err:
            print('Not recognised as a valid option, please enter a valid letter value')
            console_menu()
        return console_menu()


def team_cleaner(team):
    team["players"] = ", ".join([", ".join(x) for x in team["players"]])
    team["guardians"] = ", ".join([", ".join(x) for x in team["guardians"]])
    team["average_height"]=sum(bandits["player_heights"])/len(team["player_heights"]) 

def player_stats(team):
    players= team["players"]
    guardians= team["guardians"]
    print(f"""
        Total players: {team["experienced"]+team["inexperienced"]}
        Total experienced: {team["experienced"]}
        Total inexperienced: {team["inexperienced"]}
    """)
    print("Player names: ")
    print(f"      {players}")
    print("Guardian Names: ")  
    print(f"      {guardians}")
    
    



def other_teams():
    change_team= input("""
Would you like to analyze another team? Y or N """)
    if change_team.upper()== "Y" :
        print("Returning to menu. ")
        return console_menu()
    if change_team.upper() == "N":
        print(exit_message)
        quit()  
    else:
        print('Not recognised as a valid option, returning to the main menu')
        return console_menu()        


if __name__ == '__main__':
    clean_data()
    team_balancer()
    console_menu()
