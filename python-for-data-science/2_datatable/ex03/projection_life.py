import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

from load_csv import load


def main():
    """Display life expectancy against income for the year 1900."""
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life = load("life_expectancy_years.csv")
    if income is None or life is None:
        return

    income = income[["country", "1900"]]
    life = life[["country", "1900"]]

    income = income.rename(columns={"1900": "income"})
    life = life.rename(columns={"1900": "life_expectency"})

    merged = income.merge(life, on="country")
    merged = merged.dropna()

    plt.scatter(merged["income"], merged["life_expectency"])
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")
    plt.xscale("log")
    plt.gca().xaxis.set_major_formatter(ScalarFormatter())
    plt.show()


if __name__ == "__main__":
    main()
