<h1> Analyzing Stock Data from Kaggle's Huge Stock Market Dataset </h1>

<h1>  Libraries Used </h1>
<h3> Matplotlib </h3>
 This library is used to visualize the stock data in question. 
 To install the library for usage, simply run "pip install Matplotlib" on your code terminal. 

<h3> Pandas </h3>
This library is used for data manipulation. To install de library for usage, simply run "pip install pandas" on your code terminal.

<h3> sklearn </h3>
When running the muranoquestao7letraC.py program, user will need to import and install "sklearn.model_selection" and "sklearn.linear_model". To install both on your computer, simply run "pip install sklearn" on your code terminal. 

<h1> Code and Results </h1>
<h2> Simple Moving Average </h2>
<p> Test by running muranoquestao7.py </p>
<p> The first function of the code is used to calculate and plot the stock's simple moving
average using Pandas' built-in function "rolling()". where it calculates the "mean" using a specific window
size. </p>
<p> After the code has been run, 10 different Stocks and ETFs will appear
with their daily closing prices being plotted against its respective dataframe. Along
with it's closing prices, it's moving average with 4 different window sizes shall also appear.</p>
<p> For example, here is the graph generated for abax.us stock price:</p>

![image](https://github.com/user-attachments/assets/a35a32c8-e6e7-4250-9dda-e91afcc8a51c)
<p> It's worth noticing how SMA's with bigger windows, such as the purple line in the graph above, show a certain "delay" when compared to the original "Close Price" graph. This happens because of the way the moving average is calculated. </p>
<p> Since a built-in function was used, the code does not exemplify how the 'thinking' behind calculating the SMA happens, but the formula used is this: </p>

![image](https://github.com/user-attachments/assets/9ba38cb9-32e9-407e-a1d0-3b93d8bb3bca)
The "K" value would be the size of the window, and, as seen in the graph, increasing K means a decrease in accuracy. 
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

<p> The rank given by the code makes sense, as the two most correlated companies are directly related to the fluctuation of oil prices. Such similiarities continue down the list, contributing to the certainty that the correlation results are correct. </p>

<h2> Regression </h2>
<p> Test by running muranoquestao7letraC.py</p>
<P> This file will use the tools provided by the sklearn libraries to apply a linear regression and attempt to predict stock price flutuations. 
</P>
<p> When running the close, it is clear that the predicted prices match very closely to the real values, as seen in the data below: </p>

![image](https://github.com/user-attachments/assets/2dfa24dc-11b8-4a60-a876-2eadc9bffff2)
![image](https://github.com/user-attachments/assets/e488180c-127c-4563-8a7f-8df91ed3f6bd)


The same is true for all the companies analyzed (Microsoft, Apple and Google). 
This may be because of how the other parameters are used to determine the stock price. By using it's "Open", "High", "Low" and "Volume" data to predict the "Closing" data, and with 80% of the stock's past performance being used as a training database, it is hard to miss when looking for the "Close" price.
<p> This result would not replicate when attempting to predict future stock prices, for the lack of access to information about it's current volume, or it's daily high and low, but assembling a regression line to determine future trends could help, as shown in the following graph: </p>

![image](https://github.com/user-attachments/assets/9ea0d929-76f8-4d0d-9a37-35b1db787981)

<h2> External help and sources: </h2>
To learn more about linear regression and to complete this assignement, it would be honest to credit DataGeek's youtube video: https://www.youtube.com/watch?v=HiTBhBrs5q0, and Joel Grus' book "Data Science From Scratch". 
