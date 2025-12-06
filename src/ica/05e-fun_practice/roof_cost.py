import math

def estimate_green_roof(wid, len, sqf_cost):
    area = rect_area(wid, len)
    cost = roof_cost(area, sqf_cost)
    print(" Area =", area)
    print(" Cost =", cost)

def rect_area(wid, len):

    return math.ceil(wid) * math.ceil(len)

def roof_cost(area, sqf_cost):
    return area * sqf_cost

print(estimate_green_roof(wid=32.8, len=54.25, sqf_cost=35))
