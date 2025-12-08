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

def insertion_sort(a, key):
    """
    ממיינת את הרשימה a במקום (in-place)
    לפי ערך המפתח ש־key(x) מחזירה.
    """
    n = len(a)
    for i in range(1, n):
        current_item = a[i]
        current_key = key(current_item)

        j = i - 1
        # מזיזים איברים שגדולים מהמפתח של current_item קדימה
        while j >= 0 and key(a[j]) > current_key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = current_item


def main():
    # רשימה 1 – מיון לפי האיבר הראשון (int)
    data1 = create_random_tuples(3, 3, [int, float, str])
    print("רשימה 1 לפני המיון:", data1)
    insertion_sort(data1, key=lambda x: x[0])
    print("רשימה 1 אחרי מיון לפי האיבר הראשון:", data1)
    print()

    # רשימה 2 – מיון לפי האיבר השני (float)
    data2 = create_random_tuples(3, 3, [int, float, str])
    print("רשימה 2 לפני המיון:", data2)
    insertion_sort(data2, key=lambda x: x[1])
    print("רשימה 2 אחרי מיון לפי האיבר השני:", data2)
    print()

    # רשימה 3 – מיון לפי האיבר השלישי (str)
    data3 = create_random_tuples(3, 3, [int, float, str])
    print("רשימה 3 לפני המיון:", data3)
    insertion_sort(data3, key=lambda x: x[2])
    print("רשימה 3 אחרי מיון לפי האיבר השלישי:", data3)


if __name__ == "__main__":
    main()