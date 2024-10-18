##################################################################################################################
# Author: Tanguy Dietrich
# Date: 2024-10-18
# Description:
#               This script automaticaly compute the coil needed for a nfc antenna based on the capacitor given
#               Then it generates the image of the coil and a .kicad_mod file for the coil to be used in KiCad
#               It also generates a .dxf file and a .svg file for the coil
##################################################################################################################

import os
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import argparse

import coil_image as ci
import coil_kicad as ck
import coil_math as cm

# based on https://www.translatorscafe.com/unit-converter/bg/calculator/planar-coil-inductance/
# and https://goodcalculators.com/resonant-frequency-calculator/

CAPACITANCE_CHIP = 28.5e-12 # 28.5 pF
RESONANT_FREQUENCY = 13.56e6 # 13.56 MHz

DEFAULT_MIN_LENGTH = 10
DEFAULT_MAX_LENGTH = 25
DEFAULT_STEP_LENGTH = 0.01

DEFAULT_MIN_TURNS = 5
DEFAULT_MAX_TURNS = 20
DEFAULT_STEP_TURNS = 1

DEFAULT_MIN_WIDTH = 0.25
DEFAULT_MAX_WIDTH = 1.0
DEFAULT_STEP_WIDTH = 0.05

DEFAULT_MIN_SPACING = 0.25
DEFAULT_MAX_SPACING = 1.0
DEFAULT_STEP_SPACING = 0.05

if __name__ == '__main__':
    # compute the inductance of the coil needed
    inductance_cible = cm.compute_resonant_L(RESONANT_FREQUENCY, CAPACITANCE_CHIP)
    # print the inductance needed
    print('\r\nInductance needed: {:.2f} uH\r\n'.format(inductance_cible * 1e6))
    # Define the range of values for outer length, turns, trace width, and spacing
    length_range = np.arange(DEFAULT_MIN_LENGTH, DEFAULT_MAX_LENGTH, DEFAULT_STEP_LENGTH) 
    turns_range = np.arange(DEFAULT_MIN_TURNS, DEFAULT_MAX_TURNS, DEFAULT_STEP_TURNS)
    width_range = np.arange(DEFAULT_MIN_WIDTH, DEFAULT_MAX_WIDTH, DEFAULT_STEP_WIDTH)
    spacing_range = np.arange(DEFAULT_MIN_SPACING, DEFAULT_MAX_SPACING, DEFAULT_STEP_SPACING)
    # find the optimal parameters to match the target inductance
    optimal_params = cm.find_optimal_parameters(inductance_cible, length_range, turns_range, width_range, spacing_range)
    # print the optimal parameters
    antenna_size = optimal_params[0]
    turns = optimal_params[1]
    width = optimal_params[2]
    spacing = optimal_params[3]
    inductance = optimal_params[4]
    print('Optimal Parameters Computed:')
    print('  Outer Length: {:.2f} mm'.format(antenna_size))
    print('  Turns: {}'.format(turns))
    print('  Trace Width: {:.2f} mm'.format(width))
    print('  Spacing: {:.2f} mm'.format(spacing))
    print('  Inductance: {:.2f} uH\r\n'.format(optimal_params[-1] * 1e6))
    # Generate points
    xy_points = ci.generate_nfc_antenna(turns, width, spacing, antenna_size)
    antenna_points = np.array(xy_points)
    # Create the polygon from the points
    polygon = Polygon(antenna_points, closed=True, fill=True, edgecolor='brown', facecolor='orange')
    # Plot the antenna shape as a polygon
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.add_patch(polygon)
    ax.set_title('NFC Antenna Geometry as Polygon')
    ax.set_xlim([0, antenna_size])
    ax.set_ylim([0, -antenna_size])
    ax.set_aspect('equal')
    plt.grid(True)
    plt.show()

    # Generate the KiCad .kicad_mod file
    filename = 'NFC_COIL.kicad_mod'
    ck.generate_nfc_kicad_mod_file(filename, xy_points, inductance, turns, width, spacing)
    print(f"KiCad module saved to {filename}")
    ci.generate_nfc_dxf_file(xy_points, 'NFC_COIL.dxf')
    print("DXF file saved to NFC_COIL.dxf")
    ci.generate_nfc_svg_file(xy_points, 'NFC_COIL.svg')
    print("SVG file saved to NFC_COIL.svg")


