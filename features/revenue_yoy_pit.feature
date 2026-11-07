Feature: 營收 YoY 因子 Point-in-Time (PIT) 無前視偏誤驗證

  Scenario: 確保月調倉僅使用公告日已知之營收數據
    Given 歷史營收數據與公告日期
    When 執行月調倉
    Then 只能引用調倉日當下已發布之財報資料