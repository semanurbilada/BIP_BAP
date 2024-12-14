import glob, torch, random

# Configurations
WEIGHTS_PATH = './weights/best_bccd_v1.pt'
TEST_IMAGES_PATH = './test-images/*.jpg'
OUTPUT_PROJECT = './'
OUTPUT_NAME = 'outputs-v5'
#CONFIDENCE_THRESHOLD = 0.5

# Load the YOLOv5 model
YOLO = torch.hub.load
model = YOLO('ultralytics/yolov5', 'custom', path=WEIGHTS_PATH)

# Gather test images
images_path = glob.glob(TEST_IMAGES_PATH)
random.shuffle(images_path)

# Create output directory
output_path = f"{OUTPUT_PROJECT}/{OUTPUT_NAME}"

for img_path in images_path:
    # Run predictions
    results = model(img_path)

    # Save predictions
    results.save(
        save_dir=output_path, 
        exist_ok=True
    )

print("\nDone!\n")