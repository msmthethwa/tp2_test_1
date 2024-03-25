#Write a program that will load the “football.csv” dataset into a dataframe called “foot_ball”.
import pandas as pd 

foot_ball = pd.read_csv("C:/Users/CC/Downloads/dataset - 2020-09-24.csv")
print(foot_ball.head())

#inspect the dataframe by listing and displaying the last 7 rows of the dataframe using a single python statement.
print("\nDisplaying the last 7 rows of the dataframe \n",foot_ball.head(-7))

#Access and display the "Nationality" and "Club" columns for the first all players.
print("\n\nAccessing 'Nationality' and 'Club' columns:\n")
print(foot_ball[['Nationality', 'Club']].head())

#Access and display the data for the tenth player in the dataset using row index.
print("\nData for the tenth player:\n")
print(foot_ball.iloc[[9]])

#Access and display the "Goals" and "Appearances" for players with index positions 100 to 110
print("\n\"Goals\" and \"Appearances\" for players 100 to 110:\n")
print(foot_ball.loc[range(100, 110), ['Goals','Appearances']])

#Adding a new column "Goals per Appearance".
foot_ball["Goals per Appearance"]= foot_ball['Goals'] / foot_ball['Appearances']
print("\nFirst 5 Rows of Updated Dataset:\n")
print(foot_ball.head(5))

#Selecting players from Arsenal club.
arsenal_players = foot_ball[foot_ball['Club'] == 'Arsenal']
print("\nPlayers from Arsenal Club:\n")
print(arsenal_players.head())

#Filtering out players who have scored more than 5 goals.
high_scorers = foot_ball[foot_ball['Goals'] >  5]
print("\nPlayers who have scored over 5 Goals:\n")
print(high_scorers.head())

#Upgrading pandas module.

#pip install --upgrade pandas
