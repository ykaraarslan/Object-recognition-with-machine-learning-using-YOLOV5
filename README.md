# Object recognition with machine learning using YOLOV5

## Overview
This project aims to recognise products in images using the YOLOv5 object detection algorithm. When it recognises these products, it transfers the type, data and time of the product to the database. Here, a counter is added so that there is no continuous data flow every time it recognises. At the same time, it performs object recognition above a certain accuracy margin. 

## Installation

### Clone YOLOv5 Repository
First, clone the official YOLOv5 repository from GitHub:

```bash
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
![resim1](https://github.com/user-attachments/assets/642e0da9-ca8d-498d-b520-0f3f3dee7db5)
![train_batch1](https://github.com/user-attachments/assets/d0f3dcb1-2012-4c21-8df9-7a7f516a2741)
