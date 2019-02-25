from pint import UnitRegistry
unit = UnitRegistry()
unit.load_definitions('./pint_addons.txt') # includes slug

# scientific calculations
import numpy as np

class Aircraft:
    mass # example = 800 *unit.kilogram
    weight
    surface_ref # example = 10 *unit.m**2
    chord_wing
    aspect_ratio_wing
    loading # W/s
    fuel_capacity # example = ( 42 *unit.gallon ).to(unit.m**3)

    
