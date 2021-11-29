import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as mticker


music = pd.read_csv("elismusic.csv")

best_songs = music.sort_values(by=["Plays"], ascending=False)

x = best_songs.Name[:50]
x = x[::-1]
y = best_songs.Plays[:50]
y = y[::-1]


plt.style.use("seaborn")
fig, ax = plt.subplots(figsize=(16, 9))

ax.barh(x, y)

ax.set_title("My most listened to songs", fontsize=20)
ax.set_xlabel("Song title", fontsize=16)
ax.set_ylabel("Times listened", fontsize=16)

fig.autofmt_xdate()

ax.tick_params(axis="x", which="major", labelsize=15)

ticks_loc = ax.get_yticks()
ax.yaxis.set_major_locator(mticker.FixedLocator(ticks_loc))

ax.set_yticklabels(x, fontsize=8)

plt.show()







