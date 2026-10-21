def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage


def load_model(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        if len(lines) != 2:
            print("Error: invalid model file.")
            return None

        theta0 = float(lines[0].strip())
        theta1 = float(lines[1].strip())

        return theta0, theta1

    except FileNotFoundError:
        return 0, 0

    except ValueError:
        print("Error: invalid model values.")
        return None


def main():
    model = load_model("model.txt")

    if model is None:
        return

    theta0, theta1 = model

    mileage = input("Enter mileage: ")

    try:
        mileage = float(mileage)

    except ValueError:
        print("Error: mileage must be a number.")
        return

    if mileage < 0:
        print("Error: mileage cannot be negative.")
        return

    estimated_price = estimate_price(mileage, theta0, theta1)

    print(f"Estimated price: {estimated_price}")

if __name__ == "__main__":
    main()
