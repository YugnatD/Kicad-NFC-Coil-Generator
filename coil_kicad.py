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

def generate_nfc_kicad_mod_file(filename, xy_points):
    # Open the file for writing
    with open(filename, 'w') as f:
        # Write the header
        f.write('(module "NFC_COIL"\n')
        f.write('\t(version 20240108)\n')
        f.write('\t(generator "pcbnew")\n')
        f.write('\t(generator_version "8.0")\n')
        f.write('\t(layer "F.Cu")\n')
        f.write('\t(property "Reference" "REF**"\n')
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
        f.write('\t(property "Value" "NFC_COIL"\n')
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
        f.write(')\n')





# example of kicad_mod file
# (footprint "NFC_COIL"
# 	(version 20240108)
# 	(generator "pcbnew")
# 	(generator_version "8.0")
# 	(layer "F.Cu")
# 	(property "Reference" "REF**"
# 		(at 0 -0.5 0)
# 		(unlocked yes)
# 		(layer "F.SilkS")
# 		(uuid "5f3bc181-5f17-43c0-b860-2786212932d0")
# 		(effects
# 			(font
# 				(size 1 1)
# 				(thickness 0.1)
# 			)
# 		)
# 	)
# 	(property "Value" "NFC_COIL"
# 		(at 0 1 0)
# 		(unlocked yes)
# 		(layer "F.Fab")
# 		(uuid "ee6a6e4a-abc2-4dc7-b089-36833ec2f627")
# 		(effects
# 			(font
# 				(size 1 1)
# 				(thickness 0.15)
# 			)
# 		)
# 	)
# 	(property "Footprint" ""
# 		(at 0 0 0)
# 		(unlocked yes)
# 		(layer "F.Fab")
# 		(hide yes)
# 		(uuid "9e784775-56c5-49bf-9b55-32ed9849a966")
# 		(effects
# 			(font
# 				(size 1 1)
# 				(thickness 0.15)
# 			)
# 		)
# 	)
# 	(property "Datasheet" ""
# 		(at 0 0 0)
# 		(unlocked yes)
# 		(layer "F.Fab")
# 		(hide yes)
# 		(uuid "071e8870-d245-4677-aa43-73ee668e563f")
# 		(effects
# 			(font
# 				(size 1 1)
# 				(thickness 0.15)
# 			)
# 		)
# 	)
# 	(property "Description" ""
# 		(at 0 0 0)
# 		(unlocked yes)
# 		(layer "F.Fab")
# 		(hide yes)
# 		(uuid "4acfa58a-fe6a-4264-982c-edaac1559bb1")
# 		(effects
# 			(font
# 				(size 1 1)
# 				(thickness 0.15)
# 			)
# 		)
# 	)
# 	(attr smd)
#   (fp_poly
# 	(pts
# 		(xy 198.26 -643.89) (xy 274.74 -573.79) (xy 288.76 -647.72)
# 	)
# 	(stroke
# 		(width 0.01)
# 		(type solid)
# 	)
# 	(fill solid)
# 	(layer "F.Cu")
# 	(uuid "09213631-4e9b-40ad-8d54-59efaf75aac8")
# 	)
# )