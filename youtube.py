from yt_dlp import YoutubeDL
from pydub import AudioSegment
import os

def download_youtube_audio_as_mp3(youtube_urls, output_path="./songs"):
    # Crear la carpeta de salida si no existe
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    for youtube_url in youtube_urls:
        try:
            # Descargar el audio del video usando yt-dlp
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([youtube_url])
            
            print(f"Audio descargado y convertido a MP3: {youtube_url}")
        except Exception as e:
            print(f"Ocurrió un error con el enlace {youtube_url}: {e}")

# Ejemplo de uso
links = [
    ""               
]
download_youtube_audio_as_mp3(links) 