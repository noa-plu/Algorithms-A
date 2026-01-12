import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import q1
import q2


if __name__ == "__main__":
    g = q1.create_gradient_image(300, 300)

    bright_np = q2.brighten(g, 100, "np")
    bright_cv = q2.brighten(g, 100, "cv2")

    plt.figure(figsize=(10, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(g, cmap='gray', vmin=0, vmax=255)
    plt.title("Original")
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(bright_np, cmap='gray', vmin=0, vmax=255)
    plt.title("brighten (np)")
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(bright_cv, cmap='gray', vmin=0, vmax=255)
    plt.title("brighten (cv)")
    plt.axis('off')

    plt.tight_layout()
    plt.show()
