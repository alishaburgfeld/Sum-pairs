

def sum_pairs(arr, target):
    """
    This function returns all unique pairs of elements in the given array which sum to the target.

    Args:
        arr (list): The array of elements
        target (int): The target sum of pairs of elements 

    Returns:
        list[list[a, b]]: List of pairs of elements who sum to the target
    """

    range(start, stop, step)
    [1,2,3][1:5:2]
    [1,2,3][1:]

    result = set()

    for i, a in enumerate(arr[:-1]):
        for b in arr[i + 1:]:
            if a + b == target:
                result.add(frozenset(a, b))  # elements of a set must be hashable (immutable)
                                             # lists are mutable so we would use tuples
                                             # but we don't want duplicate pairs so we use
                                             # frozensets which are immutable sets

    return [list(item) for item in result]

    result = list()

    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            a, b = arr[i], arr[j]
            
            if a + b == target and [a, b] not in result and [b, a] not in result:
                result.append([a, b])

    return result


result = sum_pairs([1,2,3,4,5], 9) # [[4,5]]
print(result)
result = sum_pairs([1,2,3,4,5], 7) # [[2,5], [3,4]]
print(result)
result = sum_pairs([3, 1, 5, 8, 2], 27) # 'unable to find pairs'
print(result)
