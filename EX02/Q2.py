from winreg import HKEY_CLASSES_ROOT


def create_random_tuples(n, k, types=None):
    """
    Create a list of n tuples, each containing k random elements of specified types.

    Parameters:
    n (int): Number of tuples to create.
    k (int): Number of elements in each tuple.
    types (list): List of types for each element in the tuple. Length must be k.

    Returns:
    list: A list of n tuples with random elements.
    """
    import random
    import string

    if types is None:
        types = [int] * k  # Default to int if no types provided

    if len(types) != k:
        raise ValueError("Length of types must be equal to k")

    def random_element(t):
        if t == int:
            return random.randint(0, 1000)
        elif t == float:
            return random.uniform(0.0, 1000.0)
        elif t == str:
            return ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        else:
            raise ValueError(f"Unsupported type: {t}")

    result = []
    for _ in range(n):
        tuple_elements = tuple(random_element(t) for t in types)
        result.append(tuple_elements)

    return result


# ////// עד כאן הפונקציה המועתקת מהתרגיל

# א

def merge(a, b, key):
    # תוספת לפי הבקשה בחלק ב
    if not is_sorted(a, key) or not is_sorted(b, key):
        return None

    i = 0
    j = 0
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


# ב
# def is_sorted(a, key):
#     for i in range(len(a)-1):
#         if key(a[i]) > key(a[i+1]):
#             return False
#     return True

from itertools import pairwise

def is_sorted(a, key):
    return all(key(x) <= key(y) for x, y in pairwise(a))



data_a = create_random_tuples(5, 1, [int])
data_b = create_random_tuples(3, 1, [int])

# קודם למיין כל רשימה לפי האיבר היחיד בטופל (אינדקס 0)
data_a = sorted(data_a, key=lambda t: t[0])
data_b = sorted(data_b, key=lambda t: t[0])

print("a:", data_a)
print("b:", data_b)

# מיזוג – key זה פונקציה, לא מספר:
data_a_b = merge(data_a, data_b, key=lambda t: t[0])
print("merged:", data_a_b)


