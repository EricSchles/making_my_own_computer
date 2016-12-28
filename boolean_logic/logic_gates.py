import networkx as nx

def constant_false(*args):
    return [False for _ in len(*args)]

def constant(*args):
    return *args

def simple_and(x,y):
    return x and y

def multi_and(*args):
    inputs = *args
    result = inputs[0]
    for elem in inputs[1:]:
        result = result and elem
    return result

def simple_or(x,y):
    return x or y

def multi_or(*args):
    inputs = *args
    result = inputs[0]
    for elem in inputs[1:]:
        result = result or elem
    return result

def simple_and_not(x,y):
    return x and not y

def multi_and_not(*args):
    inputs = *args
    result = inputs[0]
    for elem in inputs[1:]:
        result = result and not elem
    return result

def simple_not_and(x,y):
    return (not x) and y

def multi_not_and(*args):
    inputs = *args
    result = inputs[0]
    for elem in inputs[1:]:
        result = (not result) and elem
    return result

def choose_param(*args,index=0):
    return *args[index]

def simple_xor(x,y):
    return (x and (not y)) or ((not x) and y)

def multi_xor(*args):
    inputs = *args
    result = inputs[0]
    for elem in inputs[1:]:
        result = simple_xor(result, elem)
    return result

def simple_or(x,y):
    return x or y

def multi_or(*args):
    inputs = *args
    result = inputs[0]
    for elem in inputs[1:]:
        result = result or elem
    return result

MG = nx.MultiGraph()


