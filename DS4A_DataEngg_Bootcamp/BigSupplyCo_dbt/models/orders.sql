{{ config(materialized='table') }}

with source as (
    select * from {{ ref('int_orders') }}
),

final as (
    select 
        *
        , sum(sales_amt) over (partition by product_category_id) as total_sales_amt_per_category_val
        , avg(order_item_total_amt) over (partition by customer_segment_cat) as avg_order_amt_per_segment_val
        , count(*) over (partition by order_region_addr) as n_orders_per_region_val
        , variance(product_price_amt) over (partition by product_card_id) as product_price_variance_val
        , stddev(product_price_amt) over (partition by product_card_id) as product_price_stddev_val
    from source
)

select * from final