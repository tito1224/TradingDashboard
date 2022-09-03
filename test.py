from dash import dcc, html, Input, Output, callback
import dashObjects.dashObjects as do
import matplotlib.pyplot as plt

dfTest = do.getMarketDataEOD(['^GSPC'],'2021-01-01','2021-01-14')
print(dfTest['Adj Close'].values)
print(dfTest.index)

plt.plot(dfTest.index, dfTest['Adj Close'].values)
plt.show()
