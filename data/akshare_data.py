"""Utility functions for fetching stock data using Akshare."""
from __future__ import annotations

import akshare as ak
import pandas as pd


def get_stock_data(symbol: str, start: str, end: str) -> pd.DataFrame:
    """Fetch daily stock data for Backtrader.

    Parameters
    ----------
    symbol: str
        Stock code accepted by Akshare, e.g. '000001.SZ'.
    start: str
        Start date in 'YYYYMMDD' format.
    end: str
        End date in 'YYYYMMDD' format.
    """
    df = ak.stock_zh_a_hist(symbol=symbol, period="daily", start_date=start, end_date=end, adjust="")
    df.index = pd.to_datetime(df["日期"])
    df = df[["开盘", "最高", "最低", "收盘", "成交量"]]
    df.columns = ["open", "high", "low", "close", "volume"]
    return df
