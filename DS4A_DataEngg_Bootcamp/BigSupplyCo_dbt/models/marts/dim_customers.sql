with customers as (
    select * from {{ ref('stg_bigsupplyco__customers') }}
),

final as (
    select {{ dbt_utils.star(from=ref('stg_bigsupplyco__customers'), except=['etl_update_ts']) }}
    from customers
)

select * from final