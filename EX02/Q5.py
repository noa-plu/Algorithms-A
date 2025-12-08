def partition_two_pivots(a, key):
    """
    מחלקת את הרשימה a לשלושה קטעים לפי שני פיבוטים:
    pivot1 = האיבר הראשון, pivot2 = האיבר האחרון (אחרי סידור ביניהם).

    אחרי הקריאה מתקיים:
    - a[:i1]        : key(x) < key(pivot1)
    - a[i1+1:i2]    : key(pivot1) <= key(x) <= key(pivot2)
    - a[i2+1:]      : key(x) > key(pivot2)

    הפונקציה מחזירה את שני האינדקסים (i1, i2) – המיקומים הסופיים של שני הפיבוטים.
    """
    n = len(a)
    if n == 0:
        return -1, -1
    if n == 1:
        return 0, 0

    # בוחרים את האיבר הראשון והאחרון כפיבוטים
    if key(a[0]) > key(a[-1]):
        a[0], a[-1] = a[-1], a[0]  # דואגים ש-pivot1 <= pivot2

    pivot1 = a[0]
    pivot2 = a[-1]
    k1 = key(pivot1)
    k2 = key(pivot2)

    # lt – הגבול של הקטע הראשון (< pivot1)
    # i  – הסורק
    # gt – הגבול של הקטע האחרון (> pivot2)
    lt = 1
    i = 1
    gt = n - 2

    while i <= gt:
        k = key(a[i])
        if k < k1:
            # שייך לקטע הראשון: להחליף עם lt ולהתקדם בשניהם
            a[i], a[lt] = a[lt], a[i]
            lt += 1
            i += 1
        elif k > k2:
            # שייך לקטע האחרון: להחליף עם gt ולהקטין את gt
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
            # לא מקדמים את i, כי צריך לבדוק את האיבר שהבאנו מ-gt
        else:
            # שייך לקטע האמצעי – פשוט להתקדם
            i += 1

    # עכשיו שמים את הפיבוטים במקומות שלהם:
    lt -= 1
    gt += 1
    a[0], a[lt] = a[lt], a[0]
    a[-1], a[gt] = a[gt], a[-1]

    # a[:lt]        : < pivot1
    # a[lt]         : pivot1
    # a[lt+1:gt]    : בין שני הפיבוטים
    # a[gt]         : pivot2
    # a[gt+1:]      : > pivot2
    return lt, gt


a = [9, 2, 7, 1, 5, 8, 3, 6, 4]
i1, i2 = partition_two_pivots(a, key=lambda x: x)
print("אינדקסים:", i1, i2)
print("אחרי partition:", a)