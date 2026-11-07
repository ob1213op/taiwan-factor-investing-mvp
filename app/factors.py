import numpy as np
import pandas as pd


def compute_factors(df):
    """計算 EP, BP, ROE, 營業利益率, 12-1M Momentum 並完成 Winsorization 與 Z-score"""
    factors = df.copy()
    factor_cols = ["EP", "BP", "ROE", "OpMargin", "Mom12M"]
    for col in factor_cols:
        if col in factors.columns:
            # 1%-99% Winsorization
            lower = factors[col].quantile(0.01)
            upper = factors[col].quantile(0.99)
            factors[col] = factors[col].clip(lower, upper)
            # Z-score 標準化
            factors[col] = (factors[col] - factors[col].mean()) / factors[
                col
            ].std()
    return factors