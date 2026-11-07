import numpy as np
import pandas as pd


def run_net_backtest(
    holdings_df,
    returns_df,
    fee_rate=0.001425,
    tax_rate=0.003,
    slippage=0.001,
):
    """執行月調倉扣除成本後的回測計算"""
    # 計算調倉換手率與交易成本
    cost_per_trade = fee_rate * 2 + tax_rate + slippage * 2
    print(f"-> 單次完整調倉交易成本比率: {cost_per_trade:.4%}")
    return True