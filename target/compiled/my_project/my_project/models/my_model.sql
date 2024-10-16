

WITH source_data AS (
    SELECT 
        * 
    FROM 
        "dbt"."public"."gedebie"  -- Reference the gedebie table
)

SELECT *
FROM source_data