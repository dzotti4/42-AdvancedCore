import matplotlib.pyplot as plt
import numpy as np

from load_image import ft_load


def transpose_array(array):
    """Transpose a 2D array without using a library transpose."""
    result = []
    x = 0
    while x < len(array[0]):
        row = []
        y = 0
        while y < len(array):
            row.append(int(array[y][x]))
            y += 1
        result.append(row)
        x += 1
    return result


def main():
    """Run rotate exercise."""
    array = ft_load("animal.jpeg")

    sliced = array[100:500, 300:700, 0]
    print(f"The shape of image is: {sliced.shape}")
    print(sliced)

    transposed = transpose_array(sliced)
    transposed = np.array(transposed)
    print(f"New shape after Transpose: {transposed.shape}")
    print(transposed)

    plt.imshow(transposed, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
