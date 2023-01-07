# Machine Learning and Statistics Assessment
## Student Name : Kate McGrath
## Student ID : G00398908
## Submission Date : 07/01/2022

## Contents of Repository
This repository consists of two main components:
- **Exercise Notebooks**: These notebooks contain the weekly exercises for each of the main topics covered as part of the Machine Learning and Statistics module.
- **Keras Time Series Anomaly Detection Notebook** : This notebook is an adaptation of the Keras documentation on building a neural network to detect anomalies in time series data

## Getting Started
The following packages are required to run the code in this notebook:
 - matplotlib==3.5.1
 - numpy==1.21.4
 - pandas==1.3.4
 - scipy==1.7.1
 - seaborn==0.11.2

These packages and the correct versions are included in the requirements.txt file in this repository.


## Exercise Notebooks
The exercise notebooks include the following:
### Statistics 
This notebook builds on the Lady Tasting Tea problem first described by Ronald Fisher. In this experiment, the subject claims that by tasting cups of tea, she can tell whether the milk or tea has been added first. Fisher designed an experiment to test this, where the subject is presented with 8 cups of tea, 4 with milk added first and 4 with tea added before milk, and the probability of her guessing the right answer for each by chance is calculated. In this notebook, we first determine the minimum number of cups required to maintain a probability of <1% of randomly selecting three correct cups and one incorrect. We also use SciPy's version of Fisher's exact test to simulate the problem. This function takes a 2x2 contingency table as a parameter, and returns the probability that the observed values could have occurred if the null hypothesis was correct, i.e. the subject has no ability to tell the difference.

In addition, the notebook adapts the SciPy documentation on the independent samples t test function, which is used to compare the mean values for two arrays. It examines the impact of multiple factors on the accuracy of the result returned, including heavy tailed values, arrays with unequal variances and different sample sizes.

### Models

This notebook has two main components:
- Absolute Value Functions: Using NumPy and Matplotlib, the Absolute Value Function is plotted. An absolute value function is a function that contains of a variable within absolute value bars; it is commonly used to measure the distance between points. However, it is not suitable for fitting straight lines to data; the simplest method of doing this is using a function called differentiation, which is not possible with absolute values as the function is not differentiable at 0. 
  - Fit Line to Data Set: Three methods are used to fit a straight line to a given dataset (x and y)
  - NumPy Polyfit : Uses Least Squares Fitting to calculate the line of best fit for the data.
  - SciPy Optimize : Given a function and an initial guess for the m and c parameters, SciPy Optimize returns the m and c values for the funciton that will result in the least cost.
  - SciPy Curve Fit : Uses Non-Linear Least Squares Fitting to fit a curve to a data set.
 All the above methods provide similar optimized m and c values; however, a straight line is not the best method of modelling the data set as the relationship between x and y is not linear. The NumPy polyfit function was repeated with 3 degrees, and this appeared to fit the data more closely.
