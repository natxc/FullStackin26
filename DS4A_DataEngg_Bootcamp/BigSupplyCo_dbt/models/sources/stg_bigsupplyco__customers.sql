{{ config(materialized="table") }}

with

source  as (

    select * from {{ source('public','customers_s3_files_to_postgres') }}

),

final as (
    select
        "Customer Id"::integer as customer_id
        , "Customer Fname" as customer_first_name_attr
        , "Customer Lname" as customer_last_name_attr
        -- , "Customer Email" as customer_email_attr
        -- , "Customer Password" as customer_password_strid
        , "Customer Segment" as customer_segment_cat
        , "Customer Country" as customer_country_addr
        , "Customer State" as customer_state_addr
	    , "Customer City" as customer_city_addr
	    , case when "Customer Zipcode" = '' then null 
            else lpad("Customer Zipcode", 5, '0')
          end as customer_zipcode_addr
	    , "Customer Street" as customer_street_addr
	    -- , _airbyte_ab_id
    	-- , _airbyte_emitted_at
    	, _airbyte_normalized_at as etl_update_ts
    	-- , _airbyte_customers_s__es_to_postgres_hashid
    from source
)
select * from final