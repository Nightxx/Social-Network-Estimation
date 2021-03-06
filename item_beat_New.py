import numpy as np
import pickle

import os
from metric import delta

'''
This file generates item_beat.pkl. Where item_beat[i, u] is the fraction of item that i beat in train[u].

'''



dir = ".\\result"

test_num = 1

def item_beat_New(num,K):
    #print("Finding item beat ratio for subsample", num)
    d = dir + "\\" + str(num) + "\\"
    #print(d)
    if not os.path.exists(d):
        os.makedirs(d)

    f = open(d + "train_data.pkl", 'rb')
    train = pickle.load(f)
    f.close()

    f_rank = open(d + "observed_rank_new.pkl", 'rb')
    rank = pickle.load(f_rank)
    f_rank.close()

    n1 = len(train)
    n2 = len(train[0])
    res = np.zeros((n1, n2))
    for u in range(n2):
        for i in range(n1):

            if(train[i, u] == -99): continue
            beat = 0
            total = 0
            for j in range(n1):
                if(train[j, u] != -99):
                    total += 1
                    #tmp1 = 0
                    #tmp2 = 0
                    if(train[i, u] > train[j, u]):
                        beat += 1
                        '''
                        for idx in range(rank[u][i],rank[u][j]):
                            tmp1 += 1
                            tmp2 += delta(idx,K)
                        beat += tmp2/tmp1
                        '''
            if(total > 1): res[i, u] = beat/(total-1)
            '''
            if i in rank[u].keys():
                score = 0
                for j in range(rank[u][i], n1):
                    score += delta(j, K)
                res[i, u] = score
            '''
    f = open(d + "item_beat_New.pkl", "wb")
    pickle.dump(res, f)
    f.close()
    #print("Finished.")


