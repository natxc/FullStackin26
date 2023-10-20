{{ config(materialized='table') }}

with departments as (
    select * from {{ ref('stg_bigsupplyco__departments') }}
),

final as (
    select {{ dbt_utils.star(from=ref('stg_bigsupplyco__departments'), except=['etl_update_ts','latitude_val','longitude_val']) }}
    from departments
)

select distinct * from final