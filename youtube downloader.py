#sources
from pytube import YouTube

link = input("What is the Youtube link? ")
yt = YouTube(link)

#Title
print("Title: ", yt.title)
#Views
print("Total Views: ", yt.views)
#Length
print("Length: ", yt.length)
#print streams
print("Streams: ", yt.streams)
ys = yt.streams.get_highest_resolution()

ys.download()
