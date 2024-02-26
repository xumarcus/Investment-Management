from datetime import datetime
import yahooquery as yq
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tabulate
import pprint

pp = pprint.PrettyPrinter()

tickers = yq.Ticker(["VOO", "NVDA"])
df = tickers.history(period="2y", interval="1d")
# df['desc'] = df.index
# df['date'] = df['desc'].apply(lambda l: [i for i in l]).str[1].apply(str).str[:10]
# df['ticker'] = df['desc'].apply(lambda l: [i for i in l]).str[0].apply(str)
# df['close'] = df['adjclose']

df['logret'] = np.log(df['close']/df['close'].shift(1))
df = df.drop(columns='desc')
# sorting df columns
df = df[['ticker', 'date', 'open', 'high', 'low', 'close', 'logret']]
df.reindex(df['date'])

new_df = pd.DataFrame()
new_df['date'] = df['date'].drop_duplicates()
print(df[0]['close'])
print(new_df)

# print(tabulate.tabulate(df.head(60), headers='keys', tablefmt='github', showindex=False))
# print(tabulate.tabulate(df.tail(60), headers='keys', tablefmt='github', showindex=False))
# print(f"Annualized Volatility: {(np.std(df['logret'][:252]) * np.sqrt(252)):.4%}")