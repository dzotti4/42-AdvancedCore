import matplotlib.pyplot as plt

from load_csv import load


def main():
    """Load life expectancy data and display Belgium."""
    dataset = load("life_expectancy_years.csv")
    if dataset is None:
        return

    belgium = dataset[dataset["country"] == "Belgium"]
    if belgium.empty:
        return

    belgium = belgium.drop(columns=["country"])
    years = belgium.columns.astype(int)
    life_expectancy = belgium.iloc[0]

    plt.plot(years, life_expectancy)
    plt.title("Belgium Life Expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == "__main__":
    main()
