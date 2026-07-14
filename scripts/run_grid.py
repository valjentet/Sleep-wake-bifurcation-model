"""Plotting multiples figure"""

from src.model import ModelParams
from src.simulate import simulate_sde
from src.plotting import plot_parameter_grid
import matplotlib.pyplot as plt


def main():
    alphas = [0.05, 0.1, 0.2, 0.5]
    sigmas = [0.4, 0.7, 0.8, 1]
    t0 = 50.0
    x0 = 1.0
    t_max = 100.0
    dt = 0.1
    seed = 42

    results = {}
    for i, alpha in enumerate(alphas):
        for j, sigma in enumerate(sigmas):
            params = ModelParams(alpha=alpha, t0=t0, sigma=sigma)
            times, x = simulate_sde(x0=x0, t_max=t_max, dt=dt, params=params, seed=seed)
            results[(alpha, sigma)] = (times, x, params)

    fig, axes = plot_parameter_grid(results, alphas, sigmas)
    fig.savefig("figures/parameter_grid.png", dpi=300, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()