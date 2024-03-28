import cv2
import numpy as np
import os
import random

# Function to apply various data augmentation techniques to an image
def augment_image(image):
    augmented_images = []
    
    # Flipping (horizontal and vertical)
    '''flipped_img = cv2.flip(image, 1)
    augmented_images.append(flipped_img)
    
    flipped_vert_img = cv2.flip(image, 0)
    augmented_images.append(flipped_vert_img)'''
    
    # Rotation at arbitrary angles
    '''rot_angle = random.uniform(-30, 30)
    rows, cols = image.shape[:2]
    rot_matrix = cv2.getRotationMatrix2D((cols/2,rows/2), rot_angle, 1)
    rotated_img = cv2.warpAffine(image, rot_matrix, (cols, rows))
    augmented_images.append(rotated_img)'''
    
    # Scaling
    scaled_img = cv2.resize(image, None, fx=0.8, fy=0.8)
    augmented_images.append(scaled_img)
    
    # Translation
    rows, cols = image.shape[:2]
    tx = random.randint(-30, 30)
    ty = random.randint(-30, 30)
    trans_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    translated_img = cv2.warpAffine(image, trans_matrix, (cols, rows))
    augmented_images.append(translated_img)
    
    # Brightness adjustment
    brightness_factor = 0.5 + random.random()  # Random brightness factor between 0.5 and 1.5
    bright_adjusted_img = cv2.convertScaleAbs(image, alpha=brightness_factor, beta=0)
    augmented_images.append(bright_adjusted_img)
    
    # Contrast adjustment
    contrast_factor = 0.5 + random.random()  # Random contrast factor between 0.5 and 1.5
    contrast_adjusted_img = cv2.convertScaleAbs(image, alpha=contrast_factor, beta=0)
    augmented_images.append(contrast_adjusted_img)
    
    return augmented_images

# Function to apply data augmentation to a folder of images
def augment_images_in_folder(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    
    for img_name in os.listdir(input_folder):
        if img_name.endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(input_folder, img_name)
            image = cv2.imread(img_path)
            
            augmented_images = augment_image(image)
            for idx, augmented_img in enumerate(augmented_images):
                output_path = os.path.join(output_folder, f"{img_name.split('.')[0]}_{idx}.jpg")
                cv2.imwrite(output_path, augmented_img)

# Define input and output directory paths
input_folder = r"C:\flight\training_images"
output_folder = r"C:\flight\newaug_imgs"

# Apply data augmentation techniques to images in the input directory
augment_images_in_folder(input_folder, output_folder)