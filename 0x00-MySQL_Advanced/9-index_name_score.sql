-- Script that creates an index idx_name_first on the table names
-- and the first letter of name and score

-- Drop index first if it exists
DROP INDEX IF EXISTS idx_name_first_score ON names;

-- Create index on the first letter of the name column
CREATE INDEX idx_name_first_score ON names (name(1), score);
