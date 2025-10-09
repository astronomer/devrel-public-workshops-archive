

with source as (
    select * from `airflowintegrations`.`afs2025_schema_1`.`raw_customers`

),

renamed as (

    select
        id as customer_id,
        first_name,
        last_name

    from source

)

select * from renamed