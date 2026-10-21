import matplotlib.pyplot as plt

from train import load_data


def main():
    data = load_data("data.csv")

    if data is None:
        return

    mileages, prices = data
    
    plt.scatter(mileages, prices)
    plt.xlabel("Mileages")
    plt.ylabel("Price")
    plt.title("Car prices by mileages")
    plt.show()


if __name__ == "__main__":
    main()
