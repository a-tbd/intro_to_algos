'''
Coursera: Intro to Algorithms Week 3
Maintaining the median with a double heap data structure

'''
import heapq
import pdb


def median(num_list):
    max_heap = []
    min_heap = []

    sum_median = 0
    median = -float('inf')

    for i in range(len(num_list)):
        left_size = len(max_heap)
        right_size = len(min_heap) 

        if num_list[i] > median: 
            if left_size == right_size:
            	if right_size == 0 or not num_list[i] > min_heap[0]:
                    heapq.heappush(max_heap, -num_list[i])
                else:
                    node = heapq.heappop(min_heap)
                    heapq.heappush(max_heap, -node)
                    heapq.heappush(min_heap, num_list[i])
            elif left_size > right_size: 
                heapq.heappush(min_heap, num_list[i]) 
        else:
            if left_size == right_size:
                heapq.heappush(max_heap, -num_list[i])
            elif left_size > right_size: 
                node = heapq.heappop(max_heap) 
                heapq.heappush(min_heap, -node) 
                heapq.heappush(max_heap, -num_list[i])
        median = -max_heap[0] 
        sum_median += median
    print sum_median % 10000

########################
###### TEST CASES ######
########################

test1 = [1,666,10,667,100,2,3] # 142
test2 = [6331,2793,1640,9290,225,625,6195,2303,5685,1354] # 9335
test3 = [78,71,99,9,24,11,94,96,90,14,27,60,55,46,29,74,10,67,8,97,30,18,2,43,56,98,4,33,76,86,19] # 1769

median(test1)
median(test2)
median(test3)






