"""DXF Ruler Generator.

This module generates DXF files for laser cutting and engraving custom sized
rulers, which can be easily manufactured at the nearest FabLab.

Example
-------
Generate a 7cm ruler:

    $ python -m dxf_ruler_generator 7

This will create a 'ruler_7cm.dxf' on the current working directory.

"""
import os.path
from argparse import ArgumentParser
import ezdxf


parser = ArgumentParser(description="Generate rulers for digital fabrication.")
parser.add_argument("length", metavar="L", type=int,
                    help="an integer for the ruler's length, in centimeters.")
parser.add_argument("width", metavar="W", type=int, nargs="?", default=30,
                    help="an integer for the ruler's width, in milimeters.")
parser.add_argument("tick_width", metavar="TW", type=float,
                    nargs="?", default=.25,
                    help="a float for the tick's width, in milimeters.")
args = parser.parse_args()


def run():
    """Draw the ruler."""
    dwg = ezdxf.new('R2010')
    dwg.layers.new(name='CUT', dxfattribs={'color': 7})
    dwg.layers.new(name='SCAN', dxfattribs={'color': 5})

    msp = dwg.modelspace()

    ruler_outline = [(0, 0),
                     (10*(args.length+1), 0),
                     (10*(args.length+1), args.width),
                     (0, args.width),
                     (0, 0)]
    msp.add_lwpolyline(ruler_outline, dxfattribs={'layer': 'CUT'})

    for mm in range(10*args.length+1):
        x = mm + 5 - args.tick_width / 2
        if mm == 0 or mm % 10 == 0:
            tick_height = args.width / 3
            msp.add_text(
                str(mm//10),
                dxfattribs={'rotation': 90,
                            'height': 2,
                            'layer': 'SCAN'}
            ).set_pos((x-1, args.width-tick_height))
        elif mm % 5 == 0:
            tick_height = args.width / 6
        else:
            tick_height = args.width / 12

        ruler_tick = [(x, args.width),
                      (x, args.width-tick_height),
                      (x+.25, args.width-tick_height),
                      (x+.25, args.width),
                      (x, args.width)]
        msp.add_lwpolyline(ruler_tick, dxfattribs={'layer': 'SCAN'})

    filename = f'ruler_{args.length}cm.dxf'
    dwg.saveas(filename)
    print(os.path.abspath(filename), end='')


if __name__ == "__main__":
    run()
