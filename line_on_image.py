import cv2
import numpy as np
import matplotlib.pyplot as plt
# Step 1: Load the image
image = cv2.imread('image.png')
image=cv2.resize(image,(500,500))

kernel_size=6
std_dev=5

kernel = cv2.getGaussianKernel(kernel_size, std_dev)
kernel = kernel * kernel.T

# Apply the Gaussian filter to the image
filtered_img = cv2.filter2D(image, -1, kernel)
cv2.imshow('Image with Boundaries', filtered_img)

# Convert the image to grayscale
gray = cv2.cvtColor(filtered_img, cv2.COLOR_BGR2GRAY)
# # Step 2: Convert to grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply edge detection (Canny method)
edges = cv2.Canny(gray, threshold1=100, threshold2=200)

# Step 4: Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
X=[]
Y=[]
# Step 5: Loop through each contour to get boundary coordinates
for contour in contours:
    for point in contour:
        x, y = point[0]
        print(f"Boundary Coordinate: ({x}, {y})")
        X.append(x)
        Y.append(y)

# Optional: Draw contours on the image
detect=cv2.drawContours(filtered_img, contours, -1, (0, 255, 0), 2)

# Show the result
cv2.imshow('Image with Boundaries', detect)
# cv2.imshow("Orginal",image)

X=np.array(X)
Y=np.array(Y)
plt.plot(X,Y)
# plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
