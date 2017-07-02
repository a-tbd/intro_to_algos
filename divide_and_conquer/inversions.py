'''
Calculate the number of inversions between two lists
Input: list to be examined and sorted
Output: tuple of number of inersions and the sorted list

Examples:
[0, 1, 2, 3] ==> (0, [0, 1, 2, 3])
[2, 1] ==> (1, [1, 2])  
'''

def inversions(n):
    if len(n) == 1:
        return 0, n
    else:
        split = int(round(len(n)/2))
        inv_l, left = inversions(n[:split])
        inv_r, right = inversions(n[split:])
        inv = inv_l + inv_r
        new_n = []
        while left and right:
            if int(right[0]) < int(left[0]):
                inv += len(left)
                a = right.pop(0)
                new_n.append(a)
            else:
                b = left.pop(0)
                new_n.append(b)
        if not left:
            new_n.extend(right)
        else:
            new_n.extend(left)
        return inv, new_n
