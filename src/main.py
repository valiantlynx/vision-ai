from fastapi import FastAPI, WebSocket
from typing import Union
from video_stream import VideoStream
from object_detection import ObjectDetection
import asyncio

app = FastAPI()

od = ObjectDetection()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    video_stream = VideoStream(od)
    while True:
        data = await websocket.receive_text()
        # Process frame and get detection results
        result = video_stream.process_frame(data)
        await websocket.send_text(result)
