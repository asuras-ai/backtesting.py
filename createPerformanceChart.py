import matplotlib.pyplot as plt

def create_performance_chart(result, benchmark_result=None):
    # Get the equity curve and trades from the backtest result
    equity = result._equity_curve
    trades = result._trades
    
    # Create figure with two subplots (returns and drawdowns)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True, 
                                 gridspec_kw={'height_ratios': [3, 1]})
    
    # 1. Plot Returns (top panel) on log scale
    strategy_returns = equity['Equity'].values
    ax1.semilogy(equity.index, strategy_returns, 'blue', label='Strategy')
    
    # If benchmark is provided, plot it too
    if benchmark_result is not None:
        benchmark_equity = benchmark_result._equity_curve
        benchmark_returns = benchmark_equity['Equity'].values
        ax1.semilogy(benchmark_equity.index, benchmark_returns, 'orange', label='Buy&Hold')
    
    ax1.set_ylabel('Total Return (log scale)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 2. Plot Drawdowns (bottom panel)
    drawdown = equity['DrawdownPct'].values
    ax2.plot(equity.index, -drawdown, 'blue')  # Negative because backtesting.py has positive drawdown values
    
    # If benchmark is provided, plot its drawdown too
    if benchmark_result is not None:
        benchmark_drawdown = benchmark_equity['DrawdownPct'].values
        ax2.plot(benchmark_equity.index, -benchmark_drawdown, 'orange')
    
    ax2.set_ylabel('Drawdown')
    ax2.set_xlabel('Year')
    ax2.axhline(y=0, color='k', linestyle='-', alpha=0.2)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig