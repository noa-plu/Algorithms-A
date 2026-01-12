import cv2 as cv
import numpy as np

def brighten(img, b, func):
    """
    img - תמונה בגווני אפור (np.uint8)
    b   - מספר שלם להוספה
    func - "np" או "cv"
    """
    if func == "np":
        # np.add עם סוג uint8 – חיבור מודולו 256 (גלישה)
        result = np.add(img, b, dtype=np.uint8)
    elif func == "cv2":
        # cv2.add – חיבור עם Saturation (חיתוך ב-0..255)
        # כדי להוסיף קבוע, ניתן להעביר מטריצה באותו גודל
        result = cv.add(img, b)
    else:
        raise ValueError('func must be "np" or "cv"')

    return result
