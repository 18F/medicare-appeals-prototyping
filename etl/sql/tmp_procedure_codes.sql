drop table if exists tmp_procedure_codes;

create table if not exists
    tmp_procedure_codes
as
    select
        data.*
    from ((
        select
            control_number as original_claim_id,
            procedure_code as code
        from
            lvl1_appeals_procedure_codes
    ) union (
        select
            control_number as original_claim_id,
            procedure_number as code
        from
            lvl2_appeals_procedure_codes
    ) union (
        select
            control_number as original_claim_id,
            procedure_code as code
        from
            lvl3_appeals_lvl2_related_procedure_codes
    ) union (
        select
            control_number as original_claim_id,
            procedure_code as code
        from
            lvl4_appeals_lvl3_related_procedure_codes
    )) as data;
