import matplotlib.pyplot as plt


def plot_trajectory(times, x, params=None):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(times, x, lw=2)
    ax.set_title("Simulated sleep-onset trajectory")
    ax.set_xlabel("Time")
    ax.set_ylabel("x(t)")
    ax.grid(True, alpha=0.3)

    if params is not None:
        ax.axvline(params.t0, color="red", linestyle="--", alpha=0.7, label="t0")
        ax.legend()

    return fig, ax


def plot_parameter_grid(results, alphas, sigmas):
    fig, axes = plt.subplots(len(alphas), len(sigmas), figsize=(12, 9), sharex=True, sharey=True)

    for i, alpha in enumerate(alphas):
        for j, sigma in enumerate(sigmas):
            ax = axes[i, j]
            times, x, params = results[(alpha, sigma)]
            ax.plot(times, x, color="steelblue", lw=1.5)
            ax.axvline(params.t0, color="red", linestyle="--", alpha=0.5)
            ax.set_title(f"alpha={alpha}, sigma={sigma}")
            ax.grid(True, alpha=0.2)

    fig.suptitle("Effect of landscape slope and noise on sleep-onset trajectories", fontsize=14)
    fig.supxlabel("Time")
    fig.supylabel("x(t)")
    fig.tight_layout()
    return fig, axes