import cv2

# Load the original image
original_image = cv2.imread('kumamoto01.png')

# Resize the image
dimension = (100, 100)
resized_image = cv2.resize(original_image, dimension)

# Save or display the image
cv2.imwrite('path/to/resized_image.jpg', resized_image)
