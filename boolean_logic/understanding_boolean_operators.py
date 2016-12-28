import inspect
import math
import pandas as pd

def sign_flip(sign):
    if sign == 0:
        return 1
    else:
        return 0

def bool_to_int(value):
    if value:
        return 1
    else:
        return 0
    
def generating_input_table(func):
    args = inspect.getargspec(func).args
    length_of_row = int(math.pow(2,len(args)))
    total_num_elements = length_of_row * len(args)
    inputs = []
    do_flip = 1
    for elem in range(len(args)):
        tmp = []
        sign = 0 
        for i in range(length_of_row):
            if i % do_flip == 0:
                sign = sign_flip(sign)
            tmp.append(sign)
        do_flip *= 2
        inputs.append(tmp)
    results = []
    for elem in range(len(inputs[0])):
        input_val = [inputs[ind][elem] for ind in range(len(args))]
        results.append(bool_to_int(func(*input_val)))
    args.append("results")
    inputs.append(results)
    df = pd.DataFrame({args[ind]:inputs[ind] for ind in range(len(args))})
    cols = df.columns.tolist()
    cols.remove("results")
    cols.append("results")
    return df[cols]
    
def example_func(x,y,z):
    return (x and y) or z

if __name__ == '__main__':
    print(generating_input_table(example_func))
