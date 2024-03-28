import cv2

def main():
    # Try different camera indices until the camera opens successfully
    for i in range(5):
        cap = cv2.VideoCapture(i)

        # Check if the camera is opened successfully
        if cap.isOpened():
            print("Using camera index:", i)
            break

    # Check if no camera was opened
    if not cap.isOpened():
        print("Error: Could not open any camera.")
        return

    # Define a window to display the camera feed
    cv2.namedWindow("Camera Feed", cv2.WINDOW_NORMAL)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Check if the frame was captured successfully
        if not ret:
            print("Error: Could not read frame.")
            break

        # Display the frame in the window
        cv2.imshow("Camera Feed", frame)

        # Wait for 'q' key to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

