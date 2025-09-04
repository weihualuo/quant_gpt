"""Entry point for running Backtrader backtests."""
from __future__ import annotations

import importlib
import json
import pathlib
from typing import Any

import backtrader as bt

from data.akshare_data import get_stock_data


def run_from_config(cfg: dict[str, Any]) -> None:
    cerebro = bt.Cerebro()
    cerebro.broker.setcash(cfg.get("cash", 100000))

    module = importlib.import_module(cfg["strategy"]["module"])
    strategy_cls = getattr(module, cfg["strategy"]["class"])
    cerebro.addstrategy(strategy_cls, **cfg["strategy"].get("params", {}))

    start = cfg["start"].replace("-", "")
    end = cfg["end"].replace("-", "")
    for sym in cfg.get("stocks", []):
        df = get_stock_data(sym, start, end)
        data = bt.feeds.PandasData(dataname=df)
        cerebro.adddata(data, name=sym)

    cerebro.run()
    # Plotting is optional; comment out if running in headless environments
    # cerebro.plot()


def main(config_path: str) -> None:
    cfg_file = pathlib.Path(config_path)
    with cfg_file.open("r", encoding="utf-8") as f:
        cfg = json.load(f)
    run_from_config(cfg)


if __name__ == "__main__":
    main("config/config.json")
