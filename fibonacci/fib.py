def get_fib(n):
    if(n <= 1):
        return n;
    else:
        range_end = n+1
        F = list(range(range_end))
        for i in range(2,range_end):
            F[i] = F[i-1] + F[i-2]
        return F[n]

def get_fib_last_digit(n):
    if(n <= 1):
        return n;
    else:
        range_end = n+1
        F = list(range(range_end))
        for i in range(2,range_end):
            F[i] = (F[i-1] + F[i-2])%10
        return F[n]

user_input_value = raw_input('Please specify fibonacci number: ')
user_operation_select = raw_input('Please specify operation to perform: [1 - get value], 2 - get last digit: ') or 1
try:
    val = int(user_input_value)
    operation = int(user_operation_select)
    if(operation != 1 and operation != 2):
        raise Exception("Unavailable option")

    if(operation == 1):
        result = get_fib(val)
    if(operation == 2):
        result = get_fib_last_digit(val)

    print("Result: %d" % result)
except ValueError:
    print("That's not an int!")
except Exception as ex:
    print(ex)