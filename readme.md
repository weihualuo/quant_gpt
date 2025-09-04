# Quant Backtesting Project

This project uses **Backtrader**, **TA-Lib**, and **Akshare** to run configurable quantitative backtests.

## Features
- Modular strategy system with TA-Lib indicators
- Data fetching via Akshare
- JSON configuration for parameters, strategy choice, and stock pool

## Quick Start
1. Install dependencies: `pip install -r requirements.txt`
2. Edit `config/config.json` to choose stocks and strategy parameters
3. Run the backtest: `python backtest.py`

## Project Structure
- `backtest.py` – entry point for running backtests
- `strategies/` – Backtrader strategy implementations
- `data/` – data acquisition utilities using Akshare
- `config/` – configuration files
- `tests/` – basic tests ensuring configuration integrity
