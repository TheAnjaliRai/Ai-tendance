import cv2
import pickle
import numpy as np
import os
import sys
from mtcnn import MTCNN
import time

def add_face(name):
    detector = MTCNN()
    video = cv2.VideoCapture(0)  # Initialize the camera

    if not video.isOpened():
        print("Error: Unable to access the camera.")
        return False

    faces_data = []
    sample_count = 5  # Number of samples to collect
    collected_samples = 0

    print(f"Collecting samples for {name}. Please look at the camera...")

    while collected_samples < sample_count:
        ret, frame = video.read()
        if not ret:
            print("Error: Failed to capture image from the camera.")
            break

        # Detect faces
        results = detector.detect_faces(frame)
        if results:
            x, y, w, h = results[0]['box']
            x, y = max(0, x), max(0, y)  # Fix negative coordinates
            crop_img = frame[y:y + h, x:x + w]

            try:
                resized_img = cv2.resize(crop_img, (50, 50))  # Resize face to 50x50
                faces_data.append(resized_img)
                collected_samples += 1
                print(f"Collected {collected_samples} samples.")

                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.imshow("Capturing Faces", frame)
            except Exception as e:
                print(f"Error processing frame: {e}")
                continue

        # If face not detected, continue to the next frame
        if collected_samples < sample_count:
            print("Waiting for face detection...")

        # Check if enough samples are collected
        if collected_samples >= sample_count:
            break

    video.release()
    cv2.destroyAllWindows()

    if len(faces_data) == 0:
        print("No faces detected!")
        return False

    print(f"Successfully collected {len(faces_data)} samples for {name}.")

    # Prepare data for saving
    faces_data = np.asarray(faces_data)
    faces_data = faces_data.reshape(len(faces_data), -1)

    # Load or create names and faces data
    names_path = "Data/names.pkl"
    faces_path = "Data/faces_data.pkl"

    if os.path.exists(names_path) and os.path.exists(faces_path):
        with open(names_path, 'rb') as f:
            names = pickle.load(f)
        with open(faces_path, 'rb') as f:
            faces = pickle.load(f)
    else:
        names = []
        faces = np.empty((0, 50 * 50 * 3))  # Empty array for RGB images

    # Add new data
    names.extend([name] * len(faces_data))
    faces = np.vstack((faces, faces_data))

    # Save data
    with open(names_path, 'wb') as f:
        pickle.dump(names, f)
    with open(faces_path, 'wb') as f:
        pickle.dump(faces, f)

    print(f"Successfully added {name} with {len(faces_data)} samples.")
    return True

if __name__ == "__main__":
    if len(sys.argv) > 1:
        add_face(sys.argv[1])
    else:
        print("Please provide a name as an argument.")
