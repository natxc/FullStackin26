{{ config(materialized="table") }}

with

source  as (

    select * from {{ source('public','categories_s3_files_to_postgres') }}

),

final as (
    select
        "Category Id"::integer as category_id
        , "Category Name" as category_name_attr
        -- , _airbyte_ab_id
        -- , _airbyte_emitted_at
        , _airbyte_normalized_at as etl_update_ts
        -- , _airbyte_categories___es_to_postgres_hashid
    from source
)
select * from final