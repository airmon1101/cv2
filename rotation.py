import cv2

image = cv2.imread("Enter/file/path.jpeg")

if image is None:
    print("Could not load the Image ")
else:
    (h, w) = image.shape[0:2]

    # print(f"Width: {w} \n Hight: {h} ")
    # print(w//2, h//2)

    center = (w//2, h//2) 
    M = cv2.getRotationMatrix2D(center, 90, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))

    cv2.imshow("Original Image", image)
    cv2.imshow("Rotated Image 90Degree", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
