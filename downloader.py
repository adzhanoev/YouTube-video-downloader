from youtube_dl import YoutubeDL as yt

def download(link):
    ydl_opts = {"outtmpl": "C:\\Users\\HP\\Downloads\\vids\\%(title)s.%(ext)s", "quiet": True}

    with yt(ydl_opts) as ydl:
        ydl.download([str(link)])


videos = list()
video = ""
while video.lower() != "c":
	video = input("Paste link here (enter \"c\" to exit): ")
	videos.append(video)

try:
	videos.remove("c")
except:
	videos.remove("C")

print()
for link in videos:
   try:
   	download(link)
   except:
   	print("Failed to download " + link)
   print("Downloaded " + link)
