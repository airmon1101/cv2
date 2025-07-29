import cv2

image = cv2.imread("/home/dhruv/New_cv2_project/YT_cv2/whitw_image.jpeg")

if image is not None:

    pt_1 = (500, 50)
    pt_2 = (250, 500)

    color = (0,0,255)
    thickness = 5

    rectangle = cv2.rectangle(image, pt_1, pt_2, color, thickness)

    cv2.imshow("Rectangle Image", rectangle)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error could not load the Image")