# Sleep-onset bistable simulation

This project is a small simulation study inspired by the paper [*Learning the bistable cortical dynamics of the sleep-onset period*](https://neuro-team-femto.github.io/articles/2025/hu_biorxiv_2025.pdf). It reproduces, in a simplified way, a stochastic bistable model of the wake-to-sleep transition and explores the effect of three parameters: α, σ, and t0.

The objective is to provide a clear and reusable implementation of a minimal dynamical system that captures key qualitative behaviors reported in the paper: gradual transition, abrupt switching, and noise-driven flickering between states. The paper already explore a lot of effects about : α, σ, and t0. Reading the [paper](https://neuro-team-femto.github.io/articles/2025/hu_biorxiv_2025.pdf) is better to understand why we needs those parameters.

## Model
The simulation follows a time-varying stochastic bistable dynamics in which a particle evolves in a double-well landscape that slowly tilts over time. In the paper, the tilt is controlled by a hyperbolic tangent term and the dynamics include an additive stochastic component, which together generate a range of wake-to-sleep transition patterns.

A simplified form of the model is:

$$
dx_t = f(x_t,t)\,dt + \sigma\,dW_t
$$

with a time-dependent control term of the form:

$$
\beta(t) = \tanh\bigl(\alpha (t-t_0)\bigr)
$$

In this setup:
- α controls how sharply the landscape tilts.
- σ controls the noise intensity and therefore the amount of flickering.
- t0 controls when the transition start, it's also possible to adjust total time.

## What this repository contains

- A simple implementation of the stochastic simulation.
- Parameter sweeps to compare the influence of α, σ, and t0.
- Figures generated from the simulations.
- reproducible workflow for exploring the model qualitatively.

## Figures

### Simulated trajectories

Add one or more trajectory figures here.



Short caption: Example simulated trajectory showing a noise-driven transition from wake-like to sleep-like state.

### Effect of alpha

Add your figure comparing several values of α.



Short caption: Larger values of α tend to produce earlier or steeper transitions, although the paper reports a saturation effect for sufficiently large values.

### Effect of sigma

Add your figure comparing several values of α.



Short caption: Larger values of σ increase stochastic fluctuations and flickering between the two states.

### Effect of t0

Add your figure comparing several values of t0.



Short caption: Changing t0 shifts the onset of the transition in time.

## How to run

Example:

```bash
python scripts/run_simulation.py
```

If the project includes mutli parameters:

```bash
python scripts/run_grid.py
```

## Interpretation

This repository should be understood as a reproduction and exploration project. Its value is in making the qualitative dynamics of the model easy to inspect, modify, and visualize, rather than in introducing a new theoretical contribution. The paper itself argues that this kind of bistable stochastic model can reproduce a broad range of sleep-onset phenomenology and can potentially be fitted to EEG-derived trajectories. 

## Source

Primary inspiration:
- Hu Z, Aravind M, Lei X, Kutz JN, Aucouturier JJ. *Learning the bistable cortical dynamics of the sleep-onset period*. PLOS Computational Biology, 2026.


## Architecture 

```
sleep-onset-bistable-simulation/
├── README.md                    
├── .gitignore                   
├── figures/
├── scripts/                     
│   ├── run_simulation.py        
│   └── run_grid.py       
├── src/                         
│   ├── model.py                 
│   ├── simulate.py              
│   ├── plotting.py              
│   └── __init__.py
    ```