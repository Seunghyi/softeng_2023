import os

from fastapi import FastAPI, HTTPException, Query
from pytube import YouTube

app = FastAPI()
DOWNLOADS_FOLDER = "homework15/downloads"

@app.get("/")
def read_root():
    return {"Hello": "음원 다운로드"}


@app.get("/get_youtube_audio")
async def get_youtube_audio(video_url: str = Query(..., description="YouTube video URL")):
    try:
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        # audio_stream.file_extensipon = 'mp3'
        video_title = yt.title
        filename = f"{video_title}.mp3"

        download_path = os.path.join(DOWNLOADS_FOLDER, filename)
        audio_stream.download(output_path=DOWNLOADS_FOLDER, filename=filename)
        return {"status": "success", "message": f"{video_title} 다운로드 성공"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))