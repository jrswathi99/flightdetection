import cv2
import argparse

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description= "Yolov8 Live")
    parser.add_argument(
        
        nargs=2,
        type=int
    )
    args=parser.parse_args()
    return args


def main():
    args = parse_arguments()
    frame_width, frame_height = args.webcam_resolution

    web= 0
    cap= cv2.VideoCapture(web)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

    while True:
        ret, frame = cap.read()
        cv2.imshow("yolov8" , frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()       

if __name__=="__main__":
    main()