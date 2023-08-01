# Stock Data Analysis

## Table of contents
* [General info](#general-info)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Testing](#testing)
* [Solutions](#solutions)
* [Future Plans](#future-plans)
* [Inspirations and Acknowledgments](#inspirations-and-acknowledgments)

## General info
This program performs a basic analysis of historical Facebook (FB) stock data. It reads the data from a CSV file, cleans it, and calculates the 14-day moving average of the stock's closing prices. The data is then plotted to visualize the closing price, moving average, and volume.

## Features
* Reading and cleaning historical stock data from a CSV file
* Calculating the 14-day moving average of the stock's closing prices
* Plotting the closing price, moving average, and volume on the same graph

## Technologies Used
The program is written in Python.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Prerequisites
To run this project, make sure you have Python 3.11.2 and the required libraries installed on your computer.  

If you haven't installed the pandas library yet, you can do so by running:

```
   pip install pandas 
```
## Setup
To run the project locally, follow these steps:

1. Clone this repository to your local machine or download the `fb.csv` file containing the historical stock data of Facebook.
2. Navigate to the project directory.
3. Run the program: using the command prompt or terminal:
```
python3 stock_data_analysis.ipynb
```

## Testing
This project includes unit tests for the `clean_data` function using `pytest`. The tests are written in the `test_stock_data_analysis.py` file.

The unit tests verify the correctness of the `clean_data` function. They cover aspects such as value conversion correctness, data type correctness, data integrity, and ensuring the original DataFrame remains unchanged.

### Running Tests
To run the tests, follow these steps:

1. Install pytest if you haven't already, by:
``` 
pip3 install pytest
```
2. Navigate to the project directory.

3. Run the tests by running the following command in the terminal:
```
pytest `test_stock_data_analysis.py`
```

## Solutions
The program uses the clean_data function to remove dollar signs from certain columns and convert them to float. It then calculates the 14-day moving average of the closing prices using the Pandas rolling function. The final result is a plot that displays the closing price, moving average, and volume of FB stock.

## Future Plans
This program can be further expanded to include more advanced analysis and visualization features, such as:

- Adding other technical indicators (e.g., Relative Strength Index, Moving Average Convergence Divergence) to gain more insights into the stock's performance.
-Incorporating machine learning models to predict future stock prices based on historical data.


## Inspirations and Acknowledgments
The program was adapted during the "Practical Python" training course. Thanks for the inspiring material and support!