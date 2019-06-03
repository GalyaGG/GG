def print_ndarray(input):
    print(input)
    n, p = input.shape
    for i in range(n):
        row_value = input[i, :]
        res1 = ['%.2f + %.2f' % (value, value) for value in row_value]  # list compreention
        line = '|'.join(res1)
        print(line)
    print('')
    print(input)
    pass