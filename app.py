from ntpath import join
from re import A
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
panthers=[]
bandits=[]
warriors=[]


def clean_data():
    for player in players:
        height= player["height"].split()
        player["height"]=int(height[0])
        player["guardians"].replace(" and ", ", ")
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
        if len (bandits)<exp_per_team:
            bandits.append(player)
        elif len(panthers) < exp_per_team:
            panthers.append(player)
        elif len(warriors) < exp_per_team:
            warriors.append(player)
    for player in not_experienced:
        if len(bandits) < tot_per_team:
            bandits.append(player)
        elif len(panthers) < tot_per_team:
            panthers.append(player)
        elif len(warriors) < tot_per_team:
            warriors.append(player)
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


def player_stats(team):
    names= [player["name"] for player in team]
    guardians=[]
    height = [player["height"] for player in team]
    for player in team:
        guardian=str(player["guardians"])
        guardians.append(guardian)
    height_avg= round(sum(height)/len(team),1)
    print(f"""
        Total players: {int(len(constants.PLAYERS) / len(constants.TEAMS))}
        Total experienced: {int(len(experienced) / len(teams))}
        Total inexperienced: {int(len(not_experienced)/ len(teams))}
        Average height: {float(height_avg)}
    """)
    print("Player names: ")
    print( "     "+", ".join(names))
    print("Guardian Names: ")  
    print( "     "+", ".join(guardians))


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