from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from ultralytics import YOLO
import cv2
import numpy as np
import tempfile
app = FastAPI()
model = YOLO("yolo12n.pt")  # 使用yolo12模型

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    try:
        # 读取图片
        image = cv2.imdecode(np.frombuffer(await file.read(), np.uint8), cv2.IMREAD_COLOR)

        # 使用YOLO进行目标检测
        results = model(image)

        # 创建一个临时文件来保存处理后的图片
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
            output_path = temp_file.name
        results[0].save(filename=output_path)

        return JSONResponse(content={"output_path": output_path})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)