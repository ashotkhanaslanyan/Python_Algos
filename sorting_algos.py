##
## Get biggest number in array
##

##
## Complexity O(n)
## Memory O(1)
##


def get_max(arr):

    max_temp = arr[0]

    for i in range(len(arr)):

        if(arr[i] > max_temp):

            max_temp = arr[i]

    return max_temp


##
## Get smallest number in array
##

##
## Complexity O(n) Memory O(1)
##


def get_min(arr):

    min_temp = arr[0]

    for i in range(len(arr)):

        if(arr[i] < min_temp):

            min_temp = arr[i]

    return min_temp


##
## Insertion Sort
##

##
## Complexity O(n^2)
## Memory O(1)
##


def insertion_sort(arr):

##
## For key in array, starting from index 1
## find the leftmost number bigger that the key
## shift array to the right starting from that number
## insert the key in that number's place
##

    for i in range(1, len(arr)):

        temp = arr[i]
        j = i - 1
        
        while(temp < arr[j] and j >= 0):

            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp

    return arr


##
## Counting sort 
##

##
## Complexity O(n+k), where k = len(count)
## Memory O(k), where k = len(count)
##


def counting_sort(arr):

##
## For number in range [min(arr), max(arr)]
## count how many times that number
## occures in the array.
## Save the number of occurences in count
## array with indexes from 0 to (max(arr) - min(arr)).
## Iterate throug count array and add
## numbers by their count to the sorted array.
##

    arr_min = get_min(arr)
    arr_max = get_max(arr)

    count = [0] * (arr_max - arr_min + 1)

    for num in arr:

        count[num-arr_min] += 1

    arr_i = 0
    
    for i in range(len(count)):
        
        while(count[i] > 0):

            arr[arr_i] = i + arr_min
            arr_i += 1
            count[i] -= 1

    return arr


##
## Complexity O(n+k), where k = len(count)
## Memory O(n+k), where k = len(count)
##


def radix_counting_sort(arr, exp):

    count = [0] * 10

    for num in arr:

        count[int((num/exp)%10)] += 1

    for i in range(1, len(count)):

        count[i] += count[i-1]

    sorted_arr = [0] * count[-1]
    i = len(arr) - 1

    while(i >= 0):

        index = int((arr[i]/exp)%10)
        sorted_arr[count[index]-1] = arr[i] 
        count[index] -= 1
        i-=1

    arr = sorted_arr

    return arr


##
## Radix Sort
##

##
## Complexity O(d*(n+b)), where d = digits in integers, b = base
## Memory O(d+n), where d = digits in largest integer
##


def radix_sort(arr):

##
## Get biggest number in array,
## for each exponent space in the biggest
## number use counting sort to sort at
## one's place, at ten's place, etc.
##

    arr_max = get_max(arr)
    exp = 1
    
    while(arr_max / exp > 1):

        arr = radix_counting_sort(arr, exp)
        exp *= 10
        
    return arr


##
## Heap Sort
##

##
## Complexity O(nlogn)
## Memory O(1)
##


def heapify(arr, n, i):
    
    root = i
    left = 2 * i + 1
    right = 2 * i + 2

    if(left < n and arr[i] < arr[left]):

        root = left

    if(right < n and arr[root] < arr[right]):

        root = right

    if(root != i):

        temp = arr[i]
        arr[i] = arr[root]
        arr[root] = temp

        heapify(arr, n, root)


def heap_sort(arr):

##
## Create a maximum heap.
## Get the root of the heap
## and append it to the arr.
##

    n = len(arr)

    for i in range(n//2-1, -1, -1):

        heapify(arr, n, i)

    for i in range(n-1, 0, -1):

        temp = arr[i]
        arr[i] = arr[0]
        arr[0] = temp

        heapify(arr, i, 0)

    return arr


##
## Bubble Sort
##

##
## Complexity O(n^2)
## Memory O(1)
##


def bubble_sort(arr):

##
## For each item in the array check
## wether it is bigger than it the item
## after it, and if yes switch places.
## Continue doing the process untill
## no swaps take place.
##

    swap_count = 0
    
    for i in range(1, len(arr)):
        
        if(arr[i] < arr[i-1]):

            temp = arr[i]
            arr[i] = arr[i-1]
            arr[i-1] = temp
            swap_count += 1

    if(swap_count == 0):
    
        return arr

    else:

        return bubble_sort(arr)


##
## Selection Sort
##

##
## Complexity O(n^2)
## Memory O(1)
##


def selection_sort(arr):

##
## Iterate throug the array.
## Find the smallest element in
## the array and place it at the
## beginning of the array.    
##

    n = len(arr)
    i = 0

    while(i < n-1):

        min_index = i
        j = i + 1

        while(j < n):

            if(arr[j] < arr[min_index]):

                min_index = j

            j += 1

        temp = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = temp
        i += 1
    
    return arr


##
## Merge Sort
##

##
## Complexity O(nlogn)
## Memory O(n)
##


def merge_sort(arr):

##
## Divide the array into smaller arrays
## until you have array of length 1,
## then merge the arrays by sorting them.
##

    if(len(arr) > 1):

        midpoint = len(arr)//2
        left_arr = arr[:midpoint]
        right_arr = arr[midpoint:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i, j, k = [0] * 3

        while(i < len(left_arr) and j < len(right_arr)):

            if(left_arr[i] < right_arr[j]):

                arr[k] = left_arr[i]
                i += 1

            else:

                arr[k] = right_arr[j]
                j += 1
                
            k += 1

        while(i < len(left_arr)):

            arr[k] = left_arr[i]
            i += 1
            k += 1

        while(j < len(right_arr)):

            arr[k] = right_arr[j]
            j += 1
            k += 1

    return arr


##
## Quick Sort
##

##
## Complexity O(n^2)
## Memory O(logn)
##


def quick_sort_partition(arr, smallest, largest):

    i = smallest

    for j in range(smallest+1, largest):

        if(arr[j] < arr[smallest]):

            temp = arr[i+1]
            arr[i+1] = arr[j]
            arr[j] = temp
            i += 1

    if(i == smallest and arr[smallest] > arr[smallest+1]):

        i = largest - 1

    temp = arr[smallest]
    arr[smallest] = arr[i]
    arr[i] = temp
    
    return i


def quick_sort(arr, smallest=0, largest=None):
    
##
## Choose a pivot, transfer all items
## smaller than pivot to the left
## and all the items bigger to the right.
## Repeat the process on the arrays on
## left and right, until the array is sorted
##

    if(largest == None):

        largest = len(arr)

    if(smallest < largest-1):

        pivot = quick_sort_partition(arr, smallest, largest)
        quick_sort(arr, smallest=smallest, largest=pivot)
        quick_sort(arr, smallest=pivot+1, largest=largest)
    
    return arr    


##
## Tests
##


def main():

    arr = [5, 4, 1, 9, 7, 6, 3, 2, 10, 8, 12, 11]
    print('Input array: ', arr)
    print('--Outputs--')
    print('Get max: ', get_max(arr))
    print('Get min: ', get_min(arr))
    print('Insertion sort: ', insertion_sort(arr.copy()))
    print('Counting sort: ', counting_sort(arr.copy()))
    print('Radix sort: ', radix_sort(arr.copy()))
    print('Heap sort: ', heap_sort(arr.copy()))
    print('Bubble sort: ', bubble_sort(arr.copy()))
    print('Selection sort', selection_sort(arr.copy()))
    print('Merge sort: ', merge_sort(arr.copy()))
    print('Quick sort: ', quick_sort(arr.copy()))
    

if(__name__ == '__main__'):

    main()
