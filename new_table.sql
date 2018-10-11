--add data to new table from another database
CREATE TABLE dbo.emissionScore (
	id		FLOAT,
	score	FLOAT );
INSERT INTO dbo.emissionScore
SELECT  id, AVG(score)
FROM Emissions.dbo.emissions$
GROUP BY id