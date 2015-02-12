import sys;

def binary_search(size_sorted, arr_sorted, item_to_find):
    ''' binary search implementation '''
    left_border = 0
    right_border = size_sorted
    while left_border <= right_border:
        m = int((left_border + right_border) / 2)
        if(arr_sorted[m] == item_to_find):
            return m+1 #return index starting from 1
        else:
            if(arr_sorted[m] > item_to_find):
                right_border = m - 1 #move right border
            else:
                if(arr_sorted[m] < item_to_find):
                    left_border = m + 1 #move left border
    return -1

''' Input option 1, raw
input_list = []

while True:
    input_str = input('')
    input_list.append(input_str)
    if len(input_list) > 1:
        break

arr_n = list(map(int, input_list[0].split()))
n = arr_n.pop(0) #get number of elements and remove this value from the input array
A = arr_n #get array to search in
arr_k = list(map(int, input_list[1].split()))
k = arr_k.pop(0) #get number of elements and remove this value from the input array
B = arr_k #get array of elements to search for

result_list = []

for i in range(0, k):
    result_list.append(binary_search(n-1, A, B[i]))

for i in range(0, k):
    sys.stdout.write(str(result_list[i]) + " ")
'''

''' Input option 2 with input validation '''
try:
    input_sorted_arr = input('Please specify number of elements and sorted array: ')
    arr_n = list(map(int, input_sorted_arr.split()))
    n = arr_n.pop(0) #get number of elements and remove this value from the input array
    A = arr_n #get array to search in
    
    input_search_arr = input('Please specify number of elements and elements to find: ')
    arr_k = list(map(int, input_search_arr.split()))
    k = arr_k.pop(0) #get number of elements and remove this value from the input array
    B = arr_k #get array of elements to search for

    if(len(A) > n or len(A) < n or len(B) > k or len(B) < k): #input validation
        raise Exception("Wrong number of elements")

    result_list = []

    for i in range(0, k):
        result_list.append(binary_search(n-1, A, B[i]))

    for i in range(0, k):
        sys.stdout.write(str(result_list[i]) + " ")
except ValueError:
    print("That's not an int!")
except Exception as ex:
    print(ex)