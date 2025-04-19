from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
import cv2
import numpy as np
from ultralytics import YOLO

app = FastAPI()
model = YOLO('./yolo12n.pt')

@app.post("/detect/")
async def detect_objects(file: UploadFile = File(...)):
    file_bytes = await file.read()
    image = cv2.imdecode(np.frombuffer(file_bytes, np.uint8), cv2.IMREAD_COLOR)
    results = model.predict(image)
    result_image = results[0].plot()
    _, img_encoded = cv2.imencode('.jpg', result_image)
    return Response(content=img_encoded.tobytes(), media_type="image/jpeg")
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

