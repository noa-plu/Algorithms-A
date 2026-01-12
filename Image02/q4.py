import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def create_low_contrast_image(height, width, fg, bg):
    """
    fg - רקע
    bg - חזית (הצורה)
    """
    img = np.full((height, width), fg, dtype=np.uint8)

    # נצייר מעגל במרכז
    center = (width // 2, height // 2)
    radius = min(height, width) // 4

    cv.circle(img, center, radius, bg, thickness=-1)  # -1 = מילוי מלא
    return img


if __name__ == "__main__":
    low_contrast = create_low_contrast_image(300, 300, fg=100, bg=105)
    plt.imshow(low_contrast, cmap='gray', vmin=0, vmax=255)
    plt.title("Low Contrast Image")
    plt.axis('off')
    plt.show()
