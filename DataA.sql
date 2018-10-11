--Select data to answer vehicle emission question A
SELECT VClass, co2TailpipeGpm
FROM vehicle
WHERE fuelType2 IS NULL
AND atvType IS NULL
AND fuelType1 != 'Natural Gas'
AND fuelType1 != 'Electricity'
AND fuelType1 != 'Diesel'
