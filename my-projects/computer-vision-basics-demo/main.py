from pathlib import Path

import numpy as np
from PIL import Image


def create_sample_image(output_path):
    width, height = 256, 256
    image = np.zeros((height, width, 3), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            image[y, x] = [
                x,
                y,
                (x + y) // 2,
            ]

    image[70:180, 90:170] = [255, 255, 255]

    Image.fromarray(image).save(output_path)


def rgb_to_grayscale(image_array):
    red = image_array[:, :, 0]
    green = image_array[:, :, 1]
    blue = image_array[:, :, 2]

    gray = 0.299 * red + 0.587 * green + 0.114 * blue
    return gray.astype(np.uint8)


def apply_convolution(gray_image, kernel):
    height, width = gray_image.shape
    kernel_size = kernel.shape[0]
    pad = kernel_size // 2

    padded = np.pad(gray_image, pad, mode="edge")
    output = np.zeros_like(gray_image, dtype=np.float32)

    for y in range(height):
        for x in range(width):
            region = padded[y:y + kernel_size, x:x + kernel_size]
            output[y, x] = np.sum(region * kernel)

    output = np.clip(output, 0, 255)
    return output.astype(np.uint8)


def main():
    project_dir = Path(__file__).parent
    outputs_dir = project_dir / "outputs"
    outputs_dir.mkdir(exist_ok=True)

    original_path = outputs_dir / "original.png"
    gray_path = outputs_dir / "gray.png"
    edge_path = outputs_dir / "edge.png"
    blur_path = outputs_dir / "blur.png"

    create_sample_image(original_path)

    image = Image.open(original_path).convert("RGB")
    image_array = np.array(image)

    print("Image information")
    print("=" * 50)
    print("Image path:", original_path)
    print("Image shape:", image_array.shape)
    print("Height:", image_array.shape[0])
    print("Width:", image_array.shape[1])
    print("Channels:", image_array.shape[2])
    print("Pixel example at [0, 0]:", image_array[0, 0].tolist())
    print()

    gray_image = rgb_to_grayscale(image_array)
    Image.fromarray(gray_image).save(gray_path)

    edge_kernel = np.array([
        [-1, -1, -1],
        [-1,  8, -1],
        [-1, -1, -1],
    ])

    blur_kernel = np.array([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]) / 9

    edge_image = apply_convolution(gray_image, edge_kernel)
    blur_image = apply_convolution(gray_image, blur_kernel)

    Image.fromarray(edge_image).save(edge_path)
    Image.fromarray(blur_image).save(blur_path)

    print("Saved output images")
    print("=" * 50)
    print("Original image:", original_path)
    print("Gray image:", gray_path)
    print("Edge image:", edge_path)
    print("Blur image:", blur_path)

    print()
    print("Summary")
    print("=" * 50)
    print("A color image is a height x width x channels array.")
    print("A grayscale image has one channel.")
    print("A convolution kernel can detect edges or blur an image.")
    print("CNNs use many learnable kernels to extract visual features.")


if __name__ == "__main__":
    main()