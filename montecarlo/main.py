import numpy as np
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def monte_carlo_option_pricer(stock_price, strike_price, time_to_maturity, risk_free_rate, volatility, num_simulations):
    dt = time_to_maturity / 365
    num_days = int(time_to_maturity)

    option_payoffs = []
    for _ in range(num_simulations):
        stock_prices = [stock_price]
        for _ in range(num_days):
            z = np.random.normal()  # Use normal distribution for random numbers
            price_movement = stock_prices[-1] * np.exp((risk_free_rate - 0.5 * volatility**2) * dt + volatility * np.sqrt(dt) * z)
            stock_prices.append(price_movement)

        option_payoff = max(0, stock_prices[-1] - strike_price)
        option_payoffs.append(option_payoff)

    option_price = np.exp(-risk_free_rate * time_to_maturity) * np.mean(option_payoffs)
    return option_price

def calculate_option_price():
    try:
        stock_price = float(stock_price_var.get())
        strike_price = float(strike_price_var.get())
        time_to_maturity = float(time_to_maturity_var.get())
        risk_free_rate = float(risk_free_rate_var.get())
        volatility = float(volatility_var.get())
        num_simulations = int(num_simulations_var.get())

        option_prices = []
        for _ in range(1000):  # Simulate option prices multiple times for the chart
            option_price = monte_carlo_option_pricer(stock_price, strike_price, time_to_maturity, risk_free_rate, volatility, num_simulations)
            option_prices.append(option_price)

        average_option_price = np.mean(option_prices)
        option_price_label.config(text=f"Monte Carlo Option Price: {average_option_price:.4f}")

        # Create and display a bar chart
        plt.figure(figsize=(8, 5))
        plt.hist(option_prices, bins=30, alpha=0.7, color='blue')
        plt.axvline(x=average_option_price, color='red', linestyle='dashed', linewidth=2)
        plt.xlabel("Option Price")
        plt.ylabel("Frequency")
        plt.title("Option Price Distribution")
        plt.grid(True)
        plt.tight_layout()

        canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=len(input_labels) + 2, columnspan=2)

    except ValueError:
        option_price_label.config(text="Invalid input. Please enter numeric values.")

root = tk.Tk()
root.title("Monte Carlo Options Pricer")

input_labels = ["Stock Price:", "Strike Price:", "Time to Maturity (years):", "Risk-Free Rate:", "Volatility:", "Number of Simulations:"]
entry_vars = []

default_values = [100, 100, 1, 0.05, 0.3, 10000]

for row, (label_text, default_value) in enumerate(zip(input_labels, default_values)):
    ttk.Label(root, text=label_text).grid(row=row, column=0)
    entry_var = tk.StringVar(value=default_value)
    entry = ttk.Entry(root, textvariable=entry_var)
    entry.grid(row=row, column=1)
    entry_vars.append(entry_var)

stock_price_var, strike_price_var, time_to_maturity_var, risk_free_rate_var, volatility_var, num_simulations_var = entry_vars

calculate_button = ttk.Button(root, text="Calculate", command=calculate_option_price)
calculate_button.grid(row=len(input_labels), columnspan=2)

option_price_label = ttk.Label(root, text="")
option_price_label.grid(row=len(input_labels) + 1, columnspan=2)

root.mainloop()
