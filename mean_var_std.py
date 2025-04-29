#!/usr/bin/env python
# coding: utf-8


import numpy as np


def calculate(data):
        f=np.array(data,dtype='float')
        f=f.reshape(3,3)
        mean_list=[f.mean(axis=0).tolist(),f.mean(axis=1).tolist(),f.mean().tolist()]
        var_list=[f.var(axis=0).tolist(),f.var(axis=1).tolist(),f.var().tolist()]
        std_list=[f.std(axis=0).tolist(),f.std(axis=1).tolist(),f.std().tolist()]
        max_list=[f.max(axis=0).tolist(),f.max(axis=1).tolist(),f.max().tolist()]
        min_list=[f.min(axis=0).tolist(),f.min(axis=1).tolist(),f.min().tolist()]
        sum_list=[f.sum(axis=0).tolist(),f.sum(axis=1).tolist(),f.sum().tolist()]

# Using dictionary unpacking
        dic = {}
        dic= {**dic, 'mean': mean_list, 'var': var_list, 'std': std_list, 'max': max_list, 'min': min_list, 'sum': sum_list}

        return print(dic)
    
data=list(map(int, input("Enter numbers separated by space:\n ").split()))
try:
        calculate(data)
except ValueError :
        print('List must contain 9 numbers.')

