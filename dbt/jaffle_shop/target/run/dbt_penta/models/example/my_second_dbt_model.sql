

  create or replace view `astronomer-dag-authoring`.`release_18`.`my_second_dbt_model`
  OPTIONS()
  as -- Use the `ref` function to select from other models

select *
from `astronomer-dag-authoring`.`release_18`.`my_first_dbt_model`
where id = 1;

