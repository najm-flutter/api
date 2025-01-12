from fastapi import FastAPI, HTTPException
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()

# نموذج الإدخال

@app.get("/get-captions/")
async def get_captions(vd: str):
    print(vd)
    try:
        # استخراج النصوص من الفيديو
        transcript = YouTubeTranscriptApi.list_transcripts(vd).find_generated_transcript(["ar", "en"]).fetch()
        return {"status": "success", "captions": transcript}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
