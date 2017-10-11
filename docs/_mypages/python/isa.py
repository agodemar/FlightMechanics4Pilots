import sys
import math

from pint import UnitRegistry
unit = UnitRegistry()             
# units of measurements, 'pip install -U pint'
# ex: 3*unit.m, 45*unit.cm, A.to(unit.km) conversion,...
#     T = 274*unit.degK, T.magnitude -> 274

g = 9.80665 *unit.m/(unit.sec**2)
R = 287.00 *unit.joule/(unit.kg*unit.degK)
gamma = 1.4
def cal(p0, t0, a, h0, h1):
    g_ = g.magnitude
    R_ = R.magnitude
    if a != 0:
        t1 = t0 + a * (h1 - h0)
        p1 = p0 * (t1 / t0) ** (-g_ / a / R_)
    else:
        t1 = t0
        p1 = p0 * math.exp(-g_ / R_ / t0 * (h1 - h0))
    return t1, p1

def isa(altitude):
    a = [-0.0065, 0, 0.001, 0.0028] *unit.degK/unit.m
    h = [11000, 20000, 32000, 47000] *unit.m
    p0 = 101325 *unit.newton/(unit.m**2)
    t0 = 288.15 *unit.degK
    prevh = 0 *unit.m
    if altitude.magnitude < 0 or altitude.magnitude > 47000:
        print("altitude must be in [0, 47000] m")
        return
    for i in range(0, 4):
        if altitude <= h[i]:
            temperature_, pressure_ = cal(
                p0 .magnitude, 
                t0 .magnitude, 
                a[i] .magnitude,
                prevh .magnitude, 
                altitude .magnitude
            )
            temperature = temperature_ *unit.degK
            pressure = pressure_ *unit.newton/(unit.m**2)
            break;
        else:
            # sth like dynamic programming
            t0_, p0_ = cal(
                p0 .magnitude, 
                t0 .magnitude, 
                a[i] .magnitude, 
                prevh .magnitude, 
                altitude .magnitude
            )
            t0 = t0_
            p0 = p0_
            prevh = h[i]

    density = pressure / (R * temperature)
    soundspeed = math.sqrt(
        gamma * R.magnitude * temperature.magnitude
        ) *unit.m/unit.sec
    return [temperature, soundspeed, pressure, density]
