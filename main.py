import logging
from datetime import datetime
from time import time

from lumibot.backtesting import YahooDataBacktesting
from lumibot.tools import indicators

from my_first_strategy import MyFirstStrat
#from my_first_strategy_test import MyFirstStrat

# Choose your budget and log file locations
budget = 40000

####
# 1. Backtest the strategy using different inputs
####

# Choose the time from and to which you want to backtest
backtesting_start = datetime(2012, 1, 1)
backtesting_end = datetime(2021, 8, 16)
strategy_name = "MyFirstStrat"

# Run the  backtest
datestring = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
stats_file = f"logs/{strategy_name}_{datestring}.csv"
plot_file = f"logs/{strategy_name}_{datestring}.jpg"
stats = MyFirstStrat.backtest(
    strategy_name,
    budget,
    YahooDataBacktesting,
    backtesting_start,
    backtesting_end,
    stats_file=stats_file,
    plot_file=plot_file,
)
result = stats.get(strategy_name)

####
# 2. Trade Live
####

from lumibot.brokers import Alpaca
from lumibot.traders import Trader

# Import what you need for trading
from credentials import AlpacaConfig

# Initialize all our classes
logfile = "logs/test.log"
trader = Trader(logfile=logfile)
broker = Alpaca(AlpacaConfig)

strategy = MyFirstStrat(
    name=strategy_name,
    budget=budget,
    broker=broker,
)

trader.add_strategy(strategy)
trader.run_all()
