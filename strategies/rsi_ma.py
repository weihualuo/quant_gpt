"""Example Backtrader strategy using TA-Lib indicators."""
from __future__ import annotations

import numpy as np
import talib
import backtrader as bt
import backtrader.talib as btalib


class RSIMAStrategy(bt.Strategy):
    """Combine RSI and moving average signals.

    Parameters
    ----------
    rsi_period: int
        Period for the RSI indicator.
    ma_period: int
        Period for the moving average indicator.
    """

    params = dict(rsi_period=14, ma_period=30)

    def __init__(self):
        self.dataclose = self.datas[0].close
        # Moving average from TA-Lib through Backtrader's wrapper
        self.ma = btalib.SMA(self.dataclose, timeperiod=self.p.ma_period)

    def next(self):
        # RSI computed directly with TA-Lib
        closes = np.array(self.dataclose.get(size=self.p.rsi_period))
        if len(closes) < self.p.rsi_period:
            return
        rsi = talib.RSI(closes, timeperiod=self.p.rsi_period)[-1]

        if not self.position:
            if rsi < 30 and self.dataclose[0] > self.ma[0]:
                self.buy()
        else:
            if rsi > 70 or self.dataclose[0] < self.ma[0]:
                self.sell()
