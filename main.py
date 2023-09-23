import ffmpeg
from pytube import YouTube
import asyncio
import os
import re

link = str(input("Enter the URL of the video you want to download: \n>> "))

video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", link)
if video_id_match:
    video_id = video_id_match.group(1)
    yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")
else:
    print("Invalid YouTube URL")
    exit()

video = yt.streams.filter(only_audio=True).first()

destination = "download"
out_file = video.download(output_path=destination)

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

print(yt.title + " has been successfully downloaded.")


async def rootfunc(path, title):
    speed = 1.5
    input_file = path
    speed_folder = "speed"
    os.makedirs(speed_folder, exist_ok=True)
    output_file = os.path.join(speed_folder, f'{title}.mp3')

    input_audio = ffmpeg.input(input_file)
    output_audio = ffmpeg.output(
        input_audio, output_file, filter_complex=f'atempo={speed}')
    print("priting output_audio: ", output_audio)
    ffmpeg.run(output_audio)

    print(f"Playback speed changed and saved to {output_file}")

asyncio.run(rootfunc(new_file, yt.title))
