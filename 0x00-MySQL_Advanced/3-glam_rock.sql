-- 3-glam_rock.sql
-- Retrieving all band names which style contain 'Glam rock' with their lifespan 
SELECT band_name, IF(split IS NULL, 2022 - formed, split - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%';
