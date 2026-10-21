import matplotlib.pyplot as plt


from load_image import ft_load


def ft_invert(array):
    """Inverts the color of the image received."""
    new_array = array.copy()
    new_array = 255 - new_array
    return new_array


def ft_red(array):
    """Keep only the red channel of the image received."""
    new_array = array.copy()
    new_array[:, :, 1] = 0
    new_array[:, :, 2] = 0
    return new_array


def ft_green(array):
    """Keep only the green channel of the image received."""
    new_array = array.copy()
    new_array[:, :, 0] = 0
    new_array[:, :, 2] = 0
    return new_array


def ft_blue(array):
    """Keep only the blue channel of the image received."""
    new_array = array.copy()
    new_array[:, :, 0] = 0
    new_array[:, :, 1] = 0
    return new_array


def ft_grey(array):
    """Convert the image received to grayscale."""
    new_array = array.copy()
    grey = array.mean(axis=2)
    new_array[:, :, 0] = grey
    new_array[:, :, 1] = grey
    new_array[:, :, 2] = grey
    return new_array


def main():
    """Run pimp image exercise."""
    array = ft_load("landscape.jpg")
    print(array)

    inverted = ft_invert(array)
    red = ft_red(array)
    green = ft_green(array)
    blue = ft_blue(array)
    grey = ft_grey(array)

    plt.imshow(array)
    plt.show()

    plt.imshow(inverted)
    plt.show()

    plt.imshow(red)
    plt.show()

    plt.imshow(green)
    plt.show()

    plt.imshow(blue)
    plt.show()

    plt.imshow(grey)
    plt.show()

    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()
