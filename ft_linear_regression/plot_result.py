import os
import matplotlib.pyplot as plt

from train import load_data
from predict import load_model, estimate_price


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
    
    sorted_mileages = sorted(mileages)
    predicted_prices = []

    for mileage in sorted_mileages:
        predicted_price = estimate_price(mileage, theta0, theta1)
        predicted_prices.append(predicted_price)

    plt.scatter(mileages, prices)
    plt.plot(sorted_mileages, predicted_prices)
    plt.xlabel("Mileage")
    plt.ylabel("Price")
    plt.title("Linear regression result")
    plt.show()


if __name__ == "__main__":
    main()
