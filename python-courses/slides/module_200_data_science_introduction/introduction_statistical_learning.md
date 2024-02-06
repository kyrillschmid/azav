Ressource:

### An introuction to statistical learning with applications in Python

https://hastie.su.domains/ISLP/ISLP_website.pdf.download.html

Table-of-Contents:

## Chapter 1 Introduction

An Overview of Statistical Learning
Wage Data
Stock Market Data
Gene Expression Data

## A Brief History of Statistical Learning

Notation and Simple Matrix Algebra
Data Sets Used in Labs and Exercises

## 2 Statistical Learning

2.1 What Is Statistical Learning?
2.1.1 Why Estimate f?
2.1.2 How Do We Estimate f?
2.1.3 The Trade-Off Between Prediction Accuracy and Model Interpretability
2.1.4 Supervised Versus Unsupervised Learning
2.1.5 Regression Versus Classification Problems
2.2 Assessing Model Accuracy
2.2.1 Measuring the Quality of Fit
2.2.2 The Bias-Variance Trade-Off
2.2.3 The Classification Setting
2.3 Lab: Introduction to Python
2.3.1 Getting Started
2.3.2 Basic Commands
2.3.3 Introduction to Numerical Python
2.3.4 Graphics
2.3.5 Sequences and Slice Notation
2.3.6 Indexing Data
2.3.7 Loading Data
2.3.8 For Loops
2.3.9 Additional Graphical and Numerical Summaries
2.4 Exercises
Conceptual
Applied

## 3 Linear Regression

3.1 Simple Linear Regression
3.1.1 Estimating the Coefficients
3.1.2 Assessing the Accuracy of the Coefficient Estimates
3.1.3 Assessing the Accuracy of the Model
3.2 Multiple Linear Regression
3.2.1 Estimating the Regression Coefficients
3.2.2 Some Important Questions
3.3 Other Considerations in the Regression Model
3.3.1 Qualitative Predictors
3.3.2 Extensions of the Linear Model
3.3.3 Potential Problems
3.4 The Marketing Plan
3.5 Comparison of Linear Regression with K-Nearest Neighbors
3.6 Lab: Linear Regression
3.6.1 Importing packages
3.6.2 Simple Linear Regression
3.6.3 Multiple Linear Regression
3.6.4 Multivariate Goodness of Fit
3.6.5 Interaction Terms
3.6.6 Non-linear Transformations of the Predictors
3.6.7 Qualitative Predictors
3.7 Exercises
Conceptual
Applied

## 4 Classification

4.1 An Overview of Classification
4.2 Why Not Linear Regression?
4.3 Logistic Regression
4.3.1 The Logistic Model
4.3.2 Estimating the Regression Coefficients
4.3.3 Making Predictions
4.3.4 Multiple Logistic Regression9
4.3.5 Multinomial Logistic Regression2
4.4 Generative Models for Classification4
4.4.1 Linear Discriminant Analysis for p = 15
4.4.2 Linear Discriminant Analysis for p >16
4.4.3 Quadratic Discriminant Analysis6
4.4.4 Naive Bayes2
4.5 A Comparison of Classification Methods6
4.5.1 An Analytical Comparison6
4.5.2 An Empirical Comparison4
4.6 Generalized Linear Models7
4.6.1 Linear Regression on the Bikeshare Data
4.6.2 Poisson Regression on the Bikeshare Data
4.6.3 Generalized Linear Models in Greater Generality
4.7 Lab: Logistic Regression, LDA, QDA, and KNN9
4.7.1 The Stock Market Data
4.7.2 Logistic Regression
4.7.3 Linear Discriminant Analysis
4.7.4 Quadratic Discriminant Analysis
4.7.5 Naive Bayes
4.7.6 K-Nearest Neighbors
4.7.7 Linear and Poisson Regression on the Bikeshare Data
4.8 Exercises
Conceptual
Applied

## 5 Resampling Methods

5.1 Cross-Validation
5.1.1 The Validation Set Approach
5.1.2 Leave-One-Out Cross-Validation
5.1.3 k-Fold Cross-Validation
5.1.4 Bias-Variance Trade-Off for k-Fold Cross-Validation
5.1.5 Cross-Validation on Classification Problems
5.2 The Bootstrap
5.3 Lab: Cross-Validation and the Bootstrap
5.3.1 The Validation Set Approach
5.3.2 Cross-Validation
5.3.3 The Bootstrap
5.4 Exercises
Conceptual
Applied

## 6 Linear Model Selection and Regularization

6.1 Subset Selection
6.1.1 Best Subset Selection
6.1.2 Stepwise Selection
6.1.3 Choosing the Optimal Model
6.2 Shrinkage Methods
6.2.1 Ridge Regression
6.2.2 The Lasso
6.2.3 Selecting the Tuning Parameter
6.3 Dimension Reduction Methods
6.3.1 Principal Components Regression
6.3.2 Partial Least Squares
6.4 Considerations in High Dimensions
6.4.1 High-Dimensional Data
6.4.2 What Goes Wrong in High Dimensions?
6.4.3 Regression in High Dimensions
6.4.4 Interpreting Results in High Dimensions
6.5 Lab: Linear Models and Regularization Methods
6.5.1 Subset Selection Methods
6.5.2 Ridge Regression and the Lasso
6.5.3 PCR and PLS Regression
6.6 Exercises
Conceptual
Applied

## 7 Moving Beyond Linearity

7.1 Polynomial Regression
7.2 Step Functions
7.3 Basis Functions
7.4 Regression Splines
7.4.1 Piecewise Polynomials
7.4.2 Constraints and Splines
7.4.3 The Spline Basis Representation
7.4.4 Choosing the Number and Locations of the Knots
7.4.5 Comparison to Polynomial Regression
7.5 Smoothing Splines
7.5.1 An Overview of Smoothing Splines
7.5.2 Choosing the Smoothing Parameter λ
7.6 Local Regression
7.7 Generalized Additive Models
7.7.1 GAMs for Regression Problems
7.7.2 GAMs for Classification Problems
7.8 Lab: Non-Linear Modeling
7.8.1 Polynomial Regression and Step Functions
7.8.2 Splines
7.8.3 Smoothing Splines and GAMs
7.8.4 Local Regression
7.9 Exercises
Conceptual
Applied

## 8 Tree-Based Methods

8.1 The Basics of Decision Trees
8.1.1 Regression Trees
8.1.2 Classification Trees
8.1.3 Trees Versus Linear Models
8.1.4 Advantages and Disadvantages of Trees
8.2 Bagging, Random Forests, Boosting, and Bayesian Additive Regression Trees
8.2.1 Bagging
8.2.2 Random Forests
8.2.3 Boosting
8.2.4 Bayesian Additive Regression Trees
8.2.5 Summary of Tree Ensemble Methods
8.3 Lab: Tree-Based Methods
8.3.1 Fitting Classification Trees
8.3.2 Fitting Regression Trees
8.3.3 Bagging and Random Forests
8.3.4 Boosting
8.3.5 Bayesian Additive Regression Trees
8.4 Exercises
Conceptual
Applied

## 9 Support Vector Machines

9.1 Maximal Margin Classifier
9.1.1 What Is a Hyperplane?
9.1.2 Classification Using a Separating Hyperplane
9.1.3 The Maximal Margin Classifier
9.1.4 Construction of the Maximal Margin Classifier
9.1.5 The Non-separable Case
9.2 Support Vector Classifiers
9.2.1 Overview of the Support Vector Classifier
9.2.2 Details of the Support Vector Classifier
9.3 Support Vector Machines
9.3.1 Classification with Non-Linear Decision Boundaries
9.3.2 The Support Vector Machine
9.3.3 An Application to the Heart Disease Data
9.4 SVMs with More than Two Classes
9.4.1 One-Versus-One Classification
9.4.2 One-Versus-All Classification
9.5 Relationship to Logistic Regression
9.6 Lab: Support Vector Machines
9.6.1 Support Vector Classifier
9.6.2 Support Vector Machine
9.6.3 ROC Curves
9.6.4 SVM with Multiple Classes
9.6.5 Application to Gene Expression Data
9.7 Exercises
Conceptual
Applied

## 10 Deep Learning

10.1 Single Layer Neural Networks
10.2 Multilayer Neural Networks
10.3 Convolutional Neural Networks
10.3.1 Convolution Layers
10.3.2 Pooling Layers
10.3.3 Architecture of a Convolutional Neural Network
10.3.4 Data Augmentation
10.3.5 Results Using a Pretrained Classifier
10.4 Document Classification
10.5 Recurrent Neural Networks
10.5.1 Sequential Models for Document Classification
10.5.2 Time Series Forecasting
10.5.3 Summary of RNNs
10.6 When to Use Deep Learning
10.7 Fitting a Neural Network
10.7.1 Backpropagation
10.7.2 Regularization and Stochastic Gradient Descent
10.7.3 Dropout Learning
10.7.4 Network Tuning
10.8 Interpolation and Double Descent
10.9 Lab: Deep Learning
10.9.1 Single Layer Network on Hitters Data
10.9.2 Multilayer Network on the MNIST Digit Data
10.9.3 Convolutional Neural Networks
10.9.4 Using Pretrained CNN Models
10.9.5 IMDB Document Classification
10.9.6 Recurrent Neural Networks
10.10 Exercises
Conceptual
Applied

## 11 Survival Analysis and Censored Data

11.1 Survival and Censoring Times
11.2 A Closer Look at Censoring
11.3 The Kaplan–Meier Survival Curve
11.4 The Log-Rank Test
11.5 Regression Models With a Survival Response
11.5.1 The Hazard Function
11.5.2 Proportional Hazards
11.5.3 Example: Brain Cancer Data
11.5.4 Example: Publication Data
11.6 Shrinkage for the Cox Model
11.7 Additional Topics
11.7.1 Area Under the Curve for Survival Analysis
11.7.2 Choice of Time Scale
11.7.3 Time-Dependent Covariates
11.7.4 Checking the Proportional Hazards Assumption
11.7.5 Survival Trees
11.8 Lab: Survival Analysis
11.8.1 Brain Cancer Data
11.8.2 Publication Data
11.8.3 Call Center Data
11.9 Exercises
Conceptual
Applied

## 12 Unsupervised Learning

12.1 The Challenge of Unsupervised Learning
12.2 Principal Components Analysis
12.2.1 What Are Principal Components?
12.2.2 Another Interpretation of Principal Components
12.2.3 The Proportion of Variance Explained
12.2.4 More on PCA
12.2.5 Other Uses for Principal Components
12.3 Missing Values and Matrix Completion
12.4 Clustering Methods
12.4.1 K-Means Clustering
12.4.2 Hierarchical Clustering
12.4.3 Practical Issues in Clustering
12.5 Lab: Unsupervised Learning
12.5.1 Principal Components Analysis
12.5.2 Matrix Completion
12.5.3 Clustering
12.5.4 NCI60 Data Example
12.6 Exercises
Conceptual
Applied

## 13 Multiple Testing

13.1 A Quick Review of Hypothesis Testing
13.1.1 Testing a Hypothesis
13.1.2 Type I and Type II Errors
13.2 The Challenge of Multiple Testing
13.3 The Family-Wise Error Rate
13.3.1 What is the Family-Wise Error Rate?
13.3.2 Approaches to Control the Family-Wise Error Rate
13.3.3 Trade-Off Between the FWER and Power
13.4 The False Discovery Rate
13.4.1 Intuition for the False Discovery Rate
13.4.2 The Benjamini–Hochberg Procedure
13.5 A Re-Sampling Approach to p-Values and False Discovery Rates
13.5.1 A Re-Sampling Approach to the p-Value
13.5.2 A Re-Sampling Approach to the False Discovery Rate
13.5.3 When Are Re-Sampling Approaches Useful?
13.6 Lab: Multiple Testing
13.6.1 Review of Hypothesis Tests
13.6.2 Family-Wise Error Rate
13.6.3 False Discovery Rate
13.6.4 A Re-Sampling Approach
13.7 Exercises
Conceptual
Applied
