--Combine redundant VClass values
UPDATE vehicle
SET VClass = 'Small Pickup Truck'
WHERE VClass = 'Small Pickup Trucks 4WD' OR VClass = 'Small Pickup Trucks 2WD' OR VClass = 'Small Pickup Trucks' OR VClass = 'Small Truck';

UPDATE vehicle
SET VClass = 'Standard Pickup Truck'
WHERE VClass = 'Standard Pickup Trucks/2wd' OR VClass = 'Standard Pickup Trucks 2WD' OR VClass = 'Standard Pickup Trucks 4WD' OR VClass = 'Standard Pickup Trucks 2WD' or VClass = 'Standard Pickup Trucks'

UPDATE vehicle
SET VClass = 'Sport Utility Vehicle'
WHERE VClass = 'Small Sport Utility Vehicle 2WD' OR VClass = 'Small Sport Utility Vehicle 4WD' OR VClass = 'Sport Utility Vehicle - 2WD' OR VClass = 'Sport Utility Vehicle - 4WD' OR VClass = 'Standard Sport Utility Vehicle 4WD' OR VClass = 'Standard Sport Utility Vehicle 2WD';

UPDATE vehicle
SET VClass = 'Station Wagon'
WHERE VClass = 'Midsize Station Wagons' OR VClass = 'Midsize-Large Station Wagons' OR VClass = 'Small Station Wagons';

UPDATE vehicle
SET VClass = 'Van'
WHERE VClass = 'Vans, Passenger Type' OR VClass = 'Vans, Cargo Type' OR VClass = 'Minivan' OR VClass = 'Vans Passenger' OR VClass = 'Minivan - 4WD' OR VClass = 'Minivan - 2WD' OR VClass = 'Vans'

DELETE FROM vehicle
WHERE VClass = 'Special Purpose Vehicle' OR VClass = 'Special Purpose Vehicles/2wd' OR VClass = 'Special Purpose Vehicles/4wd' OR VClass = 'Special Purpose Vehicle 4WD' OR VClass = 'Special Purpose Vehicle 2WD' OR VClass = 'Special Purpose Vehicles';