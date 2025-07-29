import cv2

image = cv2.imread("/home/dhruv/New_cv2_project/YT_cv2/whitw_image.jpeg")

if image is not None:

    pt_1 = (500, 50)
    pt_2 = (250, 500)

    color = (0,0,255)
    thickness = 8

    circle = cv2.circle(image, (150,150), 50, (255,0,0), thickness)

    cv2.imshow("Circle Image", circle)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error could not load the Image")