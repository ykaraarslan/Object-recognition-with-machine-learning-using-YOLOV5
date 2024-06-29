import torch
import time
import cv2
import firebase_admin
from firebase_admin import credentials, firestore
import pathlib
from datetime import datetime

temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

credentialData = credentials.Certificate("proje.json") #you should use your own json file
firebase_admin.initialize_app(credentialData)
firestoreDb = firestore.client()

model = torch.hub.load('ultralytics/yolov5', 'custom', path="sondenemeler.pt") # you should use your own best.pt file

object_timers = {}

timeout_duration = 5 # 5 seconds

type_values = {
    "kahve": 0,
    "pepsi": 1,
    "makarna": 2,
    "sut": 3,
    "madensuyu": 4,
    "cips": 5,
    "domestos": 6,
    "karam": 7,
    
} #If you do not want to send the type value, do not use this place, if you want, change it according to yourself.

def main():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    
    while True:
        
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        
        
        results = model(frame)
        
        
        for det in results.xyxy[0]:
            if det[4] >= 0.65:
                cv2.rectangle(frame, (int(det[0]), int(det[1])), (int(det[2]), int(det[3])), (0, 255, 0), 2)
                cv2.putText(frame, f'{results.names[int(det[5])]} {det[4]:.2f}', 
                    (int(det[0]), int(det[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                    0.9, (36, 255, 12), 2)
                class_name = results.names[int(det[5])]  
                
                
                if class_name not in object_timers or time.time() - object_timers[class_name] > timeout_duration:
                    
                    current_time = datetime.now().strftime('%d.%m.%y : %H.%M')
                    
                    
                    type_value = type_values.get(class_name, 0)  
                    
                    
                    firestoreDb.collection(u'yolov5Collection').add({
                        'type': type_value,
                        'data': class_name,
                        'time': current_time
                    })
                    print(f'{class_name} detected at {current_time} with type {type_value}')
                    
                    
                    object_timers[class_name] = time.time()
        
        
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1) == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()