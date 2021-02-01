# Use this file to create the plane objects to find their performances and compare them to each other
# Place the XFLR5 polars into the "AirFoils" folder
# All units being used in this program are the SI units (m, s, m/s, kg, N, watts, joules)
# Down below is an example of an aircraft

import PistonEngine
import TurboJet
import ElectricMotor
import Plane

# units in metric
filename = "Rough-Performance-Estimates/AirFoils/NACA_2412.txt"
plane_airfoil_str = "Cessna 172"
wing_span = 11 # meters
chord = 1.378 # meters
swept_angle = 0 # degrees
air_density_at_cruise = 1.11 # kg/m^3
angle_of_attack_at_cruise = 2 # degrees
target_cruise_velocity = 62 # m/s
max_velocity = 84 # m/s
aircraft_mass = 767 # kg
cargo_mass = 173 # Kg
fuel_mass = 171 # kg
empty_weight_friction = 0.0175 # 
span_efficiency_factor = 0.7 # Oswald Effecency Factor
specific_fuel_consumption = 0.000000777 # SFC 
propeller_efficiency =.9 # (.75-.9)
engine_power = 120000 # joules
n_structure = 6 # 







a = PistonEngine.PistonEngine("NACA_2412_Re5.256.txt", "Cessna 172", 11, 1.378, 0, 1.11, 2, 62, 84, 767, 173, 171,
                              0.0175, 0.7, 0.000000777, .9, 120000, 6)

# b = PistonEngine.PistonEngine("NACA_2412_Re5.256.txt", "Cessna 172-1", 11, 1.378, 0, 1.11, 2, 62, 84, 747, 173, 190,
#                               0.0175, 0.7, 0.000000777, .9, 120000, 6)

# c = PistonEngine.PistonEngine(filename, plane_airfoil_str, wing_span, chord, swept_angle, air_density_at_cruise,
#                  angle_of_attack_at_cruise, target_cruise_velocity, max_velocity, aircraft_mass, cargo_mass, fuel_mass,
#                  empty_weight_friction, span_efficiency_factor, specific_fuel_consumption, propeller_efficiency,
#                  engine_power, n_structure)
                
a.plot_data()

print("Angel at Max rate of Climb %f degrees " % a.get_angle_of_max_rate_of_climb_in_degrees())
print(a.get_cD0())
print(a.get_cD_at_cruise())
print(a.get_cL_at_cruise())
print(a.get_cL_max())
print(a.get_empty_weight())
print(a.get_gross_takeoff_weight())
print(a.get_K())
print(a.get_lift_force_at_target_velocity())
print(a.get_maneuvering_velocity())
print(a.get_max_endurance())
print(a.get_max_pull_up_rate())
print(a.get_max_range())
print(a.get_min_pull_up_radius())
print(a.get_minimum_power_required())
print(a.get_n_at_target_velocity())
print(a.get_name())
print(a.get_power_required_at_target_cruise_velocity())
print(a.get_pull_up_radius_at_target_velocity())
print(a.get_pull_up_rate_at_target_velocity())
print(a.get_target_cruise_velocity())
print(a.get_thrust_required_at_target_cruise_velocity())
print(a.get_turn_radius_at_maneuvering_velocity())
print(a.get_turn_radius_at_target_velocity())
print(a.get_v_stall())
print(a.get_velocity_for_max_endurance())
print(a.get_velocity_for_max_range())
print(a.get_velocity_for_max_rate_of_climb())
print(a.get_wing_area())
print(a.get_wing_loading())
print(a.get_wing_span())

lst = Plane.PlaneList()
lst.write_csv()

# lst.add_plane(a)
# lst.add_plane(b)

# c = lst.greatest_range()

# print(c.get_name())
