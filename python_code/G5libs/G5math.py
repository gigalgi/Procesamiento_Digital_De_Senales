import numpy as np

def nextpow2(n):
    m_f = np.log2(n)
    m_i = np.ceil(m_f)
    return int(2 ** m_i)
