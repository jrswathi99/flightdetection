import cv2
import numpy as np

# Load the image
image_path = r"C:\PycharmProjects\pythonProject1\test_images\test_image4.jpeg"
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blurring and thresholding
blur = cv2.GaussianBlur(gray_image, (3, 3), 0)
_, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Find contours in the image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Process each contour (strip) individually
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    area = cv2.contourArea(contour)
    
    # Add conditions to process individual strips based on area, aspect ratio, etc.
    if area > 500 and w > 20 and h > 100:
        # Calculate the orientation angle of the strip
        rect = cv2.minAreaRect(contour)
        angle = rect[2]
        
        # Rotate the strip to align horizontally
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle
        
        # Rotate the strip
        M = cv2.getRotationMatrix2D((x + w//2, y + h//2), angle, 1.0)
        strip_rotated = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]), flags=cv2.INTER_CUBIC)

        # Draw bounding box around the strip
        cv2.rectangle(strip_rotated, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image with aligned strips
cv2.imshow("Image with Aligned Strips", strip_rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()