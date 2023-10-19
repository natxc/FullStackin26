with categories as (
    select * from {{ ref('stg_bigsupplyco__categories') }}
),

final as (
    select {{ dbt_utils.star(from=ref('stg_bigsupplyco__categories'), except=['etl_update_ts']) }}
    from categories
)

select * from final