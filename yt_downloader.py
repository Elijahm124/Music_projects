from selenium import webdriver
import time


import os
import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    "nocheckcertificate": True,
    "ignoreerrors": True,
    "ffmpeg_location": "/Users/elijahmurillo/PycharmProjects/Music_projects/ffmpeg"
}

url = "https://www.youtube.com/playlist?list=PLMUEO0ZXe36uSrVHXDU1UQK8UpnEHqqOx"
driver = webdriver.Chrome(executable_path="/Users/elijahmurillo/PycharmProjects/Music_projects/chromedriver-2")
driver.get(url)
time.sleep(5)

playlist = []
videos = driver.find_elements_by_class_name('style-scope ytd-playlist-video-renderer')
print(len(videos))

for video in videos:
    link = video.find_element_by_id('video-title').get_attribute("href")
    end = link.find("&")
    link = link[:end]
    playlist.append(link)
    print(link)

os.chdir('/Users/elijahmurillo/Downloads')
print(len(playlist))

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    for link in playlist:
        print(link)
        ydl.download([link])
driver.quit()
