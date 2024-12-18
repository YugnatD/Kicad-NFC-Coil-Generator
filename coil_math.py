import os
import sys
import time
import math
from itertools import product
import numpy as np


# modified Harold A Wheeler formula for rectangular coils
def compute_coil_inductance_rect(n_turns, outer_length_mm, trace_width_mm, spacing_mm):
    # Constants
    mu_0 = 4 * math.pi * 1e-7  # Permeability of free space in H/m
    
    d_out = outer_length_mm / 1000
    w = trace_width_mm / 1000
    s = spacing_mm / 1000
    n = n_turns
    d_in = d_out - 2 * n * (w + s)

    d_avg = (d_out + d_in) / 2
    if d_in + d_out == 0:
        rho = 0
        return np.nan
    rho = (d_out - d_in) / (d_out + d_in)

    k1 = 2.34
    k2 = 2.75

    # Wheeler's formula
    L = k1 * mu_0 * ( (d_avg*n**2) / (1+k2*rho) )
    return L

def compute_coil_inductance_spiral(n_turns, outer_length_mm, trace_width_mm, spacing_mm):
    outer_radius = outer_length_mm / 2 / 1000  # Convert outer radius to meters
    trace_width_m = trace_width_mm / 1000  # Convert trace width to meters
    spacing_m = spacing_mm / 1000  # Convert spacing to meters

    # Calculate radial thickness c (difference between outer and inner radius)
    radial_thickness = n_turns * (trace_width_m + spacing_m) - spacing_m

    # Calculate average radius a
    inner_radius = outer_radius - radial_thickness  # Inner radius in meters
    average_radius = (outer_radius + inner_radius) / 2  # Average radius in meters

    # Constants
    mu_0 = 4 * math.pi * 1e-7  # Permeability of free space in H/m

    # Using the formula to calculate inductance
    L_circ = 31.33 * mu_0 * (n_turns**2) * (average_radius**2) / (8 * average_radius + 11 * radial_thickness)
    return L_circ

# Resonant frequency formula: f = 1 / (2 * pi * sqrt(L * C))
def compute_resonant_F(L, C):
    return 1 / (2 * math.pi * math.sqrt(L * C))

# Inductance formula: L = 1 / (4 * pi^2 * f^2 * C)
def compute_resonant_L(f, C):
    return 1 / (4 * math.pi**2 * f**2 * C)

# Capacitance formula: C = 1 / (4 * pi^2 * f^2 * L)
def compute_resonant_C(f, L):
    return 1 / (4 * math.pi**2 * f**2 * L)


# Function to search for optimal parameters to match target inductance
def find_optimal_parameters(target_inductance, length_range, turns_range, width_range, spacing_range, func=compute_coil_inductance_rect):
    best_params = None
    best_difference = float('inf')  # Start with a large difference
    
    # Iterate over all combinations of parameters
    for outer_length_mm, n_turns, trace_width_mm, spacing_mm in product(length_range, turns_range, width_range, spacing_range):
        # first check if the parameters are valid the antenna must be physically possible
        if outer_length_mm <= 0 or n_turns <= 0 or trace_width_mm <= 0 or spacing_mm <= 0:
            continue
        if 2 * n_turns * (trace_width_mm + spacing_mm) >= outer_length_mm:
            continue
        # inductance = compute_coil_inductance(n_turns, outer_length_mm, trace_width_mm, spacing_mm)
        inductance = func(n_turns, outer_length_mm, trace_width_mm, spacing_mm)
        difference = abs(inductance - target_inductance)
        
        if difference < best_difference:
            best_difference = difference
            best_params = (outer_length_mm, n_turns, trace_width_mm, spacing_mm, inductance)
    
    return best_params