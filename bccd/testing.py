import glob
import random
from ultralytics import YOLO

#ERROR: yolov8(code) - yolov5(weight) is not suitable together
#TODO: https://docs.ultralytics.com/models/yolov5/#usage-examples

#TODO: Bu kod yolov8 için, yolov5 için de ayrı deneme kodu: yolov5, yolov8...

# Configurations
WEIGHTS_PATH = '../weights/best_bccd_v0.pt'
TEST_IMAGES_PATH = './test-images/*.jpg'
OUTPUT_PROJECT = './'
OUTPUT_NAME = 'outputs'
CONFIDENCE_THRESHOLD = 0.5

# Load the YOLO model
model = YOLO(WEIGHTS_PATH)

# Gather test images
images_path = glob.glob(TEST_IMAGES_PATH)
random.shuffle(images_path)

# Run predictions for each image
for img_path in images_path:
    result = model.predict(
        source=img_path, 
        conf=CONFIDENCE_THRESHOLD, 
        save=True, 
        project=OUTPUT_PROJECT, 
        name=OUTPUT_NAME,
        exist_ok=True  # Outputs in the same folder
    )

print("\nDone!\n")