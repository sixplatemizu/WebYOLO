from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from ultralytics import YOLO
import cv2
import numpy as np
import tempfile
import os

app = FastAPI()
model = YOLO("yolo11n-pose.pt")  # Using YOLOv8n-pose model
@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    try:
        # Read image
        image = cv2.imdecode(np.frombuffer(await file.read(), np.uint8), cv2.IMREAD_COLOR)

        # Run YOLO pose estimation
        results = model(image)

        # Create a temporary file to save the processed image
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
            output_path = temp_file.name
        results[0].save(filename=output_path)

        # Get keypoints data (optional: send to frontend)
        keypoints = results[0].keypoints.data.tolist() if results[0].keypoints is not None else []
        return JSONResponse(content={
            "output_path": output_path,
            "keypoints": keypoints  # Optional: send pose data
        })
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)