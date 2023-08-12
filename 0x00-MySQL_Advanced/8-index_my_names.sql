-- 8-index_my_names.sql
-- Create an index on the table `names` using the first name character
CREATE INDEX idx_name_first ON names (name(1));
