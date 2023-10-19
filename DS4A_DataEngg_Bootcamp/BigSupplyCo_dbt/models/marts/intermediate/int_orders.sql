with orders as (
    select * from {{ ref('fct_orders') }}
),

customers as (
    select * from {{ ref('dim_customers') }}
),

products as (
    select * from {{ ref('dim_products') }}
),

departments as (
    select * from {{ ref('dim_departments') }}
),

categories as (
    select * from {{ ref('dim_categories') }}
),

final as (
    select distinct *
    from orders
    left join customers 
    on orders.order_customer_id = customers.customer_id
    left join departments
    on orders.order_department_id = departments.department_id
    left join products 
    on orders.order_item_cardprod_id = products.product_card_id
    left join categories
    on categories.category_id = products.product_category_id
)

select * from final