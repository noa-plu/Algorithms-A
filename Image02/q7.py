import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import q4

def to_binary(gray_img, thresh=128):
    """
    ממירה תמונה לגווני אפור לבינארית (שחור/לבן)
    """
    # אפשר cv.threshold, אבל גם ידני:
    _, binary = cv.threshold(gray_img, thresh, 255, cv.THRESH_BINARY)
    return binary


def compute_histogram(gray_img):
    """
    מחשבת היסטוגרמה ידנית לערכים 0..255
    החזרה: מערך בגודל 256 שבו hist[i] = כמות פיקסלים עם עוצמה i
    """
    hist = np.zeros(256, dtype=np.int64)
    h, w = gray_img.shape

    for y in range(h):
        for x in range(w):
            val = gray_img[y, x]
            hist[val] += 1

    return hist


def show_histogram(hist):
    """
    מציג היסטוגרמה בעזרת matplotlib
    """
    plt.figure()
    plt.bar(np.arange(256), hist)
    plt.title("Histogram")
    plt.xlabel("Gray Level")
    plt.ylabel("Count")
    plt.xlim([0, 255])
    plt.show()


if __name__ == "__main__":
    # קריאה כתמונה צבעונית ואז לגווני אפור
    # ליצור תמונה כמו בשאלה 4
    img_bw = q4.create_low_contrast_image(300, 300, 100, 105)
    # img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

    # שחור/לבן
    # img_bw = to_binary(img_gray, thresh=128)

    # היסטוגרמה של התמונה הבינארית (יהיו בעיקר שני עמודים: 0 ו-255)
    hist_bw = compute_histogram(img_bw)

    # הצגה
    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.imshow(img_bw, cmap='gray', vmin=0, vmax=255)
    plt.title("Black & White")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.bar(np.arange(256), hist_bw)
    plt.title("Histogram (BW)")
    plt.xlabel("Gray Level")
    plt.ylabel("Count")
    plt.xlim([0, 255])

    plt.tight_layout()
    plt.show()
