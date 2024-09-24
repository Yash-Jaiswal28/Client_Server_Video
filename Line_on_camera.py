import cv2
import numpy as np

# Initialize the camera
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, image = camera.read()
    
    if not ret:
        print("Error: Could not read frame.")
        break

    gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    gradients_sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    gradients_sobely = cv2.Sobel(gray_image,cv2.CV_64F, 0, 1,ksize=3)
    gradients_sobelxy = cv2.addWeighted(gradients_sobelx, 0.5,gradients_sobely, 0.5, 0)

    gradients_lapacian = cv2.Laplacian(gray_image, cv2.CV_64F)

    edges = cv2.Canny(gray_image,80 ,150)
    
    # Perform Hough Line Transform
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
    
    if lines is not None:
        for line in lines:
            rho, theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            print(f"{{{x1},{y1}}} and {{{x2},{y2}}}")
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    # Display the result
    cv2.imshow('canny',edges)
    cv2.imshow('Hough Lines', image)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
camera.release()
cv2.destroyAllWindows()
