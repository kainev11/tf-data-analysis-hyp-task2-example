import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 294776608

def solution(x: np.array, y: np.array) -> bool:
    ks_stat, p_value = ks_2samp(x, y)
    
    alpha = 0.03
    return p_value < alpha
