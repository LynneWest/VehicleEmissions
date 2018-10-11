--Create view for vehicle emission question A
CREATE VIEW VehicleEmissionsA AS
SELECT VClass, co2, co2TailpipeGpm, ghgScore, score
FROM vehicle, emissionScore
WHERE vehicle.id = emissionScore.id
AND fuelType2 IS NULL
AND fuelType1 != 'Natural Gas'
AND fuelType1 != 'Electricity'
AND fuelType1 != 'Diesel'
