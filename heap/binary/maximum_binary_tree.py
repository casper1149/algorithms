import sys;

from utils import assert_equals

def fill(arr):
    ''' Utility method to fill an array '''
    items = [10, 2, 3, 100, 1, 200]
    for item in items:
        insert(arr, item)

def fill(arr, items):
    ''' Utility method to fill an array '''
    for item in items:
        insert(arr, item)

def insert(arr, el):
    ''' Method to insert an element into the binary tree and perform sift_up operation on the element '''
    arr.append(el)
    sift_up(arr, len(arr)-1)

def sift_up(arr, item_index):
    ''' Method to perform sift_up operation '''
    if(len(arr) <=1):
        return
    if(item_index <= 0): #we have reached the root
        return
    item = arr[item_index]
    parent_index = int((item_index-1)/2)
    parent = arr[parent_index]
    if(parent < item):
        arr[parent_index] = item
        arr[item_index] = parent
    else:
        return #balance was reached
    sift_up(arr, parent_index)

def sift_down(arr, item_index):
    ''' Method to perform sift_down operation '''
    left_index = item_index*2 + 1
    if(left_index >= len(arr)):
        return
    next_index = left_index
    right_index = item_index*2 + 2
    if(right_index < len(arr) and arr[right_index] > arr[left_index]):
        next_index = right_index

    item = arr[item_index]
    if(item >= arr[next_index]):
        return
    arr[item_index] = arr[next_index]
    arr[next_index] = item
    sift_down(arr, next_index)

def extract_max(arr):
    ''' Method to extract max element and perform sift_down operation '''
    el = arr[0]
    arr[0] = arr[len(arr)-1]
    arr[len(arr)-1] = el
    arr.pop()
    sift_down(arr, 0)
    return el

def test_sift_up():
    arr = []
    fill(arr)
    print(arr)
    assert_equals(200, arr[0])

def test_sift_down():
    arr = []
    fill(arr)
    print(arr)
    item = arr[0]
    arr[0] = arr[len(arr)-1]
    arr[len(arr)-1] = item
    print(arr)
    sift_down(arr, 0)
    print(arr)
    assert_equals(3, arr[len(arr)-1])

def test_extract_max():
    arr = []
    fill(arr)
    print(arr)
    el = extract_max(arr)
    assert_equals(200, el)
    print(el)
    print(arr)

def test_main():
    arr = []
    insert(arr, 0)
    insert(arr, 0)
    insert(arr, 1)
    insert(arr, 100)
    insert(arr, 1000)
    insert(arr, 1)
    insert(arr, 0)
    insert(arr, 0)
    print(arr)
    assert_equals(1000, extract_max(arr))
    print(arr)
    insert(arr, 100)
    print(arr)
    insert(arr, 10)
    print(arr)
    assert_equals(100, extract_max(arr))
    print(arr)
    insert(arr, 5)
    print(arr)
    insert(arr, 50)
    print(arr)
    assert_equals(100, extract_max(arr))
    assert_equals(50, extract_max(arr))
    assert_equals(10, extract_max(arr))
    assert_equals(5, extract_max(arr))
    assert_equals(1, extract_max(arr))
    assert_equals(1, extract_max(arr))
    assert_equals(0, extract_max(arr))
    assert_equals(0, extract_max(arr))
    assert_equals(0, extract_max(arr))
    assert_equals(0, extract_max(arr))
    print(arr)

def main():
    ''' Main method: 1 input string define number of operations, 
        further goes input of the operations(insert and extract max) like 'Insert X', 'Extract'.
        Output is: extracted elements '''
    arr = []
    res = []
    input_length = int(input(''))
    for i in range(input_length):
        input_str = str(input(''))
        command = input_str.split(' ')
        if(command[0] == "Insert"):
            item = int(command[1])
            insert(arr, item)
        if(command[0] == "Extract"):
            if(len(arr) <= 0):
                continue
            el = extract_max(arr)
            res.append(el)

    for i in range(len(res)):
        sys.stdout.write(str(res[i])+"\n")

#test_sift_up()
#test_sift_down()
#test_extract_max()
#test_main()
main()
