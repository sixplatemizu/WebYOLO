from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import Response
import cv2
import numpy as np
from ultralytics import YOLO

app = FastAPI()
# 加载两种模型
detection_model = YOLO('models/yolo11n.pt')  # 常规目标检测模型
pose_model = YOLO('models/yolo11n-pose.pt')  # 姿态检测模型

@app.post("/detect/")
async def detect_objects(
    file: UploadFile = File(...),
    mode: str = Form("detection")  # 接收模式参数
):
    file_bytes = await file.read()
    image = cv2.imdecode(np.frombuffer(file_bytes, np.uint8), cv2.IMREAD_COLOR)
    
    # 根据模式选择模型
    if mode == "pose":
        results = pose_model.predict(image)
    else:
        results = detection_model.predict(image)
    
    # 绘制结果
    result_image = results[0].plot()
    
    _, img_encoded = cv2.imencode('.jpg', result_image)
    return Response(content=img_encoded.tobytes(), media_type="image/jpeg")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)