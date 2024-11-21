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
├── bccd/
│   ├── outputs/
│   ├── test-images/
│   ├── weights/
│       ├── best_bccd_v0.pt
│       ├── best_bccd_v1.pt
│   └── testing.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

- bccd/: Contains Blood Cell Cound and Detection side of the project.
- best_bccd_v0.pt: Version 0 of the first dataset from Roboflow. (yolov5n - T4 GPU)
- best_bccd_v1.pt: Version 1 of the first dataset from Roboflow. (yolov5l - A100 GPU - 50 epoch - 8 batch)
- requirements.txt: Lists project dependencies.

## How To Run?
1. Install dependencies:
```
pip install -r requirements.txt
```
or
```
pip3 install -r requirements.txt
```

2. Run (example):
```
python testing.py
```
or
```
python3 testing.py
```

## Licence

This project is licensed under the MIT License - see the [LICENSE](https://github.com/semanurbilada/BIP_BAP?tab=MIT-1-ov-file#readme) file for details.


## References

- BCCD Dataset: https://public.roboflow.com/object-detection/bccd/3
- Custom Roboflow Dataset: https://universe.roboflow.com/prutengiz/bccd-dataset-v0/dataset/2