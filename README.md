<div align="center">
<img src="https://cdn-icons-png.flaticon.com/512/14784/14784041.png" width="100" height="100" alt="icon">
</div>

<h1 align="center">BIP BAP</h1>

<div align="center">

## Biomedical Image Processing BAP (Scientific Research Project)
</div>

* [Purpose](#purpose)
* [Features](#features)
    * [Notes](#notes)
* [Project Structure](#project-structure)
* [How To Run?](#how-to-run)
* [Licence](#licence)
* [References](#references)

## Purpose
<div align="justify">

This project aims to explore biomedical image processing applications, focusing on the detection and counting of blood cells using the Blood Cell Counting and Detection (BCCD) dataset. The system is designed to automate and enhance accuracy in biomedical imaging tasks, with the initial training conducted on Google Colab. 

As part of the Piri Reis University Scientific Research Project (BAP), this initiative also reflects the academic contributions of the scholar students.
</div>

## Features
- Detection and count for blood cell (BCCD).
- Performance Measurement: Latency - Throughput - Reliability.

### Notes
- The yolov5m (medium) model was tested, but based on the results, the yolov5s (small) or yolov5l (large) models are recommended for better performance.

## Project Structure

The project follows this directory structure:

```
BIP_BAP/
├── results/
│   ├── kfold_yolov5l_100epochs/
│   ├── outputs-v5/
│   └── outputs-v8/
├── scripts/
│   ├── kfold_yolo_attention_mechanism.ipynb
│   ├── kfold_yolo_integration.ipynb
│   ├── yolov5.py
│   └── yolov8.py
├── test-images/
├── weights/
│   ├── best_bccd_v0.pt
│   ├── best_bccd_v1.pt
│   └── best_bccd_v3.pt
├── yolovenv/
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```
- results/: Contains various outputs and performance results.
    - /kfold_yolov5l_100epochs/: Contains kfold results with Yolov5l 100epochs - A100 GPU.
    - /outputs-v5/: Contains outputs of the yolov5 test results.
    - /outputs-v5/: Contains outputs of the yolov8 test results.
- scripts:/ Includes all the main scripts and Jupyter notebooks used in the project.
    - kfold_yolo_attention_mechanism.ipynb: A Jupyter notebook implementing K-Fold cross-validation with an attention mechanism for YOLO-based models.
    - kfold_yolo_integration.ipynb: A notebook integrating K-Fold validation with YOLO training and testing.
    - yolov5.py: YOLOv5-based detection.
    - yolov8.py: YOLOv8-based detection.
- test-images/: Contains sample test images used for validation and inference.
- weights/: Stores trained model weight files.
    - best_bccd_v0.pt: Version 0 of the first dataset from Roboflow. (yolov8 - T4 GPU)
    - best_bccd_v1.pt: Version 1 of the first dataset from Roboflow. (yolov5l - A100 GPU)
    - best_bccd_v3.pt: Version 1 of the first dataset from Roboflow. (yolov5l - A100 GPU)
- yolovenv/: The virtual environment containing dependencies for running the project.
- .gitignore: Specifies files and directories to be ignored by Git.
- LICENSE: The MIT License file.
- README.md: The documentation file explaining the project.
- requirements.txt: Lists project dependencies.

## How To Run?
1. Virtual environment setup:
```
python3 -m venv yolovenv
```

2. To activate the virtual environment (Windows):
```
yolovenv/Scripts/activate
```

3. To activate the virtual environment (Linux / MacOS):
```
source yolovenv/bin/activate
```

4. Install dependencies:
```
pip install -r requirements.txt
```
or
```
pip3 install -r requirements.txt
```

5. Run the code samples in scripts directory:
```
python yolov5.py
```
or
```
python3 yolov8.py
```

## Licence

This project is licensed under the MIT License - see the [LICENSE](https://github.com/semanurbilada/BIP_BAP?tab=MIT-1-ov-file#readme) file for details.


## References

- [BCCD Dataset](https://github.com/Shenggan/BCCD_Dataset)
- [BCCD Dataset - Roboflow](https://public.roboflow.com/object-detection/bccd/3)
- [Custom Roboflow Dataset](https://universe.roboflow.com/prutengiz/bccd-dataset-v0/dataset/2)