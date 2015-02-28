import sys;

def get_fib(n):
    ''' Fibonacci algo simple implementation'''
    if(n <= 1):
        return n;
    else:
        range_end = n+1
        F = list(range(range_end))
        for i in range(2,range_end):
            F[i] = F[i-1] + F[i-2]
        return F[n]

def get_fib_v2(n):
    ''' Fibonacci algo with improved memory usage implementation'''
    if(n <= 1):
        return n
    
    range_end = n+1
    F = [0, 1, 0]
    for i in range(2, range_end):
        F[2] = F[0] + F[1]
        F[0] = F[1]
        F[1] = F[2]

    return F[2]

def get_fib_last_digit(n):
    ''' Method to get last digit of 'n' fibonacci number '''
    if(n <= 1):
        return n;
    else:
        range_end = n+1
        F = list(range(range_end))
        for i in range(2,range_end):
            F[i] = (F[i-1] + F[i-2])%10
        return F[n]

def get_fib_modulo(n, m):
    ''' Method to get modulo 'n' fibonacci number on m '''
    fib_prev = 0
    fib = 1
    arr = [fib_prev, fib]

    for curr in range(1, n):
        fib_old = fib
        fib = (fib + fib_prev) % m
        fib_prev = fib_old

        if fib_prev == 0 and fib == 1:
            arr.pop()
            break
        else:
            arr.append(fib)

    offset = n % len(arr)
    return arr[offset]

user_input_value = input('Please specify fibonacci number: ')
user_operation_select = input('Please specify operation to perform: [1 - get value], 2 - get last digit, 3 - get divide: ') or 1
try:
    val = int(user_input_value)
    operation = int(user_operation_select)
    if(operation not in range(1,4)):
        raise Exception("Unavailable option")

    if(operation == 1):
        result = get_fib_v2(val)
    if(operation == 2):
        result = get_fib_last_digit(val)
    if(operation == 3):
        user_input_module_value = input('Please specify number to divide on: ')
        result = get_fib_modulo(val, int(user_input_module_value))

    sys.stdout.write(str(result))
except ValueError:
    print("That's not an int!")
except Exception as ex:
    print(ex)
