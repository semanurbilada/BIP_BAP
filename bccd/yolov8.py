import glob, random
from ultralytics import YOLO

# Configurations
WEIGHTS_PATH = './weights/best_bccd_v0.pt'
TEST_IMAGES_PATH = './test-images/*.jpg'
OUTPUT_PROJECT = './'
OUTPUT_NAME = 'outputs-v8'
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
        exist_ok=True  # outputs in the same folder
    )

print("\nDone!\n")