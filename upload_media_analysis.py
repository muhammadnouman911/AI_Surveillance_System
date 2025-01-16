import cv2
from deepface import DeepFace
import os

def analyze_uploaded_media(file_path):

    if not os.path.exists(file_path):
        return "Invalid file path."

    file_extension = file_path.split('.')[-1].lower()

    if file_extension in ['jpg', 'jpeg', 'png']:
        # Analyze image
        image = cv2.imread(file_path)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = DeepFace.analyze(rgb_image, actions=["age", "gender", "emotion"], enforce_detection=False)
        
        # If multiple faces are returned as a list, get the first
        if isinstance(results, list) and len(results) > 0:
            results = results[0]
        return results

    elif file_extension in ['mp4', 'avi', 'mov', 'mkv']:
        # Analyze video
        cap = cv2.VideoCapture(file_path)
        all_results = []
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = DeepFace.analyze(rgb_frame, actions=["age", "gender", "emotion"], enforce_detection=False)
            
            # If multiple faces are returned
            if isinstance(results, list) and len(results) > 0:
                results = results[0]
            all_results.append(results)
        cap.release()

        return all_results

    else:
        return "Unsupported file type."
