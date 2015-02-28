import sys;

from utils import assert_equals

def fill(arr):
    ''' Utility method to fill an array '''
    items = [0, 0, 1, 100, 1000, 1, 0, 200]
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
    if(len(arr) == 1): #no sift is required
        return
    if(item_index <= 0): #we have reached the root
        return
    item = arr[item_index]
    parent_index = int((item_index-1)/2)
    parent = arr[parent_index]
    if(parent > item):
        arr[parent_index] = item
        arr[item_index] = parent
    else:
        return
    sift_up(arr, parent_index)

def sift_down(arr, item_index):
    ''' Method to perform sift_down operation '''
    left_index = item_index*2+1
    use_right = False
    if(left_index >= len(arr)): #if there is no left leaf than there is no rigth leaf as well, we have reached the last leaf
        return
    
    next_index = left_index
    right_index = item_index*2+2
    if(right_index < len(arr) and arr[right_index] <= arr[left_index]): #if right leaf exists, and it's value is less then value of the left one, use it
        next_index = right_index

    item = arr[item_index]
    if(item <= arr[next_index]): #balance is reached, return
        return

    #swap nodes and go further
    arr[item_index] = arr[next_index]
    arr[next_index] = item
    sift_down(arr, next_index)

def extract_min(arr):
    ''' Method to extract minimum item '''
    #replace last and first element
    last_item = arr[-1]
    arr[-1] = arr[0]
    arr[0] = last_item

    #pop and save last element, sift_down and finally return last element
    res = arr.pop()
    sift_down(arr, 0)
    return res

def change_priority(arr, item_index):
    ''' Method to change priority of the item, all items are > 0, so this operation changes item value to negative '''
    arr[item_index] = -arr[item_index]

def extract_max(arr):
    ''' Method to extract maximum item '''
    max_item_index = find_max_item_index(arr, 0) #find maximum item index
    change_priority(arr, max_item_index) #change its priority
    sift_up(arr, max_item_index) #sift it up to the top
    el = -extract_min(arr) #extract and make it positive
    return el

def find_max_item_index(arr, item_index):
    ''' Method to find maximum item index '''
    left_index = item_index * 2 + 1
    if(left_index >= len(arr)):
        return item_index
    
    max_left = find_max_item_index(arr, left_index)

    right_index = item_index * 2 + 2
    if(right_index >= len(arr)):
        return item_index if max_left < item_index else max_left

    max_right = find_max_item_index(arr, right_index)
    return max_left if arr[max_left] > arr[max_right] else max_right

def find_max_item(arr, item_index):
    ''' Method to find maximum item '''
    maxx = arr[item_index]

    left_index = item_index * 2 + 1
    if(left_index < len(arr)):
        maxx = max(maxx, find_max_item(arr, left_index))

    right_index = item_index * 2 + 2
    if(right_index < len(arr)):
        maxx = max(maxx, find_max_item(arr, right_index))

    return maxx

def test_tree_search():
    arr = []
    fill(arr, [0, 0, 0, 100, 1000, 1, 1, 200, 6000])
    assert_equals(6000, find_max_item(arr, 0))
    assert_equals(8, find_max_item_index(arr, 0))

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

def test():
    arr = []
    fill(arr)
    print(arr)
    el = extract_max(arr)
    print(el)
    assert_equals(1000, el)
    print(arr)

def main():
    ''' Main method: first input string define number of operations, 
        further goes input of the operations(insert and extract max) like 'Insert X', 'Extract'.
        Sample input:
    6
    Insert 100
    Insert 10
    Extract
    Insert 5
    Insert 50
    Extract
        Sample output:
    100
    50
    '''

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
            res.append(extract_max(arr))

    for i in range(len(res)):
        sys.stdout.write(str(res[i])+"\n")

#test_main()
#test()
#test_tree_search()
main()
