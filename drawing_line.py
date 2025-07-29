import cv2

image = cv2.imread("/home/dhruv/New_cv2_project/YT_cv2/whitw_image.jpeg")

if image is None:
    print("Error could not load the image")

else:
    print("Image loadedsuccessfully")
    pt_1 = (50, 100)
    pt_2 = (800, 900)
    color = (150, 200  , 0)
    thickness = 4

    line_image = cv2.line(image, pt_1, pt_2, color, thickness)

    cv2.imshow("Line Image", line_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
