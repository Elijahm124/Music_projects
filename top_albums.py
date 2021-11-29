import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

music = pd.read_csv("elismusic.csv")

albums = music.groupby(["Album", "Artist"], as_index=False).sum()
plays = albums.sort_values(by="Plays", ascending=False)

top_albums = plays.Album[:10]
top_plays = plays.Plays[:10]
top_artists = plays.Artist[:10]


plt.style.use("seaborn")

fig, ax = plt.subplots()

ax.set_title("My Top Albums", fontsize=20)
ax.set_xlabel("Albums", fontsize=12)
ax.set_ylabel("Plays", fontsize=12)

ax.set_xticks([i for i in range(len(top_albums))])
ticks_loc = ax.get_xticks()
ax.xaxis.set_major_locator(mticker.FixedLocator(ticks_loc))
ax.set_xticklabels(top_albums)
fig.autofmt_xdate()

plt.bar(top_albums, top_plays)

plt.show()
