import numpy as np

from scipy.special import betainc

def pf(x, a, b):
    x = x / (x + (b / a))

    a1 = a / 2
    b1 = b / 2

    li = np.where(np.logical_and(x > 0, x < 1))
    ll = np.where(x <= 0)
    lu = np.where(x >= 1)

    F = np.zeros([len(x)])

    if np.array(ll).size != 0:
        F[ll] = 0
    if np.array(lu).size != 0:
        F[lu] = 1
    if np.array(li).size != 0:
        x1 = x[li]
        r = betainc(a1, b1, x1)
        F[li] = r

    return F
