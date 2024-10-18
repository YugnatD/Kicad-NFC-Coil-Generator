import os
import sys
import time
import math
import numpy as np
import ezdxf
import svgwrite


def generate_nfc_antenna(turns, width, spacing, antenna_size):
    xy_points = []
    xy_points_inner = []
    xy_points_outer = []

    current_x_outer = 0
    current_y_outer = 0
    current_x_inner = 0
    current_y_inner = -width

    current_wire_length_x_outer = antenna_size
    current_wire_length_y_outer = antenna_size
    current_wire_length_x_inner = antenna_size - width
    current_wire_length_y_inner = antenna_size - 2*width

    # make the first segment because it's special
    # outer segment
    xy_points_outer.append((current_x_outer, current_y_outer))
    # inner segment
    xy_points_inner.append((current_x_inner, current_y_inner))
    # move the outer segment
    current_x_outer += current_wire_length_x_outer
    xy_points_outer.append((current_x_outer, current_y_outer))
    # move the inner segment
    current_x_inner += current_wire_length_x_inner
    xy_points_inner.append((current_x_inner, current_y_inner))

    current_wire_length_x_inner -= width


    # first generate the outer parts
    for i in range(turns):
        # move outer
        current_y_outer -= current_wire_length_y_outer
        xy_points_outer.append((current_x_outer, current_y_outer))
        current_x_outer -= current_wire_length_x_outer
        xy_points_outer.append((current_x_outer, current_y_outer))
        current_wire_length_x_outer -= spacing + width
        current_wire_length_y_outer -= spacing + width
        current_y_outer += current_wire_length_y_outer
        xy_points_outer.append((current_x_outer, current_y_outer))
        current_x_outer += current_wire_length_x_outer
        xy_points_outer.append((current_x_outer, current_y_outer))
        current_wire_length_x_outer -= spacing + width
        current_wire_length_y_outer -= spacing + width
    
    # now generate the inner parts
    for i in range(turns):
        # move inner
        current_y_inner -= current_wire_length_y_inner
        xy_points_inner.append((current_x_inner, current_y_inner))
        current_x_inner -= current_wire_length_x_inner
        xy_points_inner.append((current_x_inner, current_y_inner))
        current_wire_length_x_inner -= spacing + width
        current_wire_length_y_inner -= spacing + width
        current_y_inner += current_wire_length_y_inner
        xy_points_inner.append((current_x_inner, current_y_inner))
        current_x_inner += current_wire_length_x_inner
        xy_points_inner.append((current_x_inner, current_y_inner))
        current_wire_length_x_inner -= spacing + width
        current_wire_length_y_inner -= spacing + width
    
    # add a last point in inner to have a pretty end, and not a triangle end
    xy_points_inner.append((current_x_inner+width, current_y_inner))

    # now puth the point in the right order to form a polygon
    xy_points.extend(xy_points_outer)
    # then add all inner points in reverse order
    xy_points_inner.reverse()
    xy_points.extend(xy_points_inner)
    return xy_points


def generate_nfc_dxf_file(points, output_file):
    # Create a new DXF document
    doc = ezdxf.new(dxfversion='R2010')

    # Add a model space to the DXF document
    msp = doc.modelspace()

    # Ensure the polyline is closed by repeating the first point as the last point
    if points[0] != points[-1]:
        points.append(points[0])  # Close the polygon by adding the first point at the end

    # Create a polyline with the provided points
    polyline_points = [(x, y) for x, y in points]

    # Add the polyline to the model space
    msp.add_lwpolyline(polyline_points)

    # Save the DXF document
    doc.saveas(output_file)

def generate_nfc_svg_file(points, output_file):
    # Create a new SVG document with a specified size (set as 500x500 here)
    dwg = svgwrite.Drawing(output_file, profile='tiny', size=(500, 500))

    # Ensure the polygon is closed by repeating the first point as the last point
    if points[0] != points[-1]:
        points.append(points[0])  # Close the polygon by adding the first point at the end

    # Add the polygon to the drawing
    dwg.add(dwg.polygon(points, stroke='black', fill='none', stroke_width=1))

    # Save the SVG document
    dwg.save()