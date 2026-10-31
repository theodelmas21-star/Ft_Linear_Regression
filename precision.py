import csv
import json

from train import open_data

data = open_data()

kms = []
prices = []
lin_prices = []

for row in data:
    km = float(row["km"])
    price = float(row["price"])

    kms.append(km)
    prices.append(price)

try:
    with open("thetas.json", "r") as f:
        thetas = json.load(f)
except (OSError):
    print('Warning: Failed to load thetas.json.')
    exit(1)

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