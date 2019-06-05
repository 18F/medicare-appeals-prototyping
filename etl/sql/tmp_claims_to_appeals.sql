drop table if exists tmp_claims_to_appeals;

create table if not exists
    tmp_claims_to_appeals
as
    select
        data.*
    from
    ((
        select
            c.original_claim_id,
            c.amount_billed,
            c.amount_paid,
            c.amount_controversy,
            c.appellant_id,
            c.appellant_type,
            c.appellant_medicare_type,
            c.appellant_appeal_category,
            c.appellant_rac,
            c.national_provider_id,
            c.provider_name,
            c.status_open_data,
            c.status_closed_data,
            c.status_closed_action,
            c.lvl1_appeal_number,
            c.lvl2_appeal_number,
            c.lvl3_appeal_number,
            a.lvl4_appeal_number,
            a.table_name
        from
            tmp_claims c inner join tmp_lvl3_appeals a using(lvl3_appeal_number)
    ) union (
        select
            c.original_claim_id,
            c.amount_billed,
            c.amount_paid,
            c.amount_controversy,
            c.appellant_id,
            c.appellant_type,
            c.appellant_medicare_type,
            c.appellant_appeal_category,
            c.appellant_rac,
            c.national_provider_id,
            c.provider_name,
            c.status_open_data,
            c.status_closed_data,
            c.status_closed_action,
            c.lvl1_appeal_number,
            c.lvl2_appeal_number,
            a.lvl3_appeal_number,
            null as lvl4_appeal_number,
            a.table_name
        from
            tmp_claims c inner join tmp_lvl2_appeals a using(lvl2_appeal_number)
    ) union (
        select
            c.original_claim_id,
            c.amount_billed,
            c.amount_paid,
            c.amount_controversy,
            c.appellant_id,
            c.appellant_type,
            c.appellant_medicare_type,
            c.appellant_appeal_category,
            c.appellant_rac,
            c.national_provider_id,
            c.provider_name,
            c.status_open_data,
            c.status_closed_data,
            c.status_closed_action,
            c.lvl1_appeal_number,
            a.lvl2_appeal_number,
            c.lvl3_appeal_number,
            null as lvl4_appeal_number,
            a.table_name
        from
            tmp_claims c inner join tmp_lvl1_appeals a using(lvl1_appeal_number)
    )) as data;
