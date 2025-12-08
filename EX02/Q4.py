# א
def partition_lomuto(a, key):
    """
    מממשת חלוקה (partition) בשיטת Lomuto.
    משתמשת באיבר האחרון כ-pivot.
    :param a: רשימה לא ממוינת (תשתנה במקום)
    :param key: פונקציה שמחזירה מפתח מכל פריט
    :return: אינדקס int – המקום הסופי של ה-pivot
    """
    # נבחר את האיבר האחרון כ-pivot
    pivot = a[-1]
    pivot_key = key(pivot)

    # i מסמן את סוף האזור של "קטנים או שווים ל-pivot"
    i = -1

    # עוברים על כל האיברים חוץ מהאחרון (שהוא ה-pivot)
    for j in range(len(a) - 1):
        if key(a[j]) <= pivot_key:
            i += 1
            a[i], a[j] = a[j], a[i]  # החלפה

    # עכשיו שמים את ה-pivot אחרי כל הקטנים/שווים
    a[i + 1], a[-1] = a[-1], a[i + 1]
    return i + 1


a = [(5,), (2,), (9,), (1,), (7,)]
idx = partition_lomuto(a, key=lambda t: t[0])
# print(idx)


# ב

def partition_hoare(a, key):
    """
    חלוקה (partition) בשיטת Hoare על כל הרשימה a.
    :param a: רשימה לא ממוינת (תשתנה במקום)
    :param key: פונקציה שמחזירה מפתח מכל פריט
    :return: אינדקס שמחלק את הרשימה לשתי קבוצות:
             אינדקסים <= החזרה: ערכים עם key <= pivot
             אינדקסים > החזרה: ערכים עם key >= pivot
    """
    if not a:
        return -1  # אין על מה לעבוד

    pivot_key = key(a[0])      # הפיבוט – לפי האיבר הראשון
    i = 0
    j = len(a) - 1

    while True:
        # להזיז את i ימינה עד שנעצור על איבר ש- key שלו >= pivot_key
        while key(a[i]) < pivot_key:
            i += 1

        # להזיז את j שמאלה עד שנעצור על איבר ש- key שלו <= pivot_key
        while key(a[j]) > pivot_key:
            j -= 1
        print(i, j)
        # אם המצביעים נפגשו או חצו – סיימנו
        if i >= j:
            print(a)
            return j+1 # j הוא "נקודת החלוקה"

        # אחרת – להחליף בין a[i] ל-a[j] ולהמשיך
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

a1 = [(5,), (2,), (9,), (1,), (7,)]
idx1 = partition_hoare(a1, key=lambda t: t[0])
print(idx1)