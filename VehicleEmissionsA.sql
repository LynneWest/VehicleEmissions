--Create view for question A
CREATE VIEW VehicleEmissionsA AS
SELECT VClass, co2TailpipeGpm, fuelType1, fuelType2, atvType
FROM vehicle