import sys;

def count_sort(n, A):
    B = [0] * 11
    for j in range(0, n):
        B[A[j]] = B[A[j]] + 1

    k = 0;
    for i in range(0, 11):
        for j in range(0, B[i]):
            A[k] = i
            k += 1

    return A

''' Input option 1

input_list = []

while True:
    input_str = input('>')
    input_list.append(input_str)
    if len(input_list) > 1:
        break

sort_size = int(input_list[0])
sort_numbers = list(map(int, input_list[1].split()))

result = count_sort(sort_size, sort_numbers)

for i in range(0, len(result)):
    sys.stdout.write(str(result[i]) + " ")
'''

''' Input option 2 with input validation '''
try:
    input_sort_size = input('Please specify number of elements to sort: ')
    sort_size = int(input_sort_size)
    input_sort_numbers = input('Please specify %d elements in between 0 and 10 to sort: ' % sort_size)
    sort_numbers = list(map(int, input_sort_numbers.split()))

    if(len(sort_numbers) > sort_size):
        raise Exception("Wrong number of elements")

    for i in range(0, len(sort_numbers)):
        if(sort_numbers[i] > 10):
            raise Exception("Element %d is too big" % (i+1))

    result = count_sort(sort_size, sort_numbers)

    for i in range(0, len(result)):
        sys.stdout.write(str(result[i]) + " ")
except ValueError:
    print("That's not an int!")
except Exception as ex:
    print(ex)
