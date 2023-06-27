
# Region Of Interest(ROI) Detector Sports

The goal of this project is to develop a model that can automatically locate the Region of Interest (ROI) in screenshots from sports apps such as Yahoo Sports and The Bleacher. The ROI refers to the rectangular area in the screenshot that contains important text, including headings,team names, sports names, and other relevant information.

To accomplish this, we will utilize the **YOLOv8** algorithm for object detection, which has been proven effective in accurately identifying objects in images. The model will be trained to detect and localize the ROIs in mobile screenshots from sports apps.


## Table of Contents

- [Region Of Interest(ROI) Detector Sports](#Region-Of-Interest(ROI)-Detector-Sports)
  - [Table of Contents](#table-of-contents)
  - [About The Project](#about-the-project)
    - [Tech Stack](#tech-stack)
    - [Screenshot](#screenshot)
        - [Confusion Matrix](#confusion-matrix)
        - [Confusion Matrix Normalized](#confusion-matrix-normalized)
        - [F1 Curve](#F1-Curve)
        - [P Curve](#P-Curve)
        - [R Curve](#R-Curve)
        - [PR Curve](#PR-Curve)
        - [Labels](#labels)
        - [Labels correlogram](#labels-correlogram)
  - [Final Result Table](#final-result-table)
    - [Table of first five rows](#table-of-first-five-rows)
    - [Result Screenshot](#result-screenshot)
  - [Train Batches](#train-batches)
    - [train_batch0](#train_batch0)
    - [train_batch1](#train_batch1)
    - [train_batch2](#train_batch2)
  - [Image Label and Prediction](#image-label-and-prediction)
    - [batch0_label](#batch0_label)
    - [batch0_pred](#batch0_pred)
    - [batch1_label](#batch1_label)
    - [batch1_pred](#batch1_pred)
  - [Contributors](#contributors)
  - [License](#license)
## About the Project
## Tech Stack
* [Python](https://www.python.org/)
* [OpenCV](https://opencv.org/)
* [PIL](https://python-pillow.org/)
* [yolov8](https://ultralytics.com/yolov8)

## Screenshots
* ### Confusion Matrix
![App Screenshot](https://i.ibb.co/QbRLQ2q/confusion-matrix.png)
* ### Confusion Matrix Normalized
![App Screenshot](https://i.ibb.co/yhv0FgV/confusion-matrix-normalized.png)
* ### F1 Curve
![App Screenshot](https://i.ibb.co/pbKrhns/F1-curve.png)
* ### P Curve
![App Screenshot](https://i.ibb.co/st4WcmR/P-curve.png)
* ### R Curve
![App Screenshot](https://i.ibb.co/Ypf66bW/R-curve.png)
* ### PR Curve
![App Screenshot](https://i.ibb.co/7JRsF0c/PR-curve.png)
* ### Labels
![App Screenshot](https://i.ibb.co/vVfdYKd/labels.jpg)
* ### Labels correlogram
![App Screenshot](https://i.ibb.co/JncCYr6/labels-correlogram.jpg)

## Final Result Table

**Table of first five rows**

| Epoch | Train/Box_loss | Train/Cls_loss | Train/Dfl_loss | Metrics/Precision(B) | Metrics/Recall(B) | Metrics/mAP50(B) | Metrics/mAP50-95(B) | Val/Box_loss | Val/Cls_loss | Val/Dfl_loss | LR/PG0 | LR/PG1 | 
|-------|----------------|----------------|----------------|----------------------|-------------------|------------------|---------------------|--------------|--------------|--------------|--------|--------|
| 0     | 1.3141         | 2.1105         | 1.2296         | 0.42433              | 0.93463           | 0.65211          | 0.90711             | 2.4356       | 0.88492      | 0.00065217   | 0.00065217 | 0.00065217 |
| 1     | 0.92957        | 1.2182         | 0.99372        | 0.93278              | 0.7726            | 0.58123          | 0.91173             | 1.596        | 0.85793      | 0.0011883    | 0.0011883  | 0.0011883  |
| 2     | 0.91132        | 1.0584         | 0.99081        | 0.94102              | 0.95904           | 0.74032          | 0.8636              | 0.88449      | 0.87043      | 0.0015924    | 0.0015924  | 0.0015924  |
| 3     | 0.88893        | 0.92452        | 0.98546        | 0.89135              | 0.95178           | 0.7441           | 0.80935             | 0.88887      | 0.84361      | 0.001406     | 0.001406   | 0.001406   |
| 4     | 0.8252         | 0.80252        | 0.96063        | 0.95748              | 0.98607           | 0.76369          | 0.82087             | 0.68853      | 0.85969      | 0.001406     | 0.001406   | 0.001406   |
| 5     | 0.80363        | 0.7365         | 0.94746        | 0.96921              | 0.98998           | 0.81167          | 0.72804             | 0.59324      | 0.84232      | 0.001208     | 0.001208   | 0.001208   |



**Result Screenshot**
![App Screenshot](https://i.ibb.co/7rfHVxD/results.png)

## Train Batches
* ### train_batch0
![App Screenshot](https://i.ibb.co/HFjxyNX/train-batch0.jpg)

* ### train_batch1
![App Screenshot](https://i.ibb.co/hV2zWHx/train-batch1.jpg)

* ### train_batch2
![App Screenshot](https://i.ibb.co/2N2DVGC/train-batch2.jpg)
## Image Label and Prediction
* ### batch0_label
![App Screenshot](https://i.ibb.co/J5YgrQn/val-batch0-labels.jpg)

* ### batch0_pred
![App Screenshot](https://i.ibb.co/pyWdFT7/val-batch0-pred.jpg)

* ### batch1_label
![App Screenshot](https://i.ibb.co/89p4d7T/val-batch1-labels.jpg)

* ### batch1_pred
![App Screenshot](https://i.ibb.co/PmJjW1Q/val-batch1-pred.jpg)

* ### batch2_label
![App Screenshot](https://i.ibb.co/DRx7MX0/val-batch2-labels.jpg)

* ### batch2_pred
![App Screenshot](https://i.ibb.co/1zBQDWB/val-batch2-pred.jpg)

## Contributors
## License

[MIT](https://choosealicense.com/licenses/mit/)

