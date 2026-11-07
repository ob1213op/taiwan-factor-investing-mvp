Feature: 營收 YoY 因子 Point-in-Time (PIT) 無前視偏誤驗證

  Scenario: 確保月調倉僅使用發布日已知之營收數據
    Given 歷史營收數據與公告日期
    When 執行 2023 年 5 月底月調倉
    Then 只能引用 5 月 10 日前已公告之 4 月營收
    And 不得提前讀取未公告之數據