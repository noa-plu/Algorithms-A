import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import q5

if __name__ == "__main__":

    # שינוי שני פיקסלים

    img_gray = q5.q4.create_low_contrast_image(300, 300, 100, 105)
    img_modified = img_gray.copy()
    img_modified[0, 0] = 0       # פיקסל אחד ל-0
    img_modified[0, 1] = 255     # פיקסל אחד ל-255

    print("לפני normalization (עם פיקסלים קיצוניים):")
    q5.print_image_stats(img_modified)

    img_norm2 =q5.normalize(img_modified)

    print("אחרי normalization (עם פיקסלים קיצוניים):")
    q5.print_image_stats(img_norm2)

    plt.figure(figsize=(10, 4))
    plt.subplot(1, 3, 1)
    plt.imshow(img_gray, cmap='gray', vmin=0, vmax=255)
    plt.title("Original")
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(img_modified, cmap='gray', vmin=0, vmax=255)
    plt.title("Modified (0 & 255)")
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(img_norm2, cmap='gray', vmin=0, vmax=255)
    plt.title("Normalized after modification")
    plt.axis('off')

    plt.tight_layout()
    plt.show()
