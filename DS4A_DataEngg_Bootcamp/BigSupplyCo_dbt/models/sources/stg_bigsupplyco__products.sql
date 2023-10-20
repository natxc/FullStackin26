{{ config(materialized="table") }}

with

source  as (

    select * from {{ source('public','products_s3_files_to_postgres') }}

),

final as (
    select
        "Product Card Id"::integer as product_card_id
        , "Product Category Id"::integer as product_category_id
        , "Product Name" as product_name_attr
        , "Product Image" as product_image_url_attr
        , "Product Price"::float as product_price_amt
        , case when "Product Status" = '0' then True else False end as is_product_available
        -- , "Product Description" as product_description_txt
        -- , _airbyte_ab_id
        -- , _airbyte_emitted_at
        , _airbyte_normalized_at as etl_update_ts
        -- , _airbyte_products_s3__es_to_postgres_hashid
    from source
)
select * from final