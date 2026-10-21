from PIL import Image
import numpy as np


def ft_load(path: str):
    """Load an image and return its RGB pixel array."""
    try:
        image = Image.open(path)
        image = image.convert("RGB")
        array = np.array(image)
        print(f"The shape of image is: {array.shape}")
        return array
    except Exception as error:
        print(f"Error: {error}")
        return None


def main():
    """Run basic tests."""
    print(ft_load("animal.jpg"))


if __name__ == "__main__":
    main()
