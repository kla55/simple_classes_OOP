Purpose: To practice and understand classes and basic OOP.

To run code: 

from airtravel import *

f = Flight('SN060', aircraft("G-EUPT", "Airbus A319", num_rows = 22, num_seats_per_row = 6))
print(f.number())
print(f.aircraft_model())
