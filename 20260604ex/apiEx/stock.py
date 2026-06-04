import time
from datetime import datetime

import yfinance as yf

TICKER = "005930.KS"  # 삼성전자 (KOSPI)

while True:
    try:
        stock = yf.Ticker(TICKER)

        # 최신 체결가 조회
        price = stock.fast_info.get("lastPrice")

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if price:
            print(f"[{now}] 삼성전자: {price:,.0f}원")
        else:
            print(f"[{now}] 가격 조회 실패")

    except Exception as e:
        print(f"에러 발생: {e}")

    time.sleep(5)