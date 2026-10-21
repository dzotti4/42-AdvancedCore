import csv


def load_data(filename):
    mileages = []
    prices = []

    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            
            if reader.fieldnames != ["km", "price"]:
                print("Error: csv must contain only 'km' and 'price' columns.")
                return None

            for row in reader:
                if None in row:
                    print("Error: csv contains too many values on one line.")
                    return None

                mileage_value = row["km"]
                price_value = row["price"]
                
                if mileage_value is None or mileage_value.strip() == "":
                    print("Error: missing mileage value.")
                    return None

                if price_value is None or price_value.strip() == "":
                    print("Error: missing price value.")
                    return None

                mileage = float(mileage_value.strip())
                price = float(price_value.strip())
                
                if mileage < 0:
                    print("Error: mileage cannot be negative.")
                    return None

                if price < 0:
                    print("Error: price cannot be negative.")
                    return None

                mileages.append(mileage)
                prices.append(price)
    
    except FileNotFoundError:
        print("Error: data.csv not found.")
        return None

    except ValueError:
        print("Error: csv contains invalid number values.")
        return None

    if len(mileages) == 0:
        print("Error: csv is empty")
        return None

    return mileages, prices



def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage


def scale_mileages(mileages, max_mileage):
    scaled_mileages = []

    for mileage in mileages:
        scaled_mileage = mileage / max_mileage
        scaled_mileages.append(scaled_mileage)

    return scaled_mileages


def train_once(mileages, prices, theta0, theta1, learning_rate):
    sum_error = 0
    sum_error_mileage = 0
    m = len(mileages)

    for i in range(m):
        prediction = estimate_price(mileages[i], theta0, theta1)
        error = prediction - prices[i]

        sum_error += error
        sum_error_mileage += error * mileages[i]

    new_theta0 = theta0 - learning_rate * (sum_error / m)
    new_theta1 = theta1 - learning_rate * (sum_error_mileage / m)

    theta0 = new_theta0
    theta1 = new_theta1

    return theta0, theta1


def save_model(filename, theta0, theta1):
    with open(filename, "w") as file:
        file.write(f"{theta0}\n")
        file.write(f"{theta1}\n")


def main():
    data = load_data("data.csv")
    if data is None:
        return

    mileages, prices = data

    max_mileage = max(mileages)
    if max_mileage == 0:
        print("Error: max mileage cannot be zero.")
        return

    scaled_mileages = scale_mileages(mileages, max_mileage)

    theta0 = 0
    theta1 = 0
    learning_rate = 0.1
    iterations = 100000

    for i in range(iterations):
        theta0, theta1 = train_once(scaled_mileages, prices, theta0, theta1, learning_rate)

    theta0_raw = theta0
    theta1_raw = theta1 / max_mileage

    save_model("model.txt", theta0_raw, theta1_raw)


if __name__ == "__main__":
    main()
