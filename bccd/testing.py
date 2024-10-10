from ultralytics import YOLO

#TODO: global images
#TODO: custom path for runs

model = YOLO('../weights/best_bccd.pt')
img = "../test-images/BloodImage_00007.jpg"

result = model.predict(source=img, conf=0.5, save=True)