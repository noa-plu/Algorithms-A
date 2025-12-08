
# 3
def parent(i: int) -> int:
    return (i - 1) // 2

def left(i: int) -> int:
    return 2 * i + 1

def right(i: int) -> int:
    return 2 * i + 2


# 4
def is_max_heap(arr, i=0, key=lambda x: x) -> bool:
    n = len(arr)
    for j in range(i * 2 + 1, n):
        p = parent(j)
        if key(arr[p]) < key(arr[j]):
            return False
    return True


# 5
def max_heapify(arr, i, heap_size, key=lambda x: x):
    """מניחה שהעצים ב-left(i), right(i) הם max-heap,
    ו'סידרת' את תת-העץ עם השורש i כך שיהיה max-heap."""
    largest = i
    l = left(i)
    r = right(i)

    # השוואה עם הילד השמאלי
    if l < heap_size and key(arr[l]) > key(arr[largest]):
        largest = l

    # השוואה עם הילד הימני
    if r < heap_size and key(arr[r]) > key(arr[largest]):
        largest = r

    # אם אחד הילדים גדול מהשורש – מחליפים וממשיכים רקורסיבית
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, heap_size, key=key)



# 6
def build_max_heap(arr, key=lambda x: x):
    n = len(arr)
    # כל האיברים מ-n//2 ואילך הם עלים; עוברים מהאמצע אחורה
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, i, n, key=key)


# 7
def heap_sort(arr, key=lambda x: x):
    n = len(arr)
    # בונים max-heap
    build_max_heap(arr, key=key)

    # בכל צעד – מעבירים את המקסימום לסוף ומקטינים את ה-heap
    for end in range(n - 1, 0, -1):
        # המקסימום נמצא ב-arr[0]
        arr[0], arr[end] = arr[end], arr[0]
        # מסדרים מחדש את הערימה עבור הגודל החדש
        max_heapify(arr, 0, end, key=key)

    return arr

