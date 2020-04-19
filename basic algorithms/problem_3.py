def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    lft, rgt = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(lft, rgt, arr.copy())

def merge(left, right, merged):
    lc, rc = 0, 0
    while lc < len(left) and rc < len(right):
        if left[lc] <= right[rc]:
            merged[lc + rc] = left[lc]
            lc += 1
        else:
            merged[lc + rc] = right[rc]
            rc += 1
    for lc in range(lc, len(left)):
        merged[lc + rc] = left[lc]
    for rc in range(rc, len(right)):
        merged[lc + rc] = right[rc]
    return merged

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    input_list = merge_sort(input_list)
    input_list.reverse()
    n1 = ''.join(map(str, input_list[0::2]))
    n2 = ''.join(map(str, input_list[1::2]))
    return [int(n1), int(n2)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# TEST 1:
test_function([[1, 2, 3, 4, 5], [542, 31]])
# TEST 2:
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
# TEST 3: Trying with multiple 0
test_function([[0,0,1], [10, 0]])
# TEST 4: trying with only 0
test_function([[0,0,0,0,0,0], [000, 000]])
# TEST 5:
test_function([[0,0,0,0,0,0,1], [1000, 000]])
# TEST 6:
test_function([[0,0,0,0,0,0,9,1], [9000, 1000]])
# TEST 9: Large numbers
test_function([[0,0,0,0,0,0,9,1,9,9,9,9,9,9,9,9,9,9,9], [999999000, 9999991000]])