from pydub import AudioSegment
from pydub import effects
from pytube import YouTube
import asyncio
import os


async def rootfunc(title):
    print("in func")
    await asyncio.sleep(5)
    root = os.path.abspath(title)
    speed = 1.5
    audio = AudioSegment.from_file(root, format="mp3")
    so = audio.speedup(playback_speed=speed)

    final = root[:-4] + '_Out.mp3'
    so.export(final, format='mp3')

    print(final + " has been successfully downloaded.")
link = str(input("Enter the URL of the video you want to download: \n>> "))

if "?feature=shared" in link:
    link = link[:len(link)-15]
yt = YouTube(link)
video = yt.streams.filter(only_audio=True).first()

destination = "download"
out_file = video.download(output_path=destination)

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

print(yt.title + " has been successfully downloaded.")


asyncio.run(rootfunc(yt.title))
