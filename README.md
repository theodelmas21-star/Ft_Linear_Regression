# Ft_Linear_Regression

    Implementation of a Linear Regression model from scratch in Python.

# Description

    > A simple linear regression implementation from scratch in Python, using Gradient Descent to predict car prices based on their mileage. This is a project from the 42 AI/Databases curriculum.
  The project explores the fundamentals of machine learning, including data processing, hypothesis functions, cost calculation, and gradient descent optimization.


---

## Table of Contents
1. About The Project
2. Features and Architecture
3. Prerequisites
4. Usage and Execution
   - Training the Model
   - Predicting a Price
   - Visualization and Scoring
5. In-Depth Mathematical Concepts

---

##  About The Project
The goal of this project is to introduce machine learning concepts by programming a linear regression model **without external ML libraries** (like Scikit-Learn for the training part). 

The program maps out the relationship between a car's mileage ($X$) and its price ($Y$) using a linear equation:
$$\text{price} = \theta_0 + (\theta_1 \times \text{mileage})$$

---

## 🛠️ Features & Architecture

* **`train.py`**: Implements **Gradient Descent** with feature scaling (Min-Max normalization) to iteratively minimize the gap. It saves the optimal weights ($\theta_0$ and $\theta_1$) into a `thetas.json` file.
* **`price.py`**: A CLI program that loads the trained weights and estimates the price of a car given its mileage. Includes safety bounds against negative price extrapolations.
* **`precision.py`**: 
  * Computes the **$R^2$ (Coefficient of Determination)** score to evaluate the model's performance against a baseline average model.
* **`plot.py`**: 
    * Plots the raw data points alongside the regression line using `matplotlib`.

---

## Prerequisites & Installation

Make sure you have Python 3 installed on your machine. 

### 1. Installing Python 3
Depending on your operating system, use the appropriate command:

* **Linux (Ubuntu / Debian):**
  ```bash
  sudo apt update
  sudo apt install python3 python3-pip

* **macOS (using HomeBrew)**
    ```bash
  brew install python

* **Windows**

  Download and install the latest Python 3 version from the official Python website (python.org).

 * **Installing Dependencies:**

    You will need matplotlib for data visualization:
    ```bash
    pip install matplotlib

---

## Usage and Execution Guide

1. Training the Model (train.py):
This script reads data.csv, normalizes the features, runs 10,000 gradient descent iterations, and saves the result in thetas.json.
Command: python train.py

2. Predicting a Price (price.py):
This script prompts the user for a mileage and displays the estimated price.
Command: python price.py

3. Visualization and Scoring (precision.py):
This script displays the graphical representation of the dataset with the fitted line and prints the precision score.
Command: python precision.py

---

## In-Depth Mathematical Concepts

1. Min-Max Normalization:
Before running gradient descent, features are scaled between 0 and 1:
x_norm = (x - x_min) / (x_max - x_min)

2. Gradient Descent Optimization:
Instead of computing the full MSE value, the algorithm calculates the gradients (derivatives of the MSE) using the gap between estimations and actual prices, updating theta0 and theta1 simultaneously using a learning rate alpha:
theta0 = theta0 - alpha * (1 / m) * sum( gap )
theta1 = theta1 - alpha * (1 / m) * sum( gap * x )

3. Gradient Descent Optimization:
Iteratively updates theta0 and theta1 using a learning rate alpha:
theta0 = theta0 - alpha * (1 / m) * sum( estimated_price - actual_price )
theta1 = theta1 - alpha * (1 / m) * sum( (estimated_price - actual_price) * mileage )

4. R2 Score (Coefficient of Determination):
Measures precision by comparing residual errors to total variance:
R2 = 1 - (ss_res / ss_total)
- 0% (or 0): The model is no better than predicting the average price.
- 100% (or 1): Perfect prediction accuracy.