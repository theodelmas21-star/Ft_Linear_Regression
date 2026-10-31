import csv
import json
import matplotlib.pyplot as plot

from train import open_data

data = open_data()

kms = []
prices = []

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

plot.scatter(kms, prices, color="blue", label="Cars (Real Data)")

min_km = min(kms)
max_km = max(kms)

line_x = [min_km, max_km]
line_y = [theta0 + (theta1 * min_km), theta0 + (theta1 * max_km)]

plot.plot(line_x, line_y, color="red", label="Linear regression")

plot.xlabel("Mileages (km)")
plot.ylabel("Price (€)")
plot.title("Ft_Linear_Regression - Bonus 42")
plot.legend()
plot.grid(True)

plot.show()