-- 2-fans.sql
-- Retrieving the total number of fans per country of each metal band
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands origin
GROUP BY origin
ORDER BY nb_fans DESC;
