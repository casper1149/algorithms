import sys;

def insertion_sort_asc(arr):
    ''' Ascending insertion sort implementation '''
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key :
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key

def insertion_sort_desc(arr):
    ''' Descending insertion sort implementation '''
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] < key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key

def test_insertion_sort_desc():
    ''' Test of descending insertion sort implementation '''
    arr = [31, 41, 59, 26, 41, 58]
    expected = [59, 58, 41, 41, 31, 26]
    insertion_sort_desc(arr)
    if arr != expected:
        raise Exception('Failed desc, expected: %s, actual: %s' % (str(expected), str(arr)))
    sys.stdout.write('Passed')    

def test_insertion_sort_asc():
    ''' Test of ascending insertion sort implementation '''
    arr = [31, 41, 59, 26, 41, 58]
    expected = [26, 31, 41, 41, 58, 59]
    insertion_sort_asc(arr)
    if arr != expected:
        raise Exception('Failed asc, expected: %s, actual: %s' % (str(expected), str(arr)))
    sys.stdout.write('Passed')

def main():
    try:
        input_array = input('Please specify input array elements to sort using space: ').split(' ')
        input_sort_direction = int(input('Please specify sort direction, [1 - asc], 2 - desc: ') or 1)
        if input_sort_direction != 1 and input_sort_direction != 2:
            raise Exception('invalid input option: %d' % input_sort_direction)
        
        if input_sort_direction == 1:
            insertion_sort_asc(input_array)
        else:
            insertion_sort_desc(input_array)

        sys.stdout.write("sorted array: "+str(input_array))
        #print("sorted array: "+str(input_array))

    except Exception as ex:
        print(ex)

#test_insertion_sort_asc()
#test_insertion_sort_desc()
main()