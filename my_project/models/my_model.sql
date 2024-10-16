{{ config(materialized='table') }}

WITH source_data AS (
    SELECT 
        * 
    FROM 
        {{ source('my_database', 'gedebie') }}  -- Reference the gedebie table
)

SELECT *
FROM source_data
