import csv
import json

def train():

    # Load the CSV file into a list of dicts (one dict per row)
    try:
        with open("data.csv", "r") as f:
            reader = csv.DictReader(f)
            data = list(reader)
    except (OSError, csv.Error):
        print('Warning: Failed to load file.')
        return

    # Find the min and max of km and price, needed for min-max normalisation.
    # Initialised with the first row so they are always real values from the data
    max_km = float(data[0]["km"])
    max_price = float(data[0]["price"])
    min_price = float(data[0]["price"])
    min_km = float(data[0]["km"])
    len_data = len(data)

    for m in data:
        cur_km = float(m["km"])
        cur_price = float(m["price"])
        
        if(cur_km > max_km):
            max_km = cur_km
        if(cur_km < min_km):
            min_km = cur_km

        if(cur_price > max_price):
            max_price = cur_price
        if(cur_price < min_price):
            min_price = cur_price

    # Learning rate: too high and the descent diverges, too low and it needs
    # many more iterations to converge
    learning_rate = 0.1
    theta0_normed = 0
    theta1_normed = 0

    # Normalise km and price to [0, 1] once, before training, instead of
    # recomputing them at every iteration
    mileages_normed = []
    prices_normed = []

    for j in data:
        mileage_normed = ((float(j["km"])) - min_km) / (max_km - min_km)
        price_normed = (float(j["price"]) - min_price) / (max_price - min_price)

        mileages_normed.append(mileage_normed)
        prices_normed.append(price_normed)

# Gradient descent: at each iteration, compute the sums of the errors over
# the whole dataset, then update both thetas simultaneously    
    for i in range(10000):
        somme = 0
        somme_x_mileage = 0

        for x, y in zip(mileages_normed, prices_normed):
            estimate_price = theta0_normed + (theta1_normed * x)
            gap = estimate_price - y

            somme += gap
            somme_x_mileage += gap * x

        theta0_normed = theta0_normed - learning_rate * (1 / len_data) * somme
        theta1_normed = theta1_normed - learning_rate * (1 / len_data) * somme_x_mileage
    # Convert the thetas back to the real scale (km and euros),
    # so that price = theta0 + theta1 * km works on raw mileages
    theta1 = theta1_normed * (max_price - min_price) / (max_km - min_km)
    theta0 = min_price + (max_price - min_price) * theta0_normed - theta1 * min_km

    thetas = {"theta0": theta0, "theta1": theta1}

    # Save the thetas for the prediction program
    try:
        with open("thetas.json", "w") as f:
            json.dump(thetas, f)
    except (OSError):
        print('Warning: Failed write thetas.json .')
        return


train()
