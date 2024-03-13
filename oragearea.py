import cv2
import numpy as np

# Load the image
image = cv2.imread('image.jpg')

# Convert the image to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the color range for the color orange
lower_orange = np.array([5, 100, 100])
upper_orange = np.array([15, 255, 255])

# Create a mask that represents the pixels in the color range
mask = cv2.inRange(hsv, lower_orange, upper_orange)

# Find contours in the mask
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Find the largest contour and its bounding rectangle
largest_contour = max(contours, key = cv2.contourArea)
x, y, w, h = cv2.boundingRect(largest_contour)

# Save the coordinates of the orange area to a variable
orange_area_coordinates = (x, y, w, h)

# Print the coordinates of the orange area
print(f'Orange area coordinates: {orange_area_coordinates}')