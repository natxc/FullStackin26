{{ config(materialized='table') }}

with orders as (
    select * from {{ ref('stg_bigsupplyco__orders') }}
),

final as (
    select {{ dbt_utils.star(from=ref('stg_bigsupplyco__orders'), except=['etl_update_ts']) }}
    from orders
)

select * from final