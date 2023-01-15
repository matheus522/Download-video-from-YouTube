from  pytube import YouTube
lnk = input('Digite o link do video: ')
video = YouTube(lnk)
stream = video.streams.get_highest_resolution()
stream.download()