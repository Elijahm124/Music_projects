import pandas as pd
from plotly import express as px
from plotly import offline

music = pd.read_csv("elismusic.csv")
df = pd.DataFrame()

artists = music.groupby(["Artist"], as_index=False).sum()
plays_by_artist = artists.sort_values(by="Plays", ascending=False)

top_25 = plays_by_artist["Artist"][:25]

lst, labels = [], []

for i in list(top_25):
    for index, row in music.iterrows():
        if row["Artist"] == i:
            lst.append(row)
            labels.append(f"Song: {row['Name']}<br />Album: {row['Album']}"
                          f"<br />Genre: {row['Genre']}")

labels = labels[::-1]
lst = lst[::-1]

data = px.bar(lst, x="Plays", y="Artist", orientation="h", hover_name=labels, title="Elijah's Favorite Artists")



fig = {"data": data}

offline.plot(fig, filename="top_artists.html")
