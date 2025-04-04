import os
from yt_dlp import YoutubeDL

def download_audio(video_url, output_path="."):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Audio downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Input YouTube video URL
video_url = input("Enter the YouTube video URL: ").strip()
download_audio(video_url)
