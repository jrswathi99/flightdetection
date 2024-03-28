import cv2
import numpy as np

# Load the image using the GPU
image_gpu = cv2.cuda_GpuMat()
image_path = "C:\PycharmProjects\pythonProject1\test_images\test_image3.jpeg"
image_np = cv2.imread(image_path)
image_gpu.upload(image_np)

# Convert the image to grayscale using the GPU
gray_gpu = cv2.cuda.cvtColor(image_gpu, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blurring and thresholding using the GPU
blur_gpu = cv2.cuda.GpuMat()
thresh_gpu = cv2.cuda.GpuMat()
cv2.cuda.blur(gray_gpu, (3, 3), blur_gpu)
_, thresh_gpu = cv2.cuda.thresh_gpu = cv2.cuda.adaptiveThreshold(blur_gpu, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Download the processed image back to CPU for contour detection
thresh_np = thresh_gpu.download()
thresh = np.asarray(thresh_np)

# Find contours in the image (CPU-based operation)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter contours based on area or other criteria to select misaligned strips
selected_contour = None
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    area = cv2.contourArea(contour)
    # Add conditions to select misaligned strips based on area, aspect ratio, etc.
    if area > 1000 and w > 50 and h > 50:
        selected_contour = contour
        break

# Perform alignment analysis for the selected misaligned strip
if selected_contour is not None:
    # Calculate alignment metrics (e.g., centroid, angles) for the misaligned strip
    M = cv2.moments(selected_contour)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    
    # Draw the centroid of the misaligned strip
    cv2.circle(image_np, (cx, cy), 5, (255, 0, 0), -1)
    cv2.imshow("Misaligned Strip with Centroid", image_np)
    cv2.waitKey(0)
    cv2.destroyAllWindows()