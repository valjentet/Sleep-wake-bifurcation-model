"""Core equations for a minimal bistable sleep-onset model."""

from dataclasses import dataclass
import numpy as np

class ModelParams:
    alpha: float = 0.15   # speed of landscape movement
    t0: float = 50.0      # transition between states
    sigma: float = 0.25   #noise power

def beta(t: float | np.ndarray, alpha: float, t0: float) -> float | np.ndarray:
    return np.tanh(alpha * (t - t0))
    
def drift(x: float | np.ndarray,
          t: float | np.ndarray,
          alpha: float,
          t0: float) -> float | np.ndarray:
    b = beta(t, alpha, t0)
    return -((x + 1.0) * (x - b) * (x - 1.0))