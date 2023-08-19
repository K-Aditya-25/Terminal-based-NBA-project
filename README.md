# Terminal-based-NBA-project
This project contains a GUESS THE MVP  game and contains an option to view the statistical trends of the last 10 MVPs in the NBA
PROJECT NBA
#### Video Demo:  https://youtu.be/pXmzOgjLVjg
#### Description:
This project is made for NBA enthusiasts and contains 2 activities:
    1. Guess The MVP
    2. Visualise NBA statistical trends
The program starts with printing the above 2 choices in a table using tabulate, and prompts the user to enter a choice between "1" and "2". Any other choices will be considered invalid and the user will be prompted to enter the choice again.

1. Guess The MVP
    After entering "1" as the choice above, the user will be shown a table of the last ten NBA seasons. (eg: 2022-23) The user will have to enter the season of his choice Any invalid season choice will lead to the season choice being asked again.

    After entering the season, a table of the stats of the 10 season leaders of that particular season will be displayes to the user. The stats will consist of:
        GP, (Games Played)
        MPG, (Minutes Per Game)
        FG%, (Field Goal %)
        FT%, (Free Throw %)
        3PM, (3 Pointers Made)
        RPG, (Rebounds Per Game)
        APG, (Assists Per Game)
        STPG, (Steals Per Game)
        BLKPG, (Blocks Per Game)
        TOPG, (TurnOvers Per Game)
        PTS, (Points Per Game)
    These stats have been imported from the official ESPN website: https://www.espn.com/nba/seasonleaders/_/league/nba
    Data cleaning has been performed by running various python scripts on the csv files.

    The user gets 3 chances to intelligently guess the MVP based on the shown stats of the seasons leaders. Invalid guesses will lead to the prompt being asked again and again.

    A) calc_score function
        This function calculates the MVP score of all the season leaders of a chosen season as per the following formula:
        Score = (0.5 * PPG) + (0.5 * GP) + (0.2 * RPG) + (0.15 * APG) + (0.1 * SPG) + (0.05 * BPG) + (0.05 * 3PM) + (0.04 * (FG% / 100)) + (0.04 * (FT% / 100)) + (0.03 * (MPG / 48)) - (0.02 * TOV)

        The multiplying factor of each parameter has been decided according to the priority of that parameter in deciding the MVP.
        Two factors that are important in determining the MVP that haven't been taken into account because they're tough to quantify:
            1. Team Record over the season
            2. Media Narrative of the player for that season
        Hence, this formula declares the MVP based purely on the highest statistical score from the formula.

2. Visualise NBA statistical trends

    After entering choice "2", the user is shown a table of two further choices:
        1. MVP Score of players accross 10 years.
        2. Points Per Game and Number of Games Played of MVPs across 10 years
    The user is prompted to enter a choice between "1" and "2"

    A) Choice "1":
        This shows a line graph plotted with matplotlib.pyplot.plot() function. X axis has the 10 seasons. Y axis plots the statistical scores (calculated using the calc_score() function) of the actual MVPs of the various seasons.

    B) Choice "2":
        This plots a grouped bar graph using matplotlib.pyplot.bar() function. X axis has the 10 seasons. Y axis contains the number of games played (orange bar) and points per game (blue bar) side to side.

Libraries and Modules Used:
    1. sys
    2. time
    3. numpy
    4. matplotlib
    5. tabulate
    6. pytest (for unit tests)

Functions implemented:
    1. calc_score
        calculates and returns the MVP score of a player given its stats
    2. validate_season
        returns true if the season, passed as an argument, is among the last 10 seasons, else, returns false
    3. validate_choice
        returns true if the choice, passed as argument, is among ["1","2"]. else, returns false
    4. print_table
        a custom function that takes a table list, a headers list and a table format string as arguments and prints the table using tabulate
    5. show_game_table
        returns a table using tabulate
    6. get_mvp
        prompts user for entering their guess for the MVP. Keeps prompting the user for the MVP guess if their guess isn't someone among the Season Leaders

Unit Test file:
    uses pytest library and contains 5 functions to test the above functions implemented. all tests must pass inorder for the project to work.
