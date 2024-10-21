# cv_functions.py

# Placeholder for OpenCV functions
import cv2

def process_image(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Placeholder for processing (e.g., edge detection, object detection)
    if image is not None:
        print(f"Processing image: {image_path}")
        # Add processing steps here
    else:
        print(f"Failed to load image: {image_path}")