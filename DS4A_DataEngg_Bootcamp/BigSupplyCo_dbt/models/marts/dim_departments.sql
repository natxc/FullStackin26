with departments as (
    select * from {{ ref('stg_bigsupplyco__departments') }}
),

final as (
    select {{ dbt_utils.star(from=ref('stg_bigsupplyco__departments'), except=['etl_update_ts']) }}
    from departments
)

select * from final