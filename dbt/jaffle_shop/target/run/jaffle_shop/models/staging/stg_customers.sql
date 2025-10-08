

  create or replace view `astronomer-dag-authoring`.`release_18`.`stg_customers`
  OPTIONS()
  as 

with source as (
    select * from `astronomer-dag-authoring`.`release_18`.`raw_customers`

),

renamed as (

    select
        id as customer_id,
        first_name,
        last_name

    from source

)

select * from renamed;

