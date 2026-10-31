import csv
import json

def estimate_price(mileage):
    with open("thetas.json", "r") as f:
        thetas = json.load(f)
    theta0 = thetas["theta0"]
    theta1 = thetas["theta1"]

    price = theta0 + (theta1 * mileage)
    
    return price

def print_price(inp):
    try:
        mileage = float(inp)
    except:
        print("You have to write a number")
        return

    #5,4 millions is the actual record of mileage for a car
    if (mileage > 5_400_000):
         print("You have to write a number between 0 an 5,4 millions")
         return

    price = estimate_price(mileage)

    print(f"The estimate price is {price}.")

if __name__ == "__main__":
    print("What's the mileage of your car ?")
    inp = input()
    print_price(inp)