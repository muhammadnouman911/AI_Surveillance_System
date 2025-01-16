import cv2
import numpy as np
from deepface import DeepFace

def generate_webcam_feed():

    cap = cv2.VideoCapture(0)  # Change index if needed (e.g., cap = cv2.VideoCapture(1))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert to RGB for DeepFace
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        try:
            # Using "mtcnn" here for potentially better face detection
            # You may also try: "retinaface", "ssd", "dlib", or "opencv"
            results = DeepFace.analyze(
                rgb_frame,
                actions=["age", "gender", "emotion"],
                detector_backend="mtcnn",
                enforce_detection=False
            )

            # If multiple faces detected, results is a list
            if isinstance(results, list):
                for face_data in results:
                    draw_bounding_box_and_text(frame, face_data)
            else:
                # Single face returns a dict
                draw_bounding_box_and_text(frame, results)

        except Exception as e:
            print(f"Error analyzing frame: {e}")

        # Encode the frame as JPEG
        _, jpeg = cv2.imencode(".jpg", frame)
        yield jpeg.tobytes()

    cap.release()


def draw_bounding_box_and_text(frame, face_data):
    """
    Draws a green bounding box and places the age, gender, and emotion
    underneath the box.
    """
    region = face_data.get("region", {})
    x = region.get("x", 0)
    y = region.get("y", 0)
    w = region.get("w", 0)
    h = region.get("h", 0)

    # Draw the green bounding box
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Extract attributes
    gender = face_data.get("dominant_gender", "Unknown")
    age = face_data.get("age", "Unknown")
    emotion = face_data.get("dominant_emotion", "Unknown")

    # Text starts just below the box:
    text_y_start = y + h + 20
    cv2.putText(frame, f"Gender: {gender}", (x, text_y_start),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    cv2.putText(frame, f"Age: {age}", (x, text_y_start + 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    cv2.putText(frame, f"Emotion: {emotion}", (x, text_y_start + 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
