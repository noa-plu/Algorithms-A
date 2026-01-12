# import cv2
# import numpy as np
#
# def convert_to_grayscale(image_bgr):
#     """
#     קולט תמונה בפורמט BGR (כמו ש-cv2.imread מחזיר),
#     ומחזיר תמונה בגווני אפור (uint8).
#     """
#     if image_bgr is None:
#         raise ValueError("convert_to_grayscale: image is None")
#
#     gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
#     return gray
#
# def normalize_gray(gray):
#     """
#     קולט תמונת אפור (uint8 או float),
#     מחשב min, max, mean, ופקטור 255/(max-min),
#     מחזיר: (normalized_uint8, stats_dict)
#
#     מבצע clipping ל-0..255.
#     לא משתמש ב-cv2.normalize.
#     """
#
#     if gray is None:
#         raise ValueError("normalize_gray: gray is None")
#
#     # נוודא עבודה ב-float לחישובים
#     g = gray.astype(np.float32)
#
#     # מותר להשתמש ב-min/max של np או של cv2.
#     # דוגמה עם cv2.minMaxLoc (כמו שהרמז מציע):
#     min_val, max_val, _, _ = cv2.minMaxLoc(g)
#
#     mean_val = float(np.mean(g))
#
#     # להימנע מחלוקה באפס אם התמונה קבועה
#     denom = (max_val - min_val)
#     if denom == 0:
#         factor = 0.0
#         out = np.zeros_like(g, dtype=np.uint8)
#         stats = {
#             "min": float(min_val),
#             "max": float(max_val),
#             "mean": mean_val,
#             "factor": factor
#         }
#         return out, stats
#
#     factor = 255.0 / denom
#
#     # normalization ידני:
#     # (x - min) * 255/(max-min)
#     norm = (g - min_val) * factor
#
#     # clipping כדי שלא יברח מחוץ לטווח
#     norm = np.clip(norm, 0, 255)
#
#     out = norm.astype(np.uint8)
#
#     stats = {
#         "min": float(min_val),
#         "max": float(max_val),
#         "mean": mean_val,
#         "factor": float(factor)
#     }
#     return out, stats
#
# def main():
#     # שנה/י לשם הקובץ שלך
#     image_path = "img.png"
#
#     img = cv2.imread(image_path)
#     if img is None:
#         raise ValueError(f"לא ניתן לקרוא את התמונה: {image_path}")
#
#     gray = convert_to_grayscale(img)
#     normalized, stats = normalize_gray(gray)
#
#     print("min =", stats["min"])
#     print("max =", stats["max"])
#     print("mean =", stats["mean"])
#     print("factor = 255/(max-min) =", stats["factor"])
#
#     # הצגה
#     cv2.imshow("Gray", gray)
#     cv2.imshow("Normalized (manual + clipping)", normalized)
#
#     # שמירה (לא חובה, אבל שימושי)
#     cv2.imwrite("normalized.png", normalized)
#
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
# if __name__ == "__main__":
#     main()

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import q4

def print_image_stats(gray_img):
    # בעזרת numpy
    min_val = gray_img.min()
    max_val = gray_img.max()
    mean_val = gray_img.mean()

    factor = 255.0 / (max_val - min_val)  # פקטור מתיחה מקסימלי בלי clipping

    print("min:", min_val)
    print("max:", max_val)
    print("mean:", mean_val)
    print("stretch factor (255/(max-min)):", factor)

    # לחלופין, אפשר בעזרת cv2.minMaxLoc:
    # min_val_cv, max_val_cv, min_loc, max_loc = cv.minMaxLoc(gray_img)


def normalize(gray_img):
    """
    מבצע נרמול כך שהמינימום יהפוך ל-0 והמקסימום ל-255
    """
    img_f = gray_img.astype(np.float32)
    min_val = img_f.min()
    max_val = img_f.max()

    if max_val == min_val:
        # תמונה קבועה – נחזיר 0
        return np.zeros_like(gray_img, dtype=np.uint8)

    norm = (img_f - min_val) * 255.0 / (max_val - min_val)
    norm = np.clip(norm, 0, 255)
    return norm.astype(np.uint8)


if __name__ == "__main__":
    # יצירת התמונה (זו הקריאה של שאלה 4)
    img_gray = q4.create_low_contrast_image(300, 300, 100, 105)

    # הדפס סטטיסטיקה לפני נרמול
    print("לפני Normalize:")
    print_image_stats(img_gray)

    # הרצה של נרמול
    img_norm = normalize(img_gray)

    print("אחרי Normalize:")
    print_image_stats(img_norm)

    # הצגה
    plt.subplot(1, 2, 1)
    plt.imshow(img_gray, cmap='gray', vmin=0, vmax=255)
    plt.title("Original low contrast")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(img_norm, cmap='gray', vmin=0, vmax=255)
    plt.title("Normalized")
    plt.axis('off')

    plt.show()



