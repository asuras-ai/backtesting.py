# Trading Strategy Backtesting Collection

## Overview
This repository contains a collection of Jupyter notebooks implementing various trading strategies using the backtesting.py framework. Each notebook demonstrates different market approaches, complete with analysis and performance metrics.

## Structure
- `notebooks/`: Directory containing all Jupyter notebooks with trading strategies
- `requirements.txt`: List of Python dependencies required to run the notebooks

## Getting Started

### Prerequisites
Make sure you have Python 3.7+ installed on your system.

### Installation
1. Clone this repository:
   ```
   https://github.com/asuras-ai/backtesting.py.git
   cd backtesting-collection
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Running the Notebooks
1. Start Jupyter Lab or Notebook:
   ```
   jupyter lab
   # or
   jupyter notebook
   ```

2. Open any of the strategy notebooks from the `notebooks/` directory

## Strategy Notebooks

The repository includes implementations of various trading strategies:

- `moving_average_crossover.ipynb`: Simple MA crossover strategy with optimization
- `rsi_strategy.ipynb`: Relative Strength Index based strategy
- `bollinger_bands.ipynb`: Trading using Bollinger Bands
- `ml_prediction_model.ipynb`: Machine learning based prediction models

Each notebook includes:
- Strategy description and theoretical background
- Implementation code
- Backtesting results and performance metrics
- Visualizations (equity curves, drawdowns, trade distributions)
- Parameter optimization (where applicable)

## Requirements

Main dependencies include:
- backtesting.py
- pandas
- numpy
- matplotlib
- scikit-learn (for ML implementations)
- yfinance (for data acquisition)

Full dependencies are listed in `requirements.txt`.

## Data Sources

The notebooks use various data sources:
- Yahoo Finance (via yfinance)
- CSV files with historical data (included in some notebooks)
- Instructions for connecting to other data providers

## Contributing

Feel free to contribute your own strategy notebooks or improvements:
1. Fork the repository
2. Create a new branch for your strategy
3. Add your notebook(s)
4. Submit a pull request with a clear description

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

The trading strategies in this repository are for educational purposes only. Past performance is not indicative of future results. Always do your own research before risking capital in financial markets.
