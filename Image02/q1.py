import numpy as np
import matplotlib.pyplot as plt

def create_gradient_image(height, width):
    img = np.zeros((height, width), dtype=np.uint8)

    max_sum = (height - 1) + (width - 1)  # הסכום המקסימלי של y+x
    if max_sum == 0:
        return img  # מקרה של 1x1

    for y in range(height):
        for x in range(width):
            value = int((y + x) * 255.0 / max_sum)
            img[y, x] = value

    return img


# דוגמה לשימוש והצגה:
if __name__ == "__main__":
    g = create_gradient_image(300, 400)
    plt.imshow(g, cmap='gray', vmin=0, vmax=255)
    plt.title("Gradient Image")
    plt.axis('off')
    plt.show()

