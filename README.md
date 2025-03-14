## **AI Surveillance System**
🚀 **Real-time Object Detection using YOLOv5**

### **Overview**
The **AI Surveillance System** is a real-time object detection application built using **YOLOv5**. This system can analyze live video feeds and uploaded media for object detection, making it useful for surveillance, security, and automated monitoring.

### **Features**
✅ Real-time object detection using YOLOv5  
✅ Supports video stream processing  
✅ Ability to analyze uploaded media files  
✅ Built with Python and integrates with deep learning frameworks  
✅ Lightweight and efficient for real-world surveillance applications  

### **Project Structure**
```
AI_Surveillance_System/
│── yolov5/                      # YOLOv5 model files
│── __pycache__/                  # Cached Python files
│── app.py                        # Main application script
│── realtime_detection.py         # Script for real-time video detection
│── upload_media_analysis.py      # Script for analyzing uploaded media
│── yolov5m.pt                    # Pretrained YOLOv5 model
│── README.md                     # Project documentation
```

### **Installation**
1️⃣ **Clone the repository**
```bash
git clone https://github.com/yourusername/AI_Surveillance_System.git
cd AI_Surveillance_System
```

2️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```

3️⃣ **Download YOLOv5 model weights**  
Ensure you have the `yolov5m.pt` model file. If missing, download it from the official YOLOv5 repository:
```bash
wget https://github.com/ultralytics/yolov5/releases/download/v6.0/yolov5m.pt
```

4️⃣ **Run the real-time detection**
```bash
python realtime_detection.py
```

5️⃣ **Run the media analysis script**
```bash
python upload_media_analysis.py --source path/to/image_or_video
```

### **Usage**
- Run `app.py` to start the main application.
- For real-time video detection, use `realtime_detection.py`.
- To analyze an uploaded image/video, use `upload_media_analysis.py`.

### **Dependencies**
- Python 3.8+
- OpenCV
- PyTorch
- YOLOv5
- Flask (if using a web-based interface)

### **Contributing**
🚀 Contributions are welcome!  
If you find a bug or want to add features, feel free to open an issue or a pull request.

### **License**
📜 This project is licensed under the MIT License.


