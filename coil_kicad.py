import os
import sys
import time
import numpy as np
import random

def generate_uuid():
    # Generate a random UUID
    return '{:08x}-{:04x}-{:04x}-{:04x}-{:012x}'.format(
        random.getrandbits(32), random.getrandbits(16),
        random.getrandbits(16), random.getrandbits(16),
        random.getrandbits(48))

def generate_nfc_kicad_mod_file(filename, xy_points, L, turns, width, spacing):
    # Open the file for writing
    with open(filename, 'w') as f:
        # Write the header
        f.write('(module "NFC_COIL"\n')
        f.write('\t(version 20240108)\n')
        f.write('\t(generator "Kicad-NFC-Coil_Generator")\n')
        f.write('\t(generator_version "1.0")\n')
        f.write('\t(layer "F.Cu")\n')
        f.write('\t(property "Reference" "L**"\n')
        f.write('\t\t(at 0 -0.5 0)\n')
        f.write('\t\t(unlocked yes)\n')
        f.write('\t\t(layer "F.SilkS")\n')
        f.write('\t\t(uuid "' + generate_uuid() + '")\n')
        f.write('\t\t(effects\n')
        f.write('\t\t\t(font\n')
        f.write('\t\t\t\t(size 1 1)\n')
        f.write('\t\t\t\t(thickness 0.1)\n')
        f.write('\t\t\t)\n')
        f.write('\t\t)\n')
        f.write('\t)\n')
        # f.write('\t(property "Value" "NFC_COIL"\n')
        f.write('\t(property "Value" "'+ "{:.2f} uH".format(L*1e6)+'"\n')
        f.write('\t\t(at 0 1 0)\n')
        f.write('\t\t(unlocked yes)\n')
        f.write('\t\t(layer "F.Fab")\n')
        f.write('\t\t(uuid "' + generate_uuid() + '")\n')
        f.write('\t\t(effects\n')
        f.write('\t\t\t(font\n')
        f.write('\t\t\t\t(size 1 1)\n')
        f.write('\t\t\t\t(thickness 0.15)\n')
        f.write('\t\t\t)\n')
        f.write('\t\t)\n')
        f.write('\t)\n')
        f.write('\t(property "Footprint" ""\n')
        f.write('\t\t(at 0 0 0)\n')
        f.write('\t\t(unlocked yes)\n')
        f.write('\t\t(layer "F.Fab")\n')
        f.write('\t\t(hide yes)\n')
        f.write('\t\t(uuid "' + generate_uuid() + '")\n')
        f.write('\t\t(effects\n')
        f.write('\t\t\t(font\n')
        f.write('\t\t\t\t(size 1 1)\n')
        f.write('\t\t\t\t(thickness 0.15)\n')
        f.write('\t\t\t)\n')
        f.write('\t\t)\n')
        f.write('\t)\n')
        f.write('\t(property "Datasheet" ""\n')
        f.write('\t\t(at 0 0 0)\n')
        f.write('\t\t(unlocked yes)\n')
        f.write('\t\t(layer "F.Fab")\n')
        f.write('\t\t(hide yes)\n')
        f.write('\t\t(uuid "' + generate_uuid() + '")\n')
        f.write('\t\t(effects\n')
        f.write('\t\t\t(font\n')
        f.write('\t\t\t\t(size 1 1)\n')
        f.write('\t\t\t\t(thickness 0.15)\n')
        f.write('\t\t\t)\n')
        f.write('\t\t)\n')
        f.write('\t)\n')
        f.write('\t(property "Description" ""\n')
        f.write('\t\t(at 0 0 0)\n')
        f.write('\t\t(unlocked yes)\n')
        f.write('\t\t(layer "F.Fab")\n')
        f.write('\t\t(hide yes)\n')
        f.write('\t\t(uuid "' + generate_uuid() + '")\n')
        f.write('\t\t(effects\n')
        f.write('\t\t\t(font\n')
        f.write('\t\t\t\t(size 1 1)\n')
        f.write('\t\t\t\t(thickness 0.15)\n')
        f.write('\t\t\t)\n')
        f.write('\t\t)\n')
        f.write('\t)\n')
        f.write('\t(attr smd)\n')
        f.write('\t(fp_poly\n')
        f.write('\t\t(pts\n')
        for x, y in xy_points:
            f.write('\t\t\t(xy {:.2f} {:.2f})\n'.format(x, y))
        f.write('\t\t)\n')
        f.write('\t\t(stroke\n')
        f.write('\t\t\t(width 0.01)\n')
        f.write('\t\t\t(type solid)\n')
        f.write('\t\t)\n')
        f.write('\t\t(fill solid)\n')
        f.write('\t\t(layer "F.Cu")\n')
        f.write('\t\t(uuid "' + generate_uuid() + '")\n')
        f.write('\t)\n')
        # then add pad for the coil
        # get the position of the last point
        x, y = xy_points[-1]
        # add the pad
        f.write('\t(pad "1" smd rect\n')
        f.write('\t\t(at {:.2f} {:.2f})\n'.format(x-width/2, y+width/2))
        f.write('\t\t(size {:.3f} {:.3f})\n'.format(width, width))
        f.write('\t\t(layers "F.Cu" "F.Paste" "F.Mask")\n')
        f.write('\t\t(thermal_bridge_angle 45)\n')
        f.write('\t\t(uuid "' + generate_uuid() + '")\n')
        f.write('\t)\n')
        # second pad
        # get the position middle point
        x, y = xy_points[len(xy_points)//2]
        # add the pad
        f.write('\t(pad "2" smd rect\n')
        f.write('\t\t(at {:.2f} {:.2f})\n'.format(x-width/2,y-width/2))
        f.write('\t\t(size {:.3f} {:.3f})\n'.format(width, width))
        f.write('\t\t(layers "F.Cu" "F.Paste" "F.Mask")\n')
        f.write('\t\t(thermal_bridge_angle 45)\n')
        f.write('\t\t(uuid "' + generate_uuid() + '")\n')
        f.write('\t)\n')
        f.write(')\n')
