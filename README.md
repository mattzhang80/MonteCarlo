# Monte Carlo Options Pricer

This project implements a Monte Carlo simulation for option pricing using Python's numpy, tkinter, and matplotlib libraries. The program calculates option prices based on user-defined parameters and displays the option price distribution using a bar chart within a Tkinter GUI window.

## Overview

The program simulates option prices using the Monte Carlo technique, which involves generating multiple random scenarios for the stock price movement over a given time period. It calculates the option payoff for each scenario and then calculates the average option price. The main components of the project are:

Monte Carlo Option Pricing: The monte_carlo_option_pricer function performs the Monte Carlo simulation for option pricing. It generates random price movements based on the Black-Scholes model, calculates the option payoffs, and estimates the average option price.
Graphical User Interface (GUI): The program provides a user-friendly GUI using the tkinter library. Users can input parameters such as stock price, strike price, time to maturity, risk-free rate, volatility, and the number of simulations. After clicking the "Calculate" button, the option price distribution is displayed as a bar chart.
## Usage

Clone the repository or download the source code.
Ensure you have the required libraries (numpy, tkinter, matplotlib) installed.
Run the Python script.
Input the desired option parameters in the GUI fields.
Click the "Calculate" button to generate the option price distribution.
## Features

Monte Carlo simulation for option pricing.
User-friendly GUI for input and visualization.
Option price distribution displayed as a bar chart.
Error handling for invalid input values.
## Credits

This project is an educational implementation of a Monte Carlo option pricing simulator with a graphical user interface. It provides a hands-on experience of option pricing concepts and GUI development using Python libraries. Developed by Matthew Zhang.

## License

This project is licensed under the MIT License. Feel free to use and modify it for educational and personal purposes.
