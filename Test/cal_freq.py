import numpy as np
import pickle
import os

dir = ".\\result"


def cal_freq(num):
    d = dir + "\\" + str(num) + "\\"
    # print(d)
    if not os.path.exists(d):
        os.makedirs(d)

    f = open(d + "train_data.pkl", 'rb')
    H = pickle.load(f)
    f.close()
    n1 = len(H)
    n2 = len(H[0])
    #freq = []
    total = 0
    for i in range(n1):
        #total = 0
        for j in range(n2):
            if(H[i, j] != -99): total += 1
    #print("calculating observed ratio for subsample",num, "is ",total/(n1 * n2))
        #freq.append(total/n2)
    return (total/(n1*n2))