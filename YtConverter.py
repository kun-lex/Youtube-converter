from pytube import YouTube
import os

yt = YouTube(input("Paste link url: \n>>"))

video = yt.streams.filter(only_audio=True).first()

destination = "/User/Hp/desktop"

out_file = video.download(output_path=destination)

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

print(yt.title + "Saved")