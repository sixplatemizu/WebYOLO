# Flutter YOLO Object Detection App

## Overview
This Flutter application integrates YOLOv8 object detection capabilities, allowing users to upload images and receive detection results. The app features a clean UI with Material Design components and communicates with a FastAPI backend for processing.

## Features
- **Image Upload**: Select images from device gallery or camera.
- **Object Detection**: Send images to backend for YOLOv8 processing.
- **Result Display**: Show original and processed images with detection boxes.
- **Cross-Platform**: Runs on Android, iOS, and desktop (via Flutter).

## Project Structure
`flutter_yolo_app/ ├── lib/ │ ├── main.dart # Application entry point │ └── image_picker.dart # Image handling logic ├── assets/ │ └── icon/ # App icon resources ├── test/ # Unit tests ├── android/ # Android platform code ├── ios/ # iOS platform code ├── windows/ # Windows platform code ├── pubspec.yaml # Dependency management └── CMakeLists.txt # Native build configuration`


## Dependencies
- **http**: ^0.13.3 (API communication)
- **image_picker**: ^0.8.4+4 (Image selection)
- **cached_network_image**: ^3.2.0 (Image caching)

## Setup Instructions
1. Ensure Flutter SDK is installed (`flutter doctor`)
2. Clone repository:
   ```bash
   git clone [repository_url]
   cd flutter_yolo_app```
3. Install dependencies:
flutter pub get
4. Run the app:
flutter run

## Backend Requirements
The app requires a running FastAPI server with:

- YOLOv8 model endpoint at /detect
- Accepts POST requests with image data
- Returns JSON with detection results

## Known Limitations
- Currently ignores lib/main.dart and iOS project file during migrations (see .metadata)
- Desktop support requires additional Flutter configuration

## Contribution
For feature requests or bug reports, please open an issue in the project repository.