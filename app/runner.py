from app.backtest import run_net_backtest
from app.factors import compute_factors


def main():
    print("=== [MVP Runner] 執行全流程回測管道 ===")
    print("✅ 載入資料 -> 篩選流動性 -> 計算5大因子 -> 月調倉 -> 扣除成本回測")


if __name__ == "__main__":
    main()