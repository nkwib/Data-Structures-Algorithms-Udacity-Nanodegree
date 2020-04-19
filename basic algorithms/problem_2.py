def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    first, last = 0, len(input_list) - 1
    try:
        while first<=last:
            mid = (first + last)//2
            if input_list[mid] == number : return mid
            elif input_list[mid]<number:
                if input_list[first]<= number and input_list[first] > input_list[mid]:
                    last = mid - 1
                else: first = mid + 1
            
            elif input_list[mid]>number:
                if input_list[last] >= number and input_list[last] < input_list[mid]:
                    first = mid + 1
                else: last = mid - 1
        return -1
    except:
        return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], 10])
test_function([['nope', 'maybe', 'yes'], 'nope'])
test_function([['nope', 'maybe', 'yes'], 124])