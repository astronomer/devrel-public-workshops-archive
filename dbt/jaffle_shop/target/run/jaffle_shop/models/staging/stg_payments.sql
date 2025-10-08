

  create or replace view `astronomer-dag-authoring`.`release_18`.`stg_payments`
  OPTIONS()
  as 

with source as (
    select * from `astronomer-dag-authoring`.`release_18`.`raw_payments`

),

renamed as (

    select
        id as payment_id,
        order_id,
        payment_method,

        -- `amount` is currently stored in cents, so we convert it to dollars
        amount / 100 as amount

    from source

)

select * from renamed;

