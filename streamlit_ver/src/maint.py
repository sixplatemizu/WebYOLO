from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
import cv2
import numpy as np
from ultralytics import YOLO

app = FastAPI()
# 加载支持姿态检测的模型
model = YOLO('yolo11n-pose.pt')  # 关键修改：必须用-pose后缀模型

@app.post("/detect/")
async def detect_objects(file: UploadFile = File(...)):
    file_bytes = await file.read()
    image = cv2.imdecode(np.frombuffer(file_bytes, np.uint8), cv2.IMREAD_COLOR)
    
    # 执行检测（自动同时输出检测框和姿态关键点）
    results = model.predict(image)
    
    # 绘制结果（包含检测框+骨骼关键点）
    result_image = results[0].plot()  # 自动合并两种结果
    
    _, img_encoded = cv2.imencode('.jpg', result_image)
    return Response(content=img_encoded.tobytes(), media_type="image/jpeg")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)