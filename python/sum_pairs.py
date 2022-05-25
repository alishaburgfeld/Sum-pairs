

def sum_pairs(arr, target):
    """
    This function returns all unique pairs of elements in the given array which sum to the target.

    Args:
        arr (list): The array of elements
        target (int): The target sum of pairs of elements 

    Returns:
        list[tuple[a, b]]: List of pairs of elements who sum to the target
    """

    arr_set = set(arr)

    result = list()
    for el in arr_set:
        candidate = target - el

        if candidate >= el and candidate in arr_set:
            result.append([el, candidate])

    return result
