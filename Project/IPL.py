# I will fetch or retriee some meaningfull insights from the IPL dataset.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# while doing sme projects i will use some deprecated libraries functions so i want to ignore them 
import warnings
# warnings.filterwarnings("ignore")

data = pd.read_csv('C:\\Umair\\Data Visualization\\Project\\IPL.csv')
# print(data.head())

# print(data.info())
# now i come to know that this dataset donot  have any null values
# which is great for me

# print(data.shape) # (74, 20)
# print(data.describe())

# print(data.isnull().sum()) # it gives the count of the null values in each column

# ----------------------------------------------------------------------------------------
# which team won the most number of matches in IPL 2022
team_wins = data['match_winner'].value_counts()
# print(team_wins)
# sns.barplot(y=team_wins.index, x=team_wins.values, palette='viridis')
# plt.title('Number of Matches Won by Each Team in IPL 2022')
# plt.xlabel('Number of Matches Won')
# plt.ylabel('Teams')
# plt.show()

# ----------------------------------------------------------------------------------------
# Toss Dicision trends
toss_decision = data['toss_decision'].value_counts()
# print(toss_decision)
# sns.countplot(x='toss_decision', data=data, palette='Set2')
# plt.title('Toss Decision Trends in IPL 2022')
# plt.xlabel('Toss Decision')
# plt.ylabel('Count')
# plt.show()

# ----------------------------------------------------------------------------------------
# Toss winner vs Match winner
toss_winner_vs_match_winner = data[data['match_winner'] == data['toss_winner']]
# print(toss_winner_vs_match_winner['toss_winner', 'match_winner'])
# print(f'Number of times Toss Winner also won the Match: {toss_winner_vs_match_winner.shape[0]} out of {data.shape[0]} matches')
percentage = (toss_winner_vs_match_winner.shape[0] / data.shape[0]) * 100
# print(f'Percentage of times Toss Winner also won the Match: {percentage:.2f}%')

# ----------------------------------------------------------------------------------------
# How do team wins? (Runs or Wickets)
team_wins_by_runs = data['won_by'] 
# print(team_wins_by_runs)
# sns.countplot(x=team_wins_by_runs, data=data, palette='Set3')
# plt.title('How Teams Win Matches in IPL 2022')
# plt.xlabel('Method of Winning (By Runs or By Wickets)')
# plt.ylabel('Number of Matches')
# plt.show()

# ----------------------------------------------------------------------------------------
# Most "Player of the Match" awards
player_of_the_match = data['player_of_the_match'].value_counts()
# print(player_of_the_match.head(10))
# sns.barplot(y=player_of_the_match.head(10).index, x=player_of_the_match.head(10).values, palette='magma')
# plt.title('Top 10 Players with Most "Player of the Match" Awards in IPL 2022')
# plt.xlabel('Number of Awards')
# plt.ylabel('Players')
# plt.show()

# ----------------------------------------------------------------------------------------
# Top Scorer
# top_scorer = data[['top_scorer', 'highscore']]
highest_score = data.groupby('top_scorer')['highscore'].sum()
# print(highest_score.sort_values(ascending=False).head(2))
# highest_score.plot(kind='bar', color='skyblue')
# plt.show()

# ----------------------------------------------------------------------------------------
# Top 10 Best Bowling Figures
data['highest_wickets'] = data['best_bowling_figure'].apply(lambda x: x.split('--')[0]).astype(int)
# print(data[['best_bowling', 'highest_wickets']])
# print(data['highest_wickets'].sort_values(ascending=False).head(10))

top_bowlers = data.groupby('best_bowling')['highest_wickets'].sum().sort_values(ascending=False).head(10)
# print(top_bowlers)
# top_bowlers.plot(kind='bar', color='lightgreen')
# plt.show()

# ----------------------------------------------------------------------------------------
# Venue Analysis
venue_wins = data['venue'].value_counts()
# print(venue_wins)
# sns.barplot(y=venue_wins.index, x=venue_wins.values, palette='coolwarm')
# plt.title('Number of Matches Played at Each Venue in IPL 2022')
# plt.xlabel('Number of Matches')
# plt.ylabel('Venues')
# plt.show()

# ----------------------------------------------------------------------------------------
# Who won by the highest margins?
magins = data[data['won_by']=='Runs'].sort_values(by='margin', ascending=False).head(1)
# print(magins[['match_winner', 'margin', 'venue']])

# ----------------------------------------------------------------------------------------
# Which team had the highest successful run chase?


# ----------------------------------------------------------------------------------------
# which player had the highest individual score in a match?
highest_individual_score = data.sort_values(by='highscore', ascending=False).head(1)
# print(highest_individual_score[['top_scorer', 'highscore', 'match_winner', 'venue']])

# ----------------------------------------------------------------------------------------
# which bowler had the best bowling figures in a match?
# best_bowling_figure = data.sort_values(by='highest_wickets', ascending=False).head(1)
best_bowling_figure = data[data['highest_wickets'] == data['highest_wickets'].max()]
print(best_bowling_figure[['best_bowling', 'highest_wickets', 'best_bowling_figure']])



