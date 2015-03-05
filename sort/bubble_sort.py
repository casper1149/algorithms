import sys;

def test_bubble_sort():
    ''' Test to verify bubble sort implementation '''
    arr = [3, 41, 3, 52, 26, 26, 5, 12]
    expected = [3, 3, 5, 12, 26, 26, 41, 52]
    bubble_sort(arr)
    if arr != expected:
        raise Exception('test_bubble_sort, expected: %s, actual: %s' % (str(expected), str(arr)))
    sys.stdout.write('test_bubble_sort passed\n')

def bubble_sort(arr):
    ''' Bubble sort implementation '''
    for i in range(0, len(arr)-1):
        for j in range(len(arr)-1, i, -1):
            if arr[j] < arr[j-1]:
                el = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = el

def main():
    ''' Main application method '''
    try:
        input_array = list(map(int, input('Please specify input array elements to sort using space: ').split(' ')))
        bubble_sort(input_array)
        sys.stdout.write("sorted array: "+str(input_array)+"\n")

    except Exception as ex:
        sys.stdout.write(str(ex))

test_bubble_sort()
main()

