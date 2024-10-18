# NFC Antenna Coil Generator

## Author: Tanguy Dietrich
## Date: 2024-10-18

### Overview
This script automates the process of computing the necessary parameters for an NFC antenna coil based on a specified capacitance. It generates the following files:
- An image of the computed coil geometry.
- A KiCad footprint (`.kicad_mod`) for use in PCB designs.
- A DXF file (`.dxf`) for 2D CAD software.
- An SVG file (`.svg`) for vector-based graphic design or other use cases.

### Features
- **Automatic coil computation**: Computes the optimal antenna coil geometry based on the resonant frequency and a given capacitance value.
- **File generation**: Generates the coil in multiple formats:
  - KiCad footprint module (`.kicad_mod`)
  - DXF file (`.dxf`)
  - SVG file (`.svg`)
  - Coil image plot.

### Installation
To run this script, you'll need the following dependencies:
- Python 3.x
- NumPy
- Matplotlib

You can install the required Python libraries with:

```bash
pip install numpy matplotlib
