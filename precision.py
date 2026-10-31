import csv
import json

from train import open_data
from price import load_thetas

# PRECISION CALCULATION
# ------------------------------------------------------------------------------
# To measure the model's precision, we compare the errors made by our linear 
# regression against the errors of a baseline model that always guesses the average price.
# 
# It's a ratio:
# - 0% means the model is no better than just using the average.
# - 100% (or 1) represents a perfect prediction (zero error).
# The closer the result is to 100%, the better the algorithm performs.


data = open_data()
kms = []
prices = []
lin_prices = []

for row in data:
    km = float(row["km"])
    price = float(row["price"])

    kms.append(km)
    prices.append(price)

thetas = load_thetas()

theta0 = thetas["theta0"]
theta1 = thetas["theta1"]

max_price = max(prices)
average_price = sum(prices) / len(prices)

for km in kms:
    lin_prices.append(theta0 + (theta1 * km))

err_av = 0
err_lin = 0

for p in range(len(prices)):
    err_av += (prices[p] - average_price) ** 2
    err_lin += (prices[p] - lin_prices[p]) ** 2

res = 1 - err_lin / err_av

print(f"The precision is : {res * 100}%.")