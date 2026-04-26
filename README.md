<h1 align="center">BIP BAP</h1>

<p align="center">
  <img src="data/bipbap-logo.png" width="70%" style="border-radius: 12px;">
</p>

<div align="center">

## Biomedical Image Processing BAP (Scientific Research Project)
</div>

* [Purpose](#purpose)
* [Features](#features)
    * [Notes](#notes)
* [Methodology](#methodology)
* [Results](#results)
* [Project Structure](#project-structure)
* [How To Run?](#how-to-run)
* [Licence](#licence)
* [References](#references)

---

## Purpose
<div align="justify">

This project aims to explore biomedical image processing applications, focusing on the detection and counting of blood cells using the Blood Cell Counting and Detection (BCCD) dataset. The system is designed to automate and enhance accuracy in biomedical imaging tasks, with the initial training conducted on Google Colab.

As part of the Piri Reis University Scientific Research Project (BAP), this initiative also reflects the academic contributions of the scholar students, particularly in `applying and practicing Machine Learning concepts`.

</div>

---

## Features

- Detection and count for blood cell (BCCD).
- Performance Measurement: Latency, throughput, reliability.
- K-Fold Cross Validation technique and integration with YOLO.
- **Attention-enhanced YOLOv5 architecture (CBAM integration).**
- **Leakage-safe dataset splitting (image-based strategy).**
- **End-to-end pipeline from annotation parsing to evaluation.**

---

### Notes

- The yolov5m (medium) model was tested, but based on the results, the yolov5s (small) or yolov5l (large) models are decided to use for better performance.
- Main Entry Point: Run `main.ipynb` for the full pipeline.

---

## Methodology

<div align="justify">

The project follows a structured end-to-end pipeline for biomedical object detection:

### 1. Data Preparation
- XML annotations are parsed and converted into structured tabular format.
- Bounding boxes are normalized into YOLO format.
- Multi-class labels: **RBC, WBC, Platelets**

### 2. Dataset Construction
- Automatic generation of YOLO-compatible directory structure:
    - images/train, images/valid
    - labels/train, labels/valid

### 3. Leakage-Safe Train/Validation Split
- **Image-based splitting strategy** is used instead of annotation-based splitting.
- Prevents data leakage where the same image appears in both sets.

### 4. K-Fold Cross Validation
- File-based K-Fold implementation
- Ensures:
- Robust evaluation
- Generalization capability
- Metrics are aggregated across folds

### 5. Attention Mechanism (CBAM Integration)
- Convolutional Block Attention Module (CBAM) is integrated into YOLOv5
- Enhances:
    - Spatial attention
    - Channel attention
    - Improves detection performance on small biomedical objects

### 6. Model Training & Evaluation
- Multiple YOLO variants tested (v5s, v5l, v8)
- Best fold selected based on validation performance
- Performance metrics extracted and analyzed

### 7. Visualization & Analysis
- Bounding box visualization
- Prediction overlays
- Performance comparison across folds and models

</div>

---

## Results

<div align="center">

### Model Performance Overview

<img src="outputs/final/confusion_matrix.png" width="45%">
<img src="outputs/final/PR_curve.png" width="50%">

<br>

<img src="outputs/final/F1_curve.png" width="48%">
<img src="outputs/final/P_curve.png" width="48%">

</div>

<div align="justify">

The evaluation results are obtained using a **5-Fold Cross Validation strategy**, ensuring robust and generalized performance assessment.

- Mean and standard deviation metrics across folds are reported (`kfold_summary_mean_std.csv`)
- Detailed fold-wise results are available (`kfold_summary.csv`)
- Precision, Recall and F1-score curves provide insight into model behavior

</div>

<div align="center">

### Qualitative Results

<img src="outputs/final/val_batch0_labels.jpg" width="48%">
<img src="outputs/final/val_batch0_pred.jpg" width="48%">

</div>

<div align="justify">

Sample predictions demonstrate the effectiveness of the detection pipeline, including bounding box localization and classification performance across different cell types.

👉 <a href="outputs/final/">See additional qualitative and quantitative results!</a>

</div>

---

## Project Structure

The project follows this directory structure:

```
BIP_BAP/
├── core/
│   ├── performance_analysis.py
│   ├── yolov5.py
│   └── yolov8.py
├── data/
│   └── test/
├── experiments/
│   ├── kfold_yolo_attention_mechanism.ipynb
│   └── kfold_yolo_integration.ipynb
├── outputs/
│   ├── final/
│   ├── outputs-v5/
│   └── outputs-v8/
├── weights/
│   ├── best_bccd_0_v8.pt
│   └── best_bccd_1_v5.pt
├── yolovenv/
├── .gitignore
├── LICENSE
├── main.ipynb
├── README.md
└── requirements.txt
```

- core/: Core implementation (YOLO pipelines, scripts).
- data/test/: Test images used for inference (sample data).
- experiments/: Experimental notebooks (K-Fold, attention mechanisms).
- outputs/: Model predictions and evaluation results.
- weights/: Pretrained and trained model weights.
- main.ipynb: Final end-to-end pipeline (main entry point).

---

## How To Run?

### 1. Local Environment Setup

Create a virtual environment:
```
python3 -m venv yolovenv
```

Activate environment: <br>
Windows:
```
yolovenv/Scripts/activate
```

Linux / MacOS:
```
source yolovenv/bin/activate
```

Install dependencies:
```
pip3 install -r requirements.txt
```

### 2. Run Inference Scripts (Local)
```
python3 core/yolov5.py
```
or
```
python3 core/yolov8.py
```

### 3. Run Full Pipeline (Recommended)
The complete pipeline, including:
- Data preprocessing
- K-Fold splitting
- Attention-enhanced training (CBAM)
- Evaluation
is implemented in:
```
main.ipynb
```

### 📌 Note:
This notebook was executed using **`Google Colab (T4 / A100 GPU)`** during the experiments. <br>
It is recommended to run the notebook in a GPU-enabled environment for reproducibility

---

## Citation

If you use BIP-BAP in your research, please cite:

```bibtex
@software{BIP_BAP2026,
  title   = {BIP-BAP: Attention-Enhanced YOLO for Biomedical Image Processing (BAP Project)},
  author  = {Volkan Uslan, Semanur Bilada, Abdulkerim Akten},
  year    = {2026},
  url     = {https://github.com/semanurbilada/BIP_BAP}
}
```

---

## Licence

MIT License - see the [LICENSE](https://github.com/semanurbilada/BIP_BAP?tab=MIT-1-ov-file#readme) file for details.

---

## References

- [BCCD Dataset - GitHub](https://github.com/Shenggan/BCCD_Dataset)
- [BCCD Dataset - Roboflow](https://public.roboflow.com/object-detection/bccd/3)
- [Custom Roboflow Dataset](https://universe.roboflow.com/prutengiz/bccd-dataset-v0/dataset/2)