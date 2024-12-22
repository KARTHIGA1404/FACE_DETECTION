import cv2
import face_recognition
from socketio import Client

# Connect to Flask-SocketIO server
socketio = Client()
socketio.connect('http://127.0.0.1:5000')

def send_alert_to_website(status, person_info=None):
    # Emit the 'update_status' event to Flask with the status and optional person info
    socketio.emit('update_status', {'status': status, 'person_info': person_info})

def main():
    # Load known images and encode them
    image1_path = "person4.jpg"
    image2_path = "person5.jpg"

    image1 = face_recognition.load_image_file(image1_path)
    image1_encoding = face_recognition.face_encodings(image1)[0]

    image2 = face_recognition.load_image_file(image2_path)
    image2_encoding = face_recognition.face_encodings(image2)[0]

    # Open the video file
    video_path = "v7.mp4"
    video_capture = cv2.VideoCapture(video_path)

    if not video_capture.isOpened():
        print("Error opening video.")
        return

    # Create a window for video playback
    cv2.namedWindow("Suspect Detection", cv2.WINDOW_NORMAL)

    frame_skip = 2  # Number of frames to skip
    frame_count = 0

    while True:
        ret, frame = video_capture.read()

        if not ret:
            print("End of video reached.")
            break

        # Skip frames for faster playback
        frame_count += 1
        if frame_count % frame_skip != 0:
            continue

        # Resize frame for faster processing
        frame = cv2.resize(frame, (640, 480))
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Find all face locations and encodings in the frame
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            # Compare detected face with known faces
            match1 = face_recognition.compare_faces([image1_encoding], face_encoding, tolerance=0.6)
            match2 = face_recognition.compare_faces([image2_encoding], face_encoding, tolerance=0.6)

            (top, right, bottom, left) = face_location

            if match1[0] or match2[0]:
                # Define personal information to send
                person_info = {
                    "name": "deepika",
                    "dob": "01/01/1980",
                    "address": "1234 Main St, Springfield",
                    "contact": "9876543210",
                    "emergency_contact": "9876543210"
                }
                # Draw a rectangle around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, "Suspect Detected", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                print("Suspect Detected")
                send_alert_to_website("Suspect Detected!", person_info)  # Send status and person info to website
            else:
                print("No Match Found.")
                send_alert_to_website("No Match Found.")

        # Display the video frame with detections
        cv2.imshow("Suspect Detection", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
