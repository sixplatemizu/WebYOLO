from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import cv2
import os
from datetime import datetime
from ultralytics import YOLO

app = FastAPI()

# 加载YOLOv8模型（会自动下载yolov8n.pt）
model = YOLO('./yolov8n.pt')  # 可选: yolov8s.pt, yolov8m.pt等
@app.post("/detect/")
async def detect_objects(file: UploadFile = File(...)):
    # 保存上传的临时文件
    temp_file = f"temp_{datetime.now().timestamp()}.jpg"
    with open(temp_file, "wb") as buffer:
        buffer.write(await file.read())
    
    # 执行目标检测
    results = model.predict(temp_file)
    
    # 保存结果图像
    output_file = f"result_{datetime.now().timestamp()}.jpg"
    results[0].save(filename=output_file)
    # 清理临时文件
    os.remove(temp_file)
    
    return FileResponse(output_file)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

