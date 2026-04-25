# Teddy Rodd
# Lab 9
# World Series Winners

def main():
    file = open("WorldSeriesWinners.txt", "r")

    team_wins = {}
    year_winner = {}

    start_year = 1903

    for line in file:
        team = line.strip()
            
        # Store year -> team
        year_winner[start_year] = team

        # Count wins
        if team in team_wins:
            team_wins[team] = team_wins[team] + 1
        else:
            team_wins[team] = 1

        start_year = start_year + 1

    file.close()

    # Uncomment this to show table... switch "year_winner" to tem_wins to show other table version...
    #for key, value in year_winner.items():
        #print(f"{key}: {value}")

    # Ask user for a year
    year = int(input("Enter a year between 1903 and 2009: "))

    # Output result
    if year in year_winner:
        team = year_winner[year]
        print("Winner:", team)
        print("Total wins:", team_wins[team])
    else:
        print("No World Series played that year.")



if __name__ == "__main__":
    main()