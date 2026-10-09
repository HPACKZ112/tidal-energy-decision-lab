import math
water_density = 1025.0
rotor_radius = 5
current_speed = 2.0
power_coefficient = 0.40
conversion_efficiency = 0.90
swept_area=math.pi * rotor_radius**2
mechanical_power = (0.5*water_density*swept_area*current_speed**3*power_coefficient)
electrical_power=mechanical_power*conversion_efficiency

print(f"swept area : {swept_area:.2f} m^2")
print(f"mechanical power : {mechanical_power/1000:.2f} kW")
print(f"electrical power : {electrical_power/1000:.2f} kW")
