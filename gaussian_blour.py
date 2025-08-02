import cv2

image = cv2.imread(str(input('Enter image path here: ')))

if image is None:
    print('Could not load the image!')
else:
    blurred = cv2.GaussianBlur(image, (9,9), 0)
    cv2.imshow('Original Image', image)
    cv2.imshow('Blurred Image', blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()