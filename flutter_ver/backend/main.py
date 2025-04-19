from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from ultralytics import YOLO
import cv2
import numpy as np
import tempfile
import os

app = FastAPI()
models = {
    "object": YOLO("yolo11n.pt"),
    "pose": YOLO("yolo11n-pose.pt")
}
@app.post("/detect")
async def detect(
    file: UploadFile = File(...),
    mode: str = Form("object")
):
    try:
        if mode not in models:
            return JSONResponse(
                content={"error": "Invalid mode. Use 'object' or 'pose'"},
                status_code=400
            )
        image = cv2.imdecode(np.frombuffer(await file.read(), np.uint8), cv2.IMREAD_COLOR)

        results = models[mode](image)

        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
            output_path = temp_file.name
        results[0].save(filename=output_path)

        response = {"output_path": output_path}
        if mode == "pose" and results[0].keypoints is not None:
            response["keypoints"] = results[0].keypoints.data.tolist()

        return JSONResponse(content=response)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)