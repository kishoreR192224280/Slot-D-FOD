import pandas as pd
import matplotlib.pyplot as plt
data="Players.csv"
df = pd.read_csv(data)
top_goal_scorers = df.nlargest(5, "Goals")
print("Top 5 players with the highest number of goals scored:")
print(top_goal_scorers)
top_earners = df.nlargest(5, "Salary")
print("\nTop 5 players with the highest salaries:")
print(top_earners)
average_age = df["Age"].mean()
players_above_average_age = df[df["Age"] > average_age]
print("\nPlayers who are above the average age:")
print(players_above_average_age)
position_counts = df["Position"].value_counts()
position_counts.plot(kind="bar",color="cyan",alpha=0.7)
plt.show()
