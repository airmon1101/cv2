import cv2

# /home/dhruv/New_cv2_project/canny_output.jpg

img = cv2.imread('/home/dhruv/New_cv2_project/yellow_filled_triangle_white_bg_1000.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

# Find Contours
contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0,255,0), 3)

cv2.imshow('Contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()