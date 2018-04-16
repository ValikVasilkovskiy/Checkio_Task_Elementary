"""
Input data: A nested list with integers.
Output data: The one-dimensional list with integers.
Example:
flat_list([1, 2, 3]) == [1, 2, 3]
flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]
flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
"""
def flat_list(array):
    r, s, t = [], str(array), ''
    for i in range(len(s)):
        if s[i].isdigit() or s[i] == '-':
            t += s[i]
        else:
            if t:
                r.append(int(t))
                t = ''
    return r

def deep(data):
    stack = []
    list(map(lambda x: stack.append(x) if '__iter__' not in dir(x) else stack.extend(deep(x)), data))
    return stack

def search_deep(data):
    stack = []
    for i in data:
        if '__iter__' not in dir(i):
            stack.append(i)
        else:
            stack.extend(search_deep(i))
    return stack


assert flat_list([[[2]], [4, [5, 6, [-69], 6, 6, 6], 7]]) == [2, 4, 5, 6, -69, 6, 6, 6, 7]

assert deep([1, [1, 2], [[[1]]], -2]) == [1, 1, 2, 1, -2]
assert deep([[1], [[-1], 2], [[[1]]], -2]) == [1, -1, 2, 1, -2]
assert deep([1, 2, 3, 4]) == [1, 2, 3, 4]
assert deep([1,]) == [1]


assert search_deep([1, [1, 2], [[[1]]], -2]) == [1, 1, 2, 1, -2]
assert search_deep([[1], [[-1], 2], [[[1]]], -2]) == [1, -1, 2, 1, -2]
assert search_deep([1, 2, 3, 4]) == [1, 2, 3, 4]
assert search_deep([1,]) == [1]