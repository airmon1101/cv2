import cv2

cap = cv2.VideoCapture(0) # 0 for inbuld web cam / 1 for external cameras

while True:
    ret, frame = cap.read()
    if not ret:
        print("Could not ret frame ")
        break
    else:
        cv2.imshow("Web feed", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("Quitting.....")
            break
cap.release()
cv2.destroyAllWindows()