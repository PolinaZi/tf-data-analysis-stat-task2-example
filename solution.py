import pandas as pd
import numpy as np

from scipy.stats import norm, gamma


chat_id = 1117973953 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    n = len(x)
    time = 62
    
    left_edge_gamma = gamma.ppf(q = alpha / 2, a = n, scale = 1 / n)
    right_edge_gamma = gamma.ppf(q = 1 - alpha / 2, a = n, scale = 1 / n)
    
    lower = (left_edge_gamma + 2*x.mean() - 1/2) / (time ** 2)
    upper = (right_edge_gamma + 2*x.mean() - 1/2) / (time ** 2)
    
    return (lower, upper)
