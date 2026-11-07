import numpy as np
import pandas as pd


def compute_factors(df):
    """計算 EP, BP, ROE, 營業利益率, 12-1M Momentum"""
    # 範例因子邏輯與去極值標準化
    factors = df.copy()
    for col in ["EP", "BP", "ROE", "OpMargin", "Mom12M"]:
        if col in factors.columns:
            # Winsorization 1-99%
            lower = factors[col].quantile(0.01)
            upper = factors[col].quantile(0.99)
            factors[col] = factors[col].clip(lower, upper)
            # Z-Score
            factors[col] = (factors[col] - factors[col].mean()) / factors[
                col
            ].std()
    return factors