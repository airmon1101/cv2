import cv2

camera = cv2.VideoCapture(0) # 0 = inbuilt_cam / 1 = external_cam;

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')
fps = 20
recorder = cv2.VideoWriter("myvideo.avi", codec, fps, (frame_width, frame_height))

while True:
    success, image = camera.read()

    if not success:
        break

    recorder.write(image)
    cv2.imshow("Recoding Live", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting.....")
        break

recorder.release()
camera.release()
cv2.destroyAllWindows()