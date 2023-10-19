with products as (
    select * from {{ ref('stg_bigsupplyco__products') }}
),

final as (
    select {{ dbt_utils.star(from=ref('stg_bigsupplyco__products'), except=['etl_update_ts']) }}
    from products
)

select * from final