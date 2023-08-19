import csv
import sys
import time
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np

#dictionary containing actual MVPs of last 10 seasons as {season: MVP}
actual_mvp = {
    "2022-23": "Joel Embiid",
    "2021-22": "Nikola Jokic",
    "2020-21": "Nikola Jokic",
    "2019-20": "Giannis Antetokounmpo",
    "2018-19": "Giannis Antetokounmpo",
    "2017-18": "James Harden",
    "2016-17": "Russell Westbrook",
    "2015-16": "Stephen Curry",
    "2014-15": "Stephen Curry",
    "2013-14": "Kevin Durant",
}

#list of last 10 seasons
seasons = [
    "2013-14",
    "2014-15",
    "2015-16",
    "2016-17",
    "2017-18",
    "2018-19",
    "2019-20",
    "2020-21",
    "2021-22",
    "2022-23",
]


def main():
    # print welcome message
    print("Welcome to Project: NBA!!")

    # print table of contents
    print(show_game_table())

    # take choice of activity to do
    choice = input("Enter you choice (1 or 2): ")
    while validate_choice(choice) == False:
        choice = input("Enter a valid choice between 1 and 2: ")

    # Guess the MVP game
    if choice == "1":
        # Let the user choose the season to guess the MVP
        print_table([[year] for year in seasons], ["Seasons"], "heavy_grid")
        season = input("Enter Season: ")
        while validate_season(season) == False:
            season = input("Enter a valid season: ")
        print()

        # print full stats of season leaders of that season
        print(f"Here are the stats of the season leaders of {season} season!")
        print()
        filename = season + ".csv"
        with open(filename) as f:
            reader = csv.DictReader(f)
            data = []  # stores all rows as individual dictionaries
            scores = (
                {}
            )  # stores scores of all season leaders of that season as {player_name: score}
            stats_table = []  # stores each row as indivodual list
            max_score = 0
            stat_mvp = None  # Player with the maximum calculated MVP Score

            for row in reader:
                scores[row["PLAYER"].split(",")[0]] = calc_score(
                    float(row["PTS"]),
                    int(row["GP"]),
                    float(row["RPG"]),
                    float(row["APG"]),
                    float(row["STPG"]),
                    float(row["BLKPG"]),
                    float(row["3PM"]),
                    float(row["FG%"]),
                    float(row["FT%"]),
                    float(row["MPG"]),
                    float(row["TOPG"]),
                )
                data.append({k: v for k, v in row.items()})
                stats_table.append(list(row.values())[1:])

            # find stat mvp
            for player in scores.keys():
                if scores[player] > max_score:
                    max_score = scores[player]
                    stat_mvp = player
            stats_headers = [
                heading for heading in data[0].keys() if heading != "\ufeffRK"
            ]
            time.sleep(1)
            print_table(stats_table, stats_headers, "heavy_grid")
            print()
            count = 3

            # Give 3 attempts to guess MVP
            while count != 0:
                user_mvp = get_mvp("Guess the MVP: ", scores)
                if user_mvp == actual_mvp[season]:
                    if user_mvp == stat_mvp:
                        print(f"YES! {user_mvp} was the MVP of the {season} season!")
                        time.sleep(0.5)
                        sys.exit("Thanks for playing!")
                    else:
                        print(f"YES! {user_mvp} was the MVP of the {season} season!")
                        time.sleep(0.5)
                        print(
                            f"However, purely going by the statistics, {stat_mvp} should've won it."
                        )
                        time.sleep(1)
                        sys.exit("Thanks for playing!")
                else:
                    print(f"Wrong guess! Attempts left: {count - 1}")
                    count -= 1
            print(f"Actual MVP of the {season} season was {actual_mvp[season]}")
            time.sleep(0.5)
            sys.exit("Thanks for playing!")

    # View Statistical Trends
    else:
        # print trends table
        print_table(
            [
                [1, "MVP Score of players accross 10 years."],
                [
                    2,
                    "Points Per Game and Number of Games Played of MVPs across 10 years",
                ],
            ],
            ["SNo", "Trends"],
            "heavy_grid",
        )

        # get user choice
        choice = input("Enter you choice (1 or 2): ")
        while validate_choice(choice) == False:
            choice = input("Enter a valid choice between 1 and 2: ")

        # View calculated MVP scores of all 10 MVPs
        if choice == "1":
            mvp_scores = {}  # stores mvp scores of each season as {season: score}
            for season in seasons:
                filename = season + ".csv"
                with open(filename) as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        if row["PLAYER"].split(",")[0] == actual_mvp[season]:
                            mvp_scores[season] = calc_score(
                                float(row["PTS"]),
                                int(row["GP"]),
                                float(row["RPG"]),
                                float(row["APG"]),
                                float(row["STPG"]),
                                float(row["BLKPG"]),
                                float(row["3PM"]),
                                float(row["FG%"]),
                                float(row["FT%"]),
                                float(row["MPG"]),
                                float(row["TOPG"]),
                            )
                            break

            # plot a line graph
            plt.plot(list(mvp_scores.keys()), list(mvp_scores.values()), c="r", lw=3)
            plt.xlabel("Seasons")
            plt.ylabel("MVP Scores")
            plt.title("Highest Statistical Scores per season.")
            plt.show()

        # a bar graph showing GP and PPG simulataneously of last 10 MVPs
        else:
            ppg = []  # stores Points Per Game of last 10 MVPs
            gp = []  # stores Number of Games Played of last 10 MVPs

            # load values into the ppg and gp list
            for season in seasons:
                filename = season + ".csv"
                with open(filename) as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        if row["PLAYER"].split(",")[0] == actual_mvp[season]:
                            ppg.append(float(row["PTS"]))
                            gp.append(int(row["GP"]))
                            break

            x = np.arange(len(seasons))
            width = 0.4  # width of a rectangle bar

            # Plot bar chart
            fig, ax = plt.subplots()
            rect1 = ax.bar(x - width / 2, ppg, width, label="PPG (Points Per Game)")
            rect2 = ax.bar(x + width / 2, gp, width, label="GP (Games Played)")

            # text in grouped bar chart
            for bar in ax.patches:
                value = bar.get_height()
                text = f"{value}"
                text_x = bar.get_x() + bar.get_width() / 2
                text_y = bar.get_y() + value
                ax.text(text_x, text_y, text, ha="center", color="r", size=12)

            # Add some text for labels,x-axis tick labels
            ax.set_ylabel("PTS averages and GP numbers")
            ax.set_xlabel("Seasons")
            ax.set_xticks(x)
            ax.set_xticklabels(seasons)
            ax.legend()
            plt.title("PPG and GP of last 10 MVPs")
            plt.show()


def calc_score(PPG, GP, RPG, APG, SPG, BPG, _3PM, FG, FT, MPG, TOV):
    """
    Calculate the MVP score according to the below formula, given the above parameters
    Multiplying factors of each parameter show the importance of the specific parameter in determining the MVP statistically
    """
    return (
        (0.5 * PPG)
        + (0.5 * GP)
        + (0.2 * RPG)
        + (0.15 * APG)
        + (0.1 * SPG)
        + (0.05 * BPG)
        + (0.05 * _3PM)
        + (0.04 * (FG / 100))
        + (0.04 * (FT / 100))
        + (0.03 * (MPG / 48))
        - (0.02 * TOV)
    )


def validate_season(season):
    """
    returns true if the parameter is in the global seasons list, else, returns false  
    """
    return season in seasons


def validate_choice(choice):
    """
    returns true if choice is valid (i.e. either 1 or 2), else, false
    """
    return choice in ["1", "2"]


def print_table(table, headers, fmt):
    """
    prints table
    """
    print(tabulate(table, headers, tablefmt=fmt))


def show_game_table(
    table=[[1, "Guess The MVP"], [2, "NBA Statistical Trends"]],
    headers=["SNo", "Choice"],
):
    """
    returns a table via tabulate as per the parameters
    """
    return tabulate(table, headers, tablefmt="heavy_grid")


def get_mvp(phrase, scores):
    """
    Takes a phrase and a dictionary containing the calculated MVP score of each season leader of a particular season.
    Gets user input and validates the input.
    """
    mvp = input(phrase).title()
    while mvp not in scores.keys():
        print("MVP can only be someone from the above Season Leaders.")
        mvp = input(phrase)
    return mvp


if __name__ == "__main__":
    main()
