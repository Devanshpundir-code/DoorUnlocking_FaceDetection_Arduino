import cv2
import face_recognition

import serial

arduino = serial.Serial('COM', 9600, timeout=1)
#multiple images of the same person
img_paths = [
    r"C:\Users\hp\Documents\projects\imagereco\yojit\1.jpeg",
    r"C:\Users\hp\Documents\projects\imagereco\yojit\2.jpeg",
    r"C:\Users\hp\Documents\projects\imagereco\yojit\3.jpeg",
    r"C:\Users\hp\Documents\projects\imagereco\yojit\4.jpeg",
    r"C:\Users\hp\Documents\projects\imagereco\yojit\5.jpeg",
    r"C:\Users\hp\Documents\projects\imagereco\yojit\6.jpeg",
    r"C:\Users\hp\Documents\projects\imagereco\yojit\7.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\8.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\9.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\10.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\11.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\12.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\13.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\14.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\15.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\16.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\17.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\18.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\19.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\20.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\21.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\22.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\23.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\24.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\25.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\26.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\27.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\28.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\29.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\30.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\31.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\32.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\33.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\34.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\35.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\36.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\37.jpeg",
    # r"C:\Users\hp\Documents\projects\imagereco\yojit\38.jpeg",


]

known_encodings = []

for path in img_paths:
    img = cv2.imread(path)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    enc = face_recognition.face_encodings(rgb_img)
    
    if enc:
        known_encodings.append(enc[0])  # Store first face encoding
    else:
        print(f"No face detected in {path}")

# Oppen webcam and recognize faces
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Convert frame to RGB 
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces and encode them
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    """gerneral doubt why does it took 2 arguments



The function face_recognition.face_encodings(rgb_frame, face_locations) :

rgb_frame → The image in which faces are detected

face_locations → The specific locations (bounding boxes) of detected faces

"""

    for i, j in zip(face_encodings, face_locations): #we are itrating j for the box and text it has nothing to do with facedetection, facedetetcion is done when we are comparing face_encoding to know_encodig 
        # Compare the detected face with known faces
        matches = face_recognition.compare_faces(known_encodings, i)
        
        label = "Unknown"

        if True in matches:
            label = "yojit"  
            arduino.write(b'1')

        # Draw a rectangle around the face
        top, right, bottom, left = j
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, label, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Show the video frame
    cv2.imshow("Face Recognition", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
arduino.close()
video_capture.release()
cv2.destroyAllWindows()
