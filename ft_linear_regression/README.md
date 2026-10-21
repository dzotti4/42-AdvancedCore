*This project has been created as part of the 42 curriculum by dzotti.*

# ft_linear_regression

## Description

An introduction to machine learning: predicting the price of a car from its mileage with a linear function

`estimatePrice(mileage) = θ0 + θ1 × mileage`

`train.py` learns θ0 and θ1 from `data.csv` with gradient descent (both thetas updated at the same time, mileages scaled for a stable learning rate) and saves them in `model.txt`. `predict.py` asks for a mileage and prints the estimated price; before training, both thetas are 0.

## Instructions

```bash
python3 train.py        # learns θ0 and θ1, writes model.txt
python3 predict.py      # asks for a mileage, prints the estimated price
```

Bonus:

```bash
python3 plot_data.py    # the data as a scatter plot
python3 plot_result.py  # the data with the regression line
python3 precision.py    # the average price error of the model
```

The plots need `matplotlib`. Invalid input (non-numbers, negative values, a broken csv or model file) prints a clear error.

## What I learned

- Gradient descent and how the learning rate and feature scaling affect it
- Checking a model against the exact least-squares solution
