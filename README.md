# Fingers-Counting
Landing.AI Model for Fingers Count Prediction using Classification
## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [Input Directory](#input-directory)
- [Live link](#Livelink)


## Introduction
This project utilizes a Landing AI model designed to predict the number of fingers shown in images. The model is trained to distinguish between three specific counts of fingers: one, two, and three. It supports multiple image formats including `.jpeg`, `.jpg`, and `.png`.
The script processes images from a specified directory, applies the model to each image, and determines the number of fingers present. The prediction results are then saved to a CSV file, providing an efficient way to analyze and review the outcomes.


## Features
- **Image Processing:** Processes images from a specified directory, supporting formats such as `.png`, `.jpg`, and `.jpeg`.
- **Prediction:** Uses a Landing AI model to predict the number of fingers shown in each image.
- **CSV Output:** Saves the prediction results into a CSV file, including the image name and the prediction result.
- **Progress Tracking:** Displays a message when the results are successfully saved.

## Training
Trained on different images represting fingers (One,Two and Three) =>48 images

## Usage
- Give folder name in image_folder
- Result filename in output_csv
```bash
image_folder = <folderName>
output_csv = <predictionresultsCSV>
```

## Example
```python
image_folder = "Google_images"
output_csv = "predictionsoffaces.csv"
```
## Live link
[https://app.landing.ai/predict/1ef2e652-710a-42ef-9236-7f92dd73f3ae](https://app.landing.ai/predict/1ef2e652-710a-42ef-9236-7f92dd73f3ae)

