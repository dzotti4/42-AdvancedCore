import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

from load_csv import load


def convert_population(value):
    """Convert population value with k, M or B suffix to float."""
    if isinstance(value, str) is False:
        return value
    if value.endswith("k"):
        return float(value[:-1]) * 1000
    if value.endswith("M"):
        return float(value[:-1]) * 1000000
    if value.endswith("B"):
        return float(value[:-1]) * 1000000000
    return float(value)


def millions_formatter(value, position):
    """Format y-axis population values in millions."""
    millions = round(value / 1000000)
    return str(millions) + "M"


def main():
    """Load population data and compare Belgium with France."""
    dataset = load("population_total.csv")
    if dataset is None:
        return

    belgium = dataset[dataset["country"] == "Belgium"]
    france = dataset[dataset["country"] == "France"]
    if belgium.empty or france.empty:
        return

    years = [str(year) for year in range(1800, 2051)]
    years_as_int = [int(year) for year in years]

    belgium_values = belgium[years].iloc[0].apply(convert_population)
    france_values = france[years].iloc[0].apply(convert_population)

    plt.plot(years_as_int, belgium_values, label="Belgium")
    plt.plot(years_as_int, france_values, label="France")
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()
    plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))
    plt.show()


if __name__ == "__main__":
    main()
