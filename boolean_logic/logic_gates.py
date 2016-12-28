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

MG = nx.MultiGraph()


