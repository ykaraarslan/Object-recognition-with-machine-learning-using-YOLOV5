# Object recognition with machine learning using YOLOV5
##
![train_batch1](https://github.com/user-attachments/assets/9c2d4626-b6bd-4845-b1ea-10a03885caeb)
![val_batch0_pred](https://github.com/user-attachments/assets/f1265267-c1d6-46c9-975b-f02d301a9e8b)


## Overview
This project aims to recognise products in images using the YOLOv5 object detection algorithm. When it recognises these products, it transfers the type, data and time of the product to the database. Here, a counter is added so that there is no continuous data flow every time it recognises. At the same time, it performs object recognition above a certain accuracy margin. 

## Installation

### Clone YOLOv5 Repository
First, clone the official YOLOv5 repository from GitHub:

```bash
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt

