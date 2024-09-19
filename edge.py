import cv2
import numpy as np

camera= cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Camera not found")
    exit()

while True:
    ret,image=camera.read()

    if not ret:
        print("Error: Can't read frame")
        break

    gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    gradients_sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    gradients_sobely = cv2.Sobel(gray_image,cv2.CV_64F, 0, 1,ksize=3)
    gradients_sobelxy = cv2.addWeighted(gradients_sobelx, 0.5,gradients_sobely, 0.5, 0)

    gradients_lapacian = cv2.Laplacian(gray_image, cv2.CV_64F)

    canny_output = cv2.Canny(gray_image,80 ,150)

    cv2.imshow("Original Video", image)
    cv2.imshow("Sobel X+Y", gradients_sobelxy)
    cv2.imshow("Laplacian", gradients_lapacian)
    # cv2.imshow("Canny",canny_output)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

camera.release()
cv2.destroyAllWindows()