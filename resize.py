import cv2

image = cv2.imread(str(input("Enter Image Path Here: ")))
# width, height

if image is not None:
    print("Image loaded")

    resized = cv2.resize(image, (520, 520))

    cv2.imshow("Original Image", image)
    cv2.imshow("Resized Image", resized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(str(input("Enter Output file name")), resized)
