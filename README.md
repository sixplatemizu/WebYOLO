# WebYOLO -- A Flutter YOLO Object Detection App

![Flutter](https://img.shields.io/badge/Flutter-%2302569B.svg?style=for-the-badge&logo=Flutter&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

基于Flutter和YOLOv8的跨平台目标检测应用，支持Android/iOS/Web/Windows平台。

## ✨ 功能特性
- 📸 多源图像获取：支持相册选取和相机拍摄
- 🤖 YOLOv8集成：实时目标检测与姿态识别
- 🌐 前后端分离：FastAPI后端处理检测请求
- 📱 响应式UI：适配不同屏幕尺寸
- 🖼️ 结果对比：并排显示原图与检测结果

## 📦 项目结构
```flutter_yolo_app/ ├── lib/ # Dart主代码 │ ├── main.dart # 应用入口 │ ├── services/ # 业务逻辑 │ └── widgets/ # 自定义组件 ├── assets/ # 静态资源 ├── test/ # 单元测试 ├── android/ # Android平台代码 ├── ios/ # iOS平台代码 ├── windows/ # Windows平台代码 └── backend/ # FastAPI服务端代码```


## 🚀 快速开始

### 前置要求
- Flutter SDK ≥ 3.0
- Python ≥ 3.8 (后端)
- YOLOv8权重文件

### 安装步骤
1. 克隆仓库
   `git clone https://github.com/your-repo/flutter_yolo_app.git`
   `cd flutter_yolo_app`

2. 安装Flutter依赖
   `flutter pub get`

3. 启动后端服务
   `cd backend`
   `pip install -r requirements.txt`
   `uvicorn main:app --reload`

4. 运行应用
   `flutter run -d windows`

### 🔧 技术栈
|组件|	用途|
|-|-|
|Flutter 3.x|	跨平台UI框架|
|FastAPI|	后端服务|
|YOLOv8|	目标检测模型|
|http|	API通信|

### 📄 许可证
MIT License © 2023 [Your Name]

> 💡 提示：使用前请确保已配置YOLOv8模型文件至backend/models/目录