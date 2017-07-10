'''
Three implementations of the Quicksort algorithm
1. using the first element as the pivot 
2. using the last element as the pivot
3. using the median of the first, last, 
   and middle elements as the pivot

Sorting 10,000 numbers:
1. 162085
2. 164123
3. 138382
'''
import pdb
import csv 

class QuickSort(object):
    def __init__(self):
        self.comparisons = 0

    def set_comparisons(self):
        self.comparisons = 0
    
    def iterate_comparisons(self, l):
        self.comparisons += len(l) - 1
    
    def first_pivot(self, l):
        self.iterate_comparisons(l)
        if len(l) <= 1:
            return l
        else:
            pivot = l[0]
            center = 1
            for f in range(1, len(l)):
                if l[f] < pivot:
                    l[center], l[f] = l[f], l[center]
                    center += 1
            l[0], l[center - 1] = l[center - 1], l[0]
            left = self.first_pivot(l[:center])
            right = self.first_pivot(l[center:])
            return left + right

    def final_pivot(self, l):
        self.iterate_comparisons(l)
        if len(l) <= 1:
            return l
        else:
            l[0], l[-1] = l[-1], l[0]
            pivot = l[0]
            center = 1
            for f in range(1, len(l)):
                if l[f] < pivot:
                    l[center], l[f] = l[f], l[center]
                    center += 1
            l[0], l[center - 1] =  l[center - 1], l[0]
            left = self.first_pivot(l[:center])
            right = self.first_pivot(l[center:])
            return left + right

    def median_three_pivot(self, l):
        self.iterate_comparisons(l)
        if len(l) <= 1:
            return l
        else:
            middle = int(round(len(l) / 2)) - 1
            # pdb.set_trace()
            median = sorted([(l[0], 0), (l[middle], middle), (l[-1], -1)])
            pivot = median[1][1]
            l[0], l[pivot] = l[pivot], l[0]
            center = 1
            for f in range(1, len(l)):
                if l[f] < l[pivot]:
                    l[center], l[f] = l[f], l[center]
                    center += 1
            l[0], l[center - 1] = l[center - 1], l[0]
            left = self.median_three_pivot(l[:center])
            right = self.median_three_pivot(l[center:])
            return left + right



with open('qs_num.csv','rb') as f:
    reader = csv.reader(f)
    num = list(reader)
flat = [int(i[0]) for i in num]

qs = QuickSort()
fp_sorted = qs.first_pivot(flat)
print "first pivot", qs.comparisons
qs.set_comparisons()

lp_sorted = qs.final_pivot(flat)
print "last pivot", qs.comparisons
qs.set_comparisons()

mtp_sorted = qs.median_three_pivot(flat)
print "median three", qs.comparisons

#sorted_flat = first_pivot(flat)
#output = [str(i) for i in sorted_flat]
#with open('qs_sorted.txt', 'w') as o:
#    o.write('\n'.join(output))


