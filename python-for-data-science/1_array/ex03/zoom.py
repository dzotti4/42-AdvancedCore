import matplotlib.pyplot as plt

from load_image import ft_load


def main():
    """Run zoom exercise."""
    array = ft_load("animal.jpeg")
    print(array)

    zoomed = array[100:500, 300:700, 0:1]
    print(f"New shape after slicing: {zoomed.shape}")
    print(zoomed)

    plt.imshow(zoomed[:, :, 0], cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
