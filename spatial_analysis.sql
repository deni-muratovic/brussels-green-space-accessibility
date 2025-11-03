-- Calculate green space access
SELECT 
    SUM((POPULATION_NUMERIC * ST_Area(geom)) / AREA) AS total_served_population,
    (SUM((POPULATION_NUMERIC * ST_Area(geom)) / AREA) / 1249597) * 100 AS access_percentage
FROM 
    intersection_final;
