--Create table and insert values for question A
CREATE TABLE dataA (
compact_car				FLOAT,
large_car				FLOAT,
midsize_car				FLOAT,
minicompact_car			FLOAT,
small_pickup_truck		FLOAT,
sport_utility_vehicle	FLOAT,
standard_pickup_truck	FLOAT,
station_wagon			FLOAT,
subcompact_car			FLOAT,
two_seater				FLOAT,
van						FLOAT );

INSERT INTO dataA(compact_car)
SELECT co2TailpipeGpm
FROM vehicle
WHERE VClass = 'Compact Cars';

INSERT INTO dataA(large_car)
SELECT co2TailpipeGpm
FROM vehicle
WHERE VClass = 'Large Cars';

INSERT INTO dataA(midsize_car)
SELECT co2TailpipeGpm
FROM vehicle
WHERE VClass = 'Midsize Cars';

INSERT INTO dataA(minicompact_car)
SELECT co2TailpipeGpm
FROM vehicle
WHERE VClass = 'Minicompact Cars';

INSERT INTO dataA(small_pickup_truck)
SELECT co2TailpipeGpm
FROM vehicle
WHERE VClass = 'Small Pickup Truck';

INSERT INTO dataA(sport_utility_vehicle)
SELECT co2TailpipeGpm
FROM vehicle
WHERE VClass = 'Sport Utility Vehicle';

INSERT INTO dataA(standard_pickup_truck)
SELECT co2TailpipeGpm
FROM vehicle
WHERE VClass = 'Standard Pickup Truck';

INSERT INTO dataA(station_wagon)
SELECT co2TailpipeGpm
FROM vehicle
WHERE VClass = 'Station Wagon';

INSERT INTO dataA(subcompact_car)
SELECT co2TailpipeGpm
FROM vehicle
WHERE VClass = 'Subcompact Cars';

INSERT INTO dataA(two_seater)
SELECT co2TailpipeGpm
FROM vehicle
WHERE VClass = 'Two Seaters';

INSERT INTO dataA(van)
SELECT co2TailpipeGpm
FROM vehicle
WHERE VClass = 'Van';