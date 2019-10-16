from pytube import YouTube

SAVE_PATH = "E:/" #save video here

link="https://www.youtube.com/watch?v=rNvbCx0dFiA"  #to be downloaded
yt = YouTube(link)
stream = yt.streams.first()
stream.download()
print('Download Completed!') 

