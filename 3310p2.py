# Roy Afaryan
# Dr. Young
# CS3310 - Project 2
# 5/18/2023

import statistics
import random
import time

# Algorithm 1: Mergesort
def mergesort(arr):
    
    # base case
     if len(arr) <= 1:
          return arr

     else:
          # find the midpoint
          mid = len(arr) // 2

          # everything to the left of the midpoint (recursive call)
          leftPartition = mergesort(arr[:mid])

          # everything to the right of the midpoint (recursive call)
          rightPartition = mergesort(arr[mid:])

          # merge function call
          return merge(leftPartition, rightPartition)
    

def merge(leftPartition, rightPartition):
    
     # create instance of newly sorted array
     mergedArr = []

     # while both partitions are non-empty
     while leftPartition and rightPartition:

          if leftPartition[0] > rightPartition[0]:
               # add right partition element 0 to the end of the list
               mergedArr.append(rightPartition[0])
               # remove rightPartition[0] from rightPartition list
               rightPartition.pop(0)
          else:
               # add left partition element 0 to the end of the list
               mergedArr.append(leftPartition[0])
               # remove leftPartition[0] from leftPartition list
               leftPartition.pop(0)

     # ensure proper sorted list with arrays of uneven length
     mergedArr.extend(leftPartition)
     mergedArr.extend(rightPartition)

     return mergedArr


# Algorithm 2: Quicksort
def quicksort(arr, left, right):
      
      if left < right:
           pivot_index = partition(arr, left, right)
           quicksort(arr, left, pivot_index - 1)
           quicksort(arr, pivot_index + 1, right)

def partition(arr, left, right):

     pivot = arr[left]
     i = left + 1

     for j in range(left + 1, right + 1):
          if arr[j] <= pivot:
               # swap i and j values
               arr[i], arr[j] = arr[j], arr[i]
               i += 1
     # swap i + 1 and pivot values
     arr[left], arr[i - 1] = arr[i - 1], arr[left]
     # return pivot position
     return i - 1



# Algorithm 3: Quicksort via MM
def quicksortMM(arr, left, right):
      
      if left < right:
           pivot_index = partitionMM(arr, left, right)
           quicksortMM(arr, left, pivot_index - 1)
           quicksortMM(arr, pivot_index + 1, right)

def partitionMM(arr, left, right):

     pivot = findMedian(arr, left, right)
     
     # properly swap the index of MM with the first element
     i = left
     for j in range(left, right):
          if arr[j] == pivot:
               arr[j], arr[i] = arr[i], arr[j]
               break
     
     # first element (MM) is the pivot
     pivot = arr[left]
     i = left + 1

     # same algorithm as quicksort
     for j in range(left + 1, right + 1):
          if arr[j] <= pivot:
               # swap i and j values
               arr[i], arr[j] = arr[j], arr[i]
               i += 1
     # swap i + 1 and pivot values
     arr[left], arr[i - 1] = arr[i - 1], arr[left]
     # return pivot position
     return i - 1

def findMedian(arr, left, right):
     
     subarrays = [arr[i:i+5] for i in range(left, right + 1, 5)]
     medians = [statistics.median_low(subarray) for subarray in subarrays]
     return int(statistics.median_low(medians))
          
# FIND Kth ELEMENT
# k = 1, min
# k = n, max
def find_kth_element(arr, k):

     kth_smallest = arr[k - 1]

     if k == 1:
          print(f'{kth_smallest} is the smallest value in the sorted list.')

     elif k % 10 == 1:
          print(f'{kth_smallest} is the {k}st smallest value in the sorted list.')
     elif k % 10 == 2:
          print(f'{kth_smallest} is the {k}nd smallest value in the sorted list.')
     elif k % 10 == 3:
          print(f'{kth_smallest} is the {k}rd smallest value in the sorted list.')
     elif k % 10 in [4, 5, 6, 7, 8, 9, 0]:
          print(f'{kth_smallest} is the {k}th smallest value in the sorted list.')


def main():

     # Generate a random size between 1 and 10
     size = 10
     k = 1
     mergesort_times = []
     quicksort_times = []
     quicksortMM_times = []

     for count in range(10):
          # Generate a random array of size 'size' with values between 1 and 100
          arr1 = [random.randint(1, 100) for _ in range(size)]
          arr2 = arr1.copy()
          arr3 = arr1.copy()
          
          print("Unsorted Array:")
          print(arr1)
          print()

          # arr1 = mergesort
          print("Sorted array using mergesort:")
          # start time
          start_time = time.time()
          # call mergesort
          arr1 = mergesort(arr1)
          # print sorted list
          print(arr1)
          # print kth element
          find_kth_element(arr1, k)
          # end time
          end_time = time.time()
          # time taken for mergesort to complete
          time_taken = round((end_time - start_time) * 1000, 2)
          # print time
          print("Execution time (mergesort):", time_taken, "milliseconds\n")
          # append mergesort time to list of times
          mergesort_times.append(time_taken)


          # arr2 = quicksort
          print("Sorted array using quicksort:")
          # start time
          start_time = time.time()
          # call mergesort
          quicksort(arr2, 0, len(arr2) - 1)
          # print sorted list
          print(arr2)
          # print kth element
          find_kth_element(arr2, k)
          # end time
          end_time = time.time()
          # time taken for quicksort to complete
          time_taken = round((end_time - start_time) * 1000, 2)
          # print time
          print("Execution time (quicksort):", time_taken, "milliseconds\n")
          # append quicksort time to list of times
          quicksort_times.append(time_taken)


          # arr3 = quicksortMM
          print("Sorted array using quicksort with MM:")
          # start time
          start_time = time.time()
          # call quicksortMM
          quicksortMM(arr3, 0, len(arr3) - 1)
          # print sorted list
          print(arr3)
          # print kth element
          find_kth_element(arr3, k)
          # end time
          end_time = time.time()
          # time taken for quicksortMM to complete
          time_taken = round((end_time - start_time) * 1000, 2)
          # print time
          print("Execution time (quicksort with MM):", time_taken, "milliseconds\n")
          # append mergesort time to list of times
          quicksortMM_times.append(time_taken)
               
     # print average times for each algorithm:
     print(f"For size n = {size}, the average time for mergesort is", round(statistics.mean(mergesort_times), 2), "milliseconds.")
     print(f"For size n = {size}, the average time for quicksort is", round(statistics.mean(quicksort_times), 2), "milliseconds.")
     print(f"For size n = {size}, the average time for quicksort with MM is", round(statistics.mean(quicksortMM_times), 2), "milliseconds.")


if __name__ == "__main__":
     main()



              

    

    
    
