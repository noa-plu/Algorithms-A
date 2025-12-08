def merge(a, b, key):

    i = j = 0
    result = []

    # כל עוד יש איברים בשתי הרשימות
    while i < len(a) and j < len(b):
        if key(a[i]) <= key(b[j]):
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    # מה שנשאר בסוף באחת הרשימות – להעתיק כמו שהוא
    result.extend(a[i:])
    result.extend(b[j:])

    return result

def merge_sorted_lists(lists, key):
    if not lists:
        return []
    result = lists[0]
    for lst in lists[1:]:
        result = merge(result, lst, key)
    return result




lists = [
    [(0,), (4,), (9,)],
    [(1,), (3,), (10,)],
    [(2,), (5,), (6,), (7,)]
]

merged = merge_sorted_lists(lists, key=lambda t: t[0])
print(merged)


#

# import heapq
#
#
# def merge_sorted_lists(lists, key):
#     """
#     ממזגת כמה רשימות מסודרות לרשימה אחת מסודרת, לפי פונקציית key.
#
#     :param lists: רשימה של רשימות ממוינות בסדר עולה
#     :param key: פונקציה שמקבלת פריט ומחזירה מפתח להשוואה
#     :return: רשימה חדשה, ממוזגת וממוינת
#     """
#     heap = []
#     result = []
#
#     # הכנסה ראשונית להיפ – האיבר הראשון מכל רשימה
#     for list_idx, lst in enumerate(lists):
#         if lst:  # רק אם הרשימה לא ריקה
#             first_item = lst[0]
#             heapq.heappush(heap, (key(first_item), list_idx, 0, first_item))
#
#     # מיזוג באמצעות היפ
#     while heap:
#         _, list_idx, item_idx, value = heapq.heappop(heap)
#         result.append(value)
#
#         next_idx = item_idx + 1
#         if next_idx < len(lists[list_idx]):
#             next_item = lists[list_idx][next_idx]
#             heapq.heappush(
#                 heap,
#                 (key(next_item), list_idx, next_idx, next_item)
#             )
#
#     return result



# def merge_sorted_lists( lists, key):
#
#     if not lists:
#         return []
#
#     temp = lists[0]
#
#     for k in range(1, len(lists)):
#         current = lists[k]
#         result = []
#         i = j = 0
#         while i < len(temp) and j < len(current):
#             if key(temp[i]) <= key(current[j]):
#                 result.append(temp[i])
#                 i += 1
#             else:
#                 result.append(current[j])
#                 j += 1
#
#     # מה שנשאר בסוף באחת הרשימות – להעתיק כמו שהוא
#         result.extend(temp[i:])
#         result.extend(current[j:])
#         temp=result
#
#     return temp

