# Sorting Algorithms

This project implements three sorting algorithms: Mergesort, Quicksort, and Quicksort with Median of Medians (MM). The program compares the execution time of these algorithms for sorting random arrays.

## Requirements

To run the program, ensure you have the following:

- Python (version 3 or above)

## Usage

1. Open the Python script `project2.py` in your preferred Python IDE or text editor.
2. Modify the `size` variable to set the desired size of the array.
3. Modify the `k` variable to set the desired value for finding the k-th smallest element.
4. Run the script.
5. The program will generate a random array of the specified size with values between 1 and 100.
6. For each sorting algorithm, it will print the unsorted array and the sorted array.
7. It will also find and print the k-th smallest element in the sorted array.
8. After running the algorithms 10 times, it will display the average execution time for each algorithm.

## Algorithms

1. **Mergesort**: This algorithm recursively divides the array into two halves, sorts them separately, and then merges the sorted halves.

2. **Quicksort**: This algorithm chooses a pivot element, partitions the array around the pivot, and recursively sorts the subarrays before and after the pivot.

3. **Quicksort with Median of Medians (MM)**: This algorithm uses the Median of Medians technique to select a good pivot element, improving the worst-case performance of Quicksort.

## Results

The program calculates the average execution time for each algorithm based on 10 runs. The three sorting algorithms are compared based on their average execution times. The lower the average time, the more efficient the algorithm is considered.

