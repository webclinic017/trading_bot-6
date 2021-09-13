# trading_bot

This is a stock trading bot created from the [Lumibot repository](https://github.com/Lumiwealth/lumibot).

This bot uses a main file, a strategy file and a credentials file. It uses [Alpaca](http://alpaca.markets/) as a broker. 

The strategy currently set up is a diversified leveraged ETF strategy. 

Backtesting, performed over the time period January 1, 2012 to August 16, 2021 yielded the following results:

- CAGR 29.34%      
- Volatility 27.23%
- Sharpe 1.08
- Max Drawdown 45.20% on 2020-03-24
- RoMaD 64.92%

Compared to the benchmark of the SPY ticker for the same time period:

- SPY CAGR 18.63%
- SPY Volatility 16.18%
- SPY Sharpe 1.15
- SPY Max Drawdown 33.28% on 2020-03-23
- SPY RoMaD 55.99%

You can see that while my strategy has roughly double the returns of the S&P 500, it has also twice as volatile. That being the case, the CAGR and volatility are comparable relative to one another yielding a Sharpe ratio close to that of the S&P 500.

Plotting the returns, this strategy yielded estentially the market return from 2012 through 2016, after which the strategy outperformed the market significantly.

I will be further developing this strategy to reduce volatility and maximize returns with the goal of adding AI/ML capabilities to it. I look forward to when the Lumibot library adds a broker that is capable of trading cryptocurrency.




