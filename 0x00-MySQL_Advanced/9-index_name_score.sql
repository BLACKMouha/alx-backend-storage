-- 9-index_name_score.sql
-- Create an index on the table `names` using the first name character and the score
CREATE INDEX idx_name_first ON names (name(1), score);
