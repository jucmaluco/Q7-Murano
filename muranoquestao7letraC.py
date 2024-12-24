import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

def linear_regression(file_name):
    filepath = "Data/Stocks/"+file_name+".us.txt"
    df = pd.read_csv(filepath)

    df["Date"] = pd.to_datetime(df["Date"])

    X = df[["Open", "High", "Low", "Volume"]].values  # Independent variables
    y = df["Close"].values  # Dependent variable
    dates = df["Date"].values

    X_train, X_test, y_train, y_test, dates_train, dates_test = train_test_split(
        X, y, dates, test_size=0.20, random_state=0
    )

    # Create and train the regression model
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    # Make predictions
    y_pred = regressor.predict(X_test)

    # Create a DataFrame for the results
    dfr = pd.DataFrame({
        "Date": dates_test,  # Include the dates corresponding to the test set
        "Actual Price": y_test,
        "Predicted Price": y_pred
    })

    # Sort results by Date for proper plotting
    dfr = dfr.sort_values(by="Date")

    # Calculate the overall regression trend line
    trend_X = np.arange(len(df)).reshape(-1, 1)
    trend_regressor = LinearRegression()
    trend_regressor.fit(trend_X, df["Close"].values)
    trend_y = trend_regressor.predict(trend_X)

    # Plot the results
    plt.figure(figsize=(16, 8))
    plt.plot(dfr["Date"], dfr["Actual Price"], label="Actual Price", color="blue", linewidth=2)
    plt.plot(dfr["Date"], dfr["Predicted Price"], label="Predicted Price", color="orange", linestyle="--", linewidth=2)
    plt.plot(df["Date"], trend_y, label="Trend Line", color="red", linewidth=2)  # Add trend line
    plt.ylabel("Close Price", fontsize=16)
    plt.xlabel("Date", fontsize=16)
    plt.title(f"Actual vs Predicted Close Prices for {file_name.upper()} Over Time", fontsize=18)
    plt.legend()
    plt.show()

linear_regression("googl")
linear_regression("aapl")
linear_regression("msft")
