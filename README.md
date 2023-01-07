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
 
 ### Parameters
This notebook provides an overview of polynomial regression, which is used in scenarios where the relationship between x and y is not linear, and the line of best fit is closer to a curve. A polynomial regression model can be developed using Least Squares Fitting; this is a procedure for finding the best-fitting curve for a given dataset by minimizing the sum of the squares of the offsets of the points from the curve. 

In the notebook, the NumPy polyfit function is used to fit a polynomial function with a defined number of degrees to a given data set, where degrees refer to the highest power of the variables in the function. When selecting the number of degrees for a polynomial function, it is important not to overfit the data. Overfitting is where the model has too many terms for the number of observations, and begins to fit the data exactly. This can mean that the model is describing the random error in the data rather than the actual relationships between the variables. 

### Keras Time Series Anomaly Detector
In this notebook, a neural network is developed using Keras to detect anomalies in the Numenta Anomaly benchmark dataset. The code and plots have been adapted from the Keras documentation, which can be accessed via the below link.

https://keras.io/examples/timeseries/timeseries_anomaly_detection/.

This notebook demonstrates how a neural network, developed using Keras, could be trained to recognize and replicate patterns in a given data set. The input data in this case is taken from the Numenta Anomaly Benchmark source data: NAB is an open-source framework for evaluating and benchmarking anomaly detection algorithms. In addition to real-world anomaly examples, the NAB source data also includes simulated anomaly files. This model is trained to reconstruct one of these simulated data sets, daily_small_noise. This data set emulates small daily variations in a given system. Once the model was trained, it could be passed data from a second source file to the model, with the same structure as the daily_small_noise data set but one set of anomalous values. As the model has been trained to predict only small values in the data set, the error values (MAE) for the anomalies far exceeds the reconstruction loss threshold. We can then flag these values where the MAE is higher than the threshold as anomalies.
