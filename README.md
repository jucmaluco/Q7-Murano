<h1> Analyzing Stock Data from Kaggle's Huge Stock Market Dataset </h1>

<h1>  Libraries Used </h1>
<h3> Matplotlib </h3>
 This library is used to visualize the stock data in question. 
 To install the library for usage, simply run "pip install Matplotlib" on your code terminal. 

<h3> Pandas </h3>
This library is used for data manipulation. To install de library for usage, simply run "pip install pandas" on your code terminal.

<h1> Code and Results </h1>
<h2> Simple Moving Average </h2>
<p> Test by running muranoquestao7.py </p>
<p> The first function of the code is used to calculate and plot the stock's simple moving
average using Pandas' built-in function "rolling()". where it calculates the "mean" using a specific window
size. </p>
<p> After the code has been run, 10 different Stocks and ETFs will appear
with their daily closing prices being plotted against its respective dataframe. Along
with it's closing prices, it's moving average with 4 different window sizes shall also appear.</p>

<h2> Correlation </h2>
<p> Test by running muranoquestao7.py </p>
<p>This section of the program will analyze the correlation between
the last 100 days of each stock in question. The choice for the 100 
day timeframe came out of convenience, when dealing with stocks that have
much different establishment dates. Stocks that have been in existence, or in registration, 
for less than 100 days, have been discarded from the correlation.</p>

<p> Also, the top 5 stocks with the largest correlation have been exposed, and upon running the code,
the following rank shall be printed on the terminal: </p>

![image](https://github.com/user-attachments/assets/9b7a7a28-d0cb-4319-bacd-b28d711d5642)

<p> The rank given by the code makes sense, as the most correlated companies accompany oil prices. Such similiarities continue down the list. </p>
