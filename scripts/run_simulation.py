from src.model import ModelParams
from src.simulate import simulate_sde
from src.plotting import plot_trajectory
import matplotlib.pyplot as plt


def main():
    params = ModelParams(alpha=0.15, t0=50.0, sigma=0.8)
    times, x = simulate_sde(x0=1.0, t_max=100.0, dt=0.1, params=params, seed=00)
    fig, ax = plot_trajectory(times, x)
    fig.savefig("figures/trajectory.png", dpi=300, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()