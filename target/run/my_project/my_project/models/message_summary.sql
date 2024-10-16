
  
    

  create  table "dbt"."public"."message_summary__dbt_tmp"
  
  
    as
  
  (
    

WITH message_data AS (
    SELECT 
        "Sender", 
        COUNT(*) AS message_count,
        MIN("Date") AS first_message_date,
        MAX("Date") AS last_message_date
    FROM 
        "dbt"."public"."gedebie"  -- Ensure 'gedebie' is a valid source
    GROUP BY 
        "Sender"
)

SELECT 
    "Sender",  -- Include the Sender column in the final output
    message_count,
    first_message_date,
    last_message_date,
    DATE_PART('day', last_message_date - first_message_date) AS message_duration_days
FROM 
    message_data
ORDER BY 
    message_count DESC
  );
  