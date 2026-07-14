"""Plotting functions for the bistable sleep-onset model."""

import matplotlib.pyplot as plt


def plot_trajectory(times, x):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(times, x, lw=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("x(t)")
    ax.set_title("Simulated sleep-onset trajectory")
    ax.grid(True, alpha=0.2)
    fig.tight_layout()
    return fig, ax