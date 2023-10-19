{{ config(materialized="table") }}

with

source  as (

    select * from {{ source('public','departments_s3_files_to_postgres') }}

),

final as (
    select
        "Department Id"::integer as department_id
	    , "Department Name" as department_name_attr
	    , "latitude"::float as latitude_val
	    , "longitude"::float as longitude_val
	    -- , _airbyte_ab_id
	    -- , _airbyte_emitted_at
	    , _airbyte_normalized_at as etl_update_ts
	    -- , _airbyte_departments__es_to_postgres_hashid
    from source
)
select * from final