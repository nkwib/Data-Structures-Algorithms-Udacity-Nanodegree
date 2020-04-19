def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0: return ()
    min = max = ints[0]
    for i in ints:
        if i < min: min = i
        if i > max: max = i
    return (min, max)

## Example Test Case of Ten Integers
import random

t1 = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(t1)
t2 = [i for i in range(0, 330)]
random.shuffle(t2)
t3 = [i for i in range(0, 0)]
random.shuffle(t3)
t4 = [i for i in range(330, 330)]
random.shuffle(t4)
t5 = [i for i in range(-10, 10)]
random.shuffle(t5)

print ("Pass" if ((0, 9) == get_min_max(t1)) else "Fail")
print ("Pass" if ((0, 329) == get_min_max(t2)) else "Fail")
print ("Pass" if (() == get_min_max(t3)) else "Fail")
print ("Pass" if (() == get_min_max(t4)) else "Fail")
print ("Pass" if ((-10, 9) == get_min_max(t5)) else "Fail")