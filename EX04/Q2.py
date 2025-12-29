import random

def quick_kth(arr, left, right, k, key=lambda x: x):

    if left == right:
        return arr[left]

    # בחירת pivot אקראי כדי לשפר את המקרה הממוצע
    pivot_index = random.randint(left, right)
    pivot_value = key(arr[pivot_index])

    # מעבירים את ה-pivot לסוף
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

    # Lomuto partition לפי key
    store_index = left
    for i in range(left, right):
        if key(arr[i]) < pivot_value:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1

    # מחזירים את ה-pivot למקום הסופי שלו
    arr[store_index], arr[right] = arr[right], arr[store_index]

    # איפה ה-k ביחס לפיווט?
    if k == store_index:
        return arr[store_index]
    elif k < store_index:
        return quick_kth(arr, left, store_index - 1, k, key=key)
    else:
        return quick_kth(arr, store_index + 1, right, k, key=key)


arr = [{"name": "a", "age": 30},
       {"name": "b", "age": 20},
       {"name": "c", "age": 40}]

# מוצא את האיבר עם הגיל האמצעי
mid = quick_kth(arr, 0, len(arr)-1, 1, key=lambda p: p["age"])
print(mid)
