import numpy as np
import pandas as pd

def editDis(a,b):
    D = np.zeros((len(a)+1, len(b)+1))
    for i in range(0, len(a) + 1):
        D[i][0] = i
    for j in range(0, len(b) + 1):
        D[0][j] = j
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                D[i][j] = D[i - 1][j - 1]
            else:
                D[i][j] = min(D[i][j - 1], D[i - 1][j], D[i - 1][j - 1]) + 1
    return D[-1][-1]

def all_substr_of_length(minl, maxl, t):
    return [{t[i:i+j]:[i+1,len(t[i:i+j])]} for i in range(len(t)-minl) for j in range(minl,maxl+1)]

def appro_match_substr(p, t, maxdis):
    """Gives minimum lev distance of all substrings of b and
    the single string a.
    """
    res = []
    for i in all_substr_of_length(len(p) - maxdis,maxdis+len(p), t):
        if editDis(' '.join(i.keys()),p)<=maxdis:
            res.append(list(i.values()))
    return res

if __name__ == "__main__":
    p='ACGTAG'
    t='ACGGATCGGCATCGT'
    a = appro_match_substr(p,t,2)
    print(a)
