import sys;

def test_merge_sort():
    ''' Test to verify merge sort implementation, consists of two validations,
        one using array with an even number of elements and one with uneven '''
    arr = [3, 41, 3, 52, 26, 26, 5, 12]
    expected = [3, 3, 5, 12, 26, 26, 41, 52]
    merge_sort(arr, 1, len(arr))
    if arr != expected:
        raise Exception('test_merge_sort, expected: %s, actual: %s' % (str(expected), str(arr)))


    arr = [3, 41, 3, 52, 26, 26, 1]
    expected = [1, 3, 3, 26, 26, 41, 52]
    merge_sort(arr, 1, len(arr))
    if arr != expected:
        raise Exception('test_merge_sort, expected: %s, actual: %s' % (str(expected), str(arr)))

    sys.stdout.write('test_merge_sort passed\n')

def merge_sort(arr, left, right):
    ''' Merge sort implementation main method '''
    if left < right:
        mediana = int((left+right)/2)
        merge_sort(arr, left, mediana)
        merge_sort(arr, mediana+1, right)
        merge(arr, left, right, mediana)

def merge(arr, left, right, mediana):
    ''' Merge sort implementation merge method '''
    left = left-1
    left_arr = arr[left:mediana]
    right_arr = arr[mediana:right]	
    k = left
    while k < right:
        if len(left_arr) == 0:
           arr[k] = right_arr.pop(0)
           k += 1
           continue
        if len(right_arr) == 0:
           arr[k] = left_arr.pop(0)
           k += 1
           continue
        
        if left_arr[0] <= right_arr[0]:
            arr[k] = left_arr.pop(0)
        else:
            arr[k] = right_arr.pop(0)
        k += 1

def main():
    ''' Main application method '''
    try:
        input_array = list(map(int, input('Please specify input array elements to sort using space: ').split(' ')))
        merge_sort(input_array, 1, len(input_array))
        sys.stdout.write("sorted array: "+str(input_array)+"\n")

    except Exception as ex:
        sys.stdout.write(str(ex))

test_merge_sort()
main()

