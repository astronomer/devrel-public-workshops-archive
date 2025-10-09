

with source as (
    select * from `airflowintegrations`.`afs2025_schema_1`.`raw_orders`

),

renamed as (

    select
        id as order_id,
        user_id as customer_id,
        order_date,
        status

    from source

)

select * from renamed