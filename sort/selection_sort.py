import sys;

def swap(arr, index_one, index_two):
    ''' Method to swap array elements'''
    el = arr[index_one]
    arr[index_one] = arr[index_two]
    arr[index_two] = el

def selection_sort_asc(arr):
    ''' Ascending selection sort implementation '''
    for i in range(0, len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j

        if min != i:
            swap(arr, i, min)

def selection_sort_desc(arr):
    ''' Descending selection sort implementation '''
    for i in range(0, len(arr)-1):
        max = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[max]:
                max = j

        if max != i:
            swap(arr, i, max)

def test_selection_sort_asc():
    ''' Test to verify ascending selection sort implementation '''
    arr = [31, 41, 59, 26, 21, 58, 31]
    expected = [21, 26, 31, 31, 41, 58, 59]
    selection_sort_asc(arr)
    if arr != expected:
        raise Exception('Failed asc, expected: %s, actual: %s' % (str(expected), str(arr)))
    sys.stdout.write('Asc test passed\n')

def test_selection_sort_desc():
    ''' Test to verify ascending selection sort implementation '''
    arr = [31, 41, 59, 26, 21, 58, 31]
    expected = [59, 58, 41, 31, 31, 26, 21]
    selection_sort_desc(arr)
    if arr != expected:
        raise Exception('Failed desc, expected: %s, actual: %s' % (str(expected), str(arr)))
    sys.stdout.write('Desc test passed\n')

def main():
    try:
        input_array = input('Please specify input array elements to sort using space: ').split(' ')
        input_sort_direction = int(input('Please specify sort direction, [1 - asc], 2 - desc: ') or 1)
        if input_sort_direction != 1 and input_sort_direction != 2:
            raise Exception('invalid sort direction option: %d' % input_sort_direction)
        
        if input_sort_direction == 1:
            selection_sort_asc(input_array)
        else:
            selection_sort_desc(input_array)

        sys.stdout.write("sorted array: "+str(input_array))

    except Exception as ex:
        sys.stdout.write(str(ex))

test_selection_sort_asc()
test_selection_sort_desc()
main()