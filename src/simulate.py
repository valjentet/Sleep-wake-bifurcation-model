"""Simulation tools for the bistable sleep-onset model."""

import numpy as np
from .model import drift, ModelParams


def simulate_sde(x0=-1.0,t_max=100.0,dt=0.1,params=None,seed=None):
    if params is None:
        params = ModelParams()

    random = np.random.default_rng(seed)

    times = np.arange(0.0, t_max + dt, dt)
    x = np.zeros_like(times)
    x[0] = x0

    for i in range(len(times) - 1):
        t = times[i]
        noise = params.sigma * np.sqrt(dt) * random.normal() #Gaussian noise
        x[i + 1] = x[i] + drift(x[i], t, params.alpha, params.t0) * dt + noise

    return times, x