from sklearn.neighbors import KNeighborsClassifier
import cv2
import pickle
import numpy as np
from mtcnn import MTCNN
from datetime import datetime
import os

def mark_attendance():
    detector = MTCNN()
    video = cv2.VideoCapture(0)
    
    # Load trained data
    try:
        with open("Data/names.pkl", "rb") as f:
            LABELS = pickle.load(f)
        with open("Data/faces_data.pkl", "rb") as f:
            FACES = pickle.load(f)
    except FileNotFoundError:
        print("No training data found. Please add students first.")
        return
    
    if len(FACES) == 0 or len(LABELS) == 0:
        print("No training data available.")
        return
    
    # Train KNN classifier
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(FACES, LABELS)
    
    # Prepare attendance file
    date = datetime.now().strftime("%Y-%m-%d")
    filename = f"Data/Attendance_{date}.csv"
    
    # Create file if it doesn't exist
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write("Name,Time\n")
    
    recognized_names = set()
    
    print("Starting attendance marking. Press 'q' to quit...")
    
    while True:
        ret, frame = video.read()
        if not ret:
            break
        
        # Detect faces
        results = detector.detect_faces(frame)
        for result in results:
            x, y, w, h = result['box']
            # Fix negative coordinates
            x, y = max(0, x), max(0, y)
            crop_img = frame[y:y+h, x:x+w]
            
            try:
                resized_img = cv2.resize(crop_img, (50, 50))
                flattened = resized_img.flatten().reshape(1, -1)
                
                # Predict
                prediction = knn.predict(flattened)
                confidence = np.max(knn.predict_proba(flattened))
                
                # Only consider predictions with high confidence
                if confidence > 0.9:
                    name = prediction[0]
                    cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
                    
                    # Record attendance if not already done
                    if name not in recognized_names:
                        recognized_names.add(name)
                        timestamp = datetime.now().strftime("%H:%M:%S")
                        with open(filename, 'a') as f:
                            f.write(f"{name},{timestamp}\n")
                        print(f"Marked attendance for {name} at {timestamp}")
            except:
                continue
            
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
        
        cv2.imshow("Attendance System", frame)
        if cv2.waitKey(1) == ord('q'):
            break
    
    video.release()
    cv2.destroyAllWindows()
    print("Attendance marking completed.")

if __name__ == "__main__":
    mark_attendance()