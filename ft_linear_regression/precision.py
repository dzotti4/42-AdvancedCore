import os

from train import load_data
from predict import load_model, estimate_price


def calculate_average_price_error(mileages, prices, theta0, theta1):
    total_error = 0
    m = len(mileages)

    for i in range(m):
        prediction = estimate_price(mileages[i], theta0, theta1)
        error = prediction - prices[i]

        if error < 0:
           error =  error * -1

        total_error += error

    average_error = total_error / m
    
    return average_error



def main():
    if os.path.exists("model.txt") is False:
        print("Error: model.txt not found. Run train.py first.")
        return

    model = load_model("model.txt")

    if model is None:
        return

    data = load_data("data.csv")
    
    if data is None:
        return

    theta0, theta1 = model
    mileages, prices = data

    average_error = calculate_average_price_error(mileages, prices, theta0, theta1)


    print(f"theta0: {theta0}")
    print(f"theta1: {theta1}")
    print(f"number of cars: {len(mileages)}")
    print(f"average price error: {average_error}")


if __name__ == "__main__":
    main()
