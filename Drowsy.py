
import cv2
import mediapipe as mp
import winsound

mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh()

cap = cv2.VideoCapture(0)

sleep_counter = 0

while True:
    success, frame = cap.read()
    if not success:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb)

    if result.multi_face_landmarks:
        for face_landmarks in result.multi_face_landmarks:

            left_eye = [33,160,158,133,153,144]

            h,w,_ = frame.shape
            eye_points = []

            for id in left_eye:
                x = int(face_landmarks.landmark[id].x * w)
                y = int(face_landmarks.landmark[id].y * h)
                eye_points.append((x,y))
                cv2.circle(frame,(x,y),2,(0,255,0),-1)

            if abs(eye_points[1][1] - eye_points[5][1]) < 12:
                sleep_counter += 1
            else:
                sleep_counter = 0

            if sleep_counter > 15:
                cv2.putText(frame,"DROWSINESS ALERT!",
                            (50,100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,(0,0,255),3)

                # Windows alarm sound
                winsound.Beep(1000, 500)

    cv2.imshow("Driver Monitoring", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()