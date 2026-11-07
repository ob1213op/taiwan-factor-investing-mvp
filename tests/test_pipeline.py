import numpy as np
import pandas as pd
import pytest


def test_zscore_standardization():
    """驗證 Z-score 標準化後平均值是否接近 0"""
    data = pd.Series([10.0, 20.0, 30.0, 40.0, 50.0])
    z_score = (data - data.mean()) / data.std()
    assert abs(z_score.mean()) < 1e-6


def test_liquidity_filter():
    """驗證流動性過濾後剔除最後 20% 的數據"""
    df = pd.DataFrame({"stock": range(10), "volume": range(1, 11)})
    threshold = df["volume"].quantile(0.2)
    filtered = df[df["volume"] > threshold]
    assert len(filtered) == 8