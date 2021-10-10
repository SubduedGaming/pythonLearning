#sources
from pytube import YouTube

for i in range(1000000):
    link = input("Please paste your link now: ")
    yt = YouTube(link)
    #Title
    print("Title: ", yt.title)
    #Views
    print("Total Views: ", yt.views)
    #Length
    print("Length: ", yt.length)
    #print streams
    print("Streams: ", yt.streams)
    ys = yt.streams.get_audio_only()
    ys.download()


