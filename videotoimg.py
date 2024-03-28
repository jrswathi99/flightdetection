import os
import cv2
from skimage.metrics import structural_similarity as compare_ssim

video_path=r"C:\flight\training_videos\WIN_20240209_15_23_09_Pro.mp4"
output_folder=r"C:\flight\training_images"
def extract_frames(video_path, output_folder, threshold=0.95):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    # Check if the video is opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    
    # Initialize variables
    frame_count = 1589
    prev_frame = None
    
    # Loop through each frame in the video
    while True:
        # Read a frame from the video
        ret, frame = cap.read()
        
        # Check if the frame is read successfully
        if not ret:
            break
        
        # Compare current frame with previous frame
        if prev_frame is not None:
            # Compute structural similarity index
            gray_prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            ssim = compare_ssim(gray_prev_frame, gray_frame)
            
            # Skip frame if similarity is above threshold
            if ssim > threshold:
                continue
        
        # Save the frame as an image
        #image_path = f"{output_folder}/frame_{frame_count}.jpg"
        #cv2.imwrite(image_path, frame)
        image_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
        if not os.path.exists(image_path):
            cv2.imwrite(image_path, frame)
        
        
        # Update previous frame
        prev_frame = frame
        
        # Increment frame counter
        frame_count += 1
    
    # Release the video capture object
    cap.release()
    print(f"Frames extracted: {frame_count}")


extract_frames(video_path, output_folder)

