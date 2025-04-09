
# Eye Disease Classification

This project demonstrates the implementation of various machine learning and deep learning models for multi-label classification of eye diseases using fundus images. The dataset consists of fundus images of the left and right eyes, each labeled with one or more of the following conditions:

-   **N**: Normal
-   **D**: Diabetes
-   **G**: Glaucoma
-   **C**: Cataract
-   **A**: Age-related Macular Degeneration (AMD)
-   **H**: Hypertension
-   **M**: Pathological Myopia
-   **O**: Other abnormalities

The other dataset is more balanced and contains 4 classes 
- cataract
- diabetic_retinopathy
- glaucoma
- normal

## Features

-   **Dataset Analysis and Preprocessing**:
    -   Extensive Exploratory Data Analysis (EDA) and preprocessing.
    -   Data augmentation for improved generalization in deep learning models.
    -   Filtering for valid patients and images.
-   **Model Implementations**:
    -   Traditional machine learning models:
        -   Random Forest
        -   K-Nearest Neighbors (KNN)
        -   Logistic Regression
        -   Gradient Boosting
        -   Support Vector Machine (SVM)
        -   XGBoost
        -   AdaBoost
    -   Deep learning models:
        -   ResNet50 
        -   EfficientNet
-   **Evaluation Metrics**:
    -   Accuracy
    -   Precision, Recall, F1-score (micro/macro)
    -   Exact match ratio and per-label precision/recall.

----------


## Datasets Used

https://www.kaggle.com/datasets/andrewmvd/ocular-disease-recognition-odir5k

https://www.kaggle.com/datasets/gunavenkatdoddi/eye-diseases-classification/data

----------

## Installation

### Prerequisites

-   Python 3.8+
-   CUDA-enabled GPU (optional for deep learning models)

## Usage


### Training Machine Learning Models

```test.ipynb contains the deep learning models training``` 


### Training Deep Learning Models


```main1.ipynb contains the deep learning models training``` 
    






