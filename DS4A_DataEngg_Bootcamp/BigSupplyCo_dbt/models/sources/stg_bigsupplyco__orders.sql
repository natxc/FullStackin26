{{ config(materialized="table") }}

with

source  as (

    select * from {{ source('public','orders_s3_files_to_postgres') }}

),

final as (
    select
        "Order Id"::integer as order_id
        , "Order Item Id"::integer as order_item_id
        , "Order Customer Id"::integer as order_customer_id
        , "Order Department Id"::integer as order_department_id
        , "Order Item Cardprod Id"::integer as order_item_cardprod_id
        , "order date (DateOrders)"::date as order_dt
        , "Order Status" as order_status_cat
        , "market" as market_cat
        , "Order Region" as order_region_addr
        , "Order Country" as order_country_addr
        , "Order State" as order_state_addr
        , "Order City" as order_city_addr
        , case when "Order Zipcode" = '' then null 
            else lpad("Order Zipcode", 5, '0')
          end as order_zipcode_addr
        , "Order Item Quantity"::integer as n_order_items
        , "Order Item Discount"::float as order_item_discount_amt
        , "Order Item Discount Rate"::float as order_item_discount_pct
        , "Order Profit"::float as order_profit_amt
        , "Order Item Total"::float as order_item_total_amt
        , "Type" as payment_type_cat
        , "sales"::float as sales_amt
        , "Late Delivery Risk"::boolean as is_late_delivery_risk
        , "Days for shipping (real)"::integer as n_days_for_shipping__real
        , "Days for shipment (scheduled)"::integer as n_days_for_shipment__scheduled
        , "Delivery Status" as delivery_status_cat
        -- , "_airbyte_ab_id"
        -- , "_airbyte_emitted_at"
        , "_airbyte_normalized_at" as etl_update_ts
        -- , "_airbyte_orders_s3_files_to_postgres_hashid"
    from source
)
select * from final