drop table if exists tmp_claims;

create table if not exists
    tmp_claims
as
    select
        uuid_generate_v4() as id,
        null::uuid as holistic_appeal_id,
        null::uuid as appellant_uuid,
        null::uuid as provider_uuid,
        null::varchar as appellant_name,
        data.*
    from
    ((
        select
            lower(regexp_replace(control_number::varchar, '\W+', '', 'g')) as original_claim_id,
            coalesce(dollar_amount, 0.0) as amount_billed,
            coalesce(covered_charge, 0.0) as amount_paid,
            coalesce(non_covered_charge, 0.0) as amount_controversy,
            hic_number::varchar as appellant_id,
            appeal_appellant_type as appellant_type,
            medicare_type as appellant_medicare_type,
            appeal_category as appellant_appeal_category,
            case
                when rac_name is not null
                then 'true'::boolean
                else 'false'::boolean
            end as appellant_rac,
            lower(regexp_replace(npi::varchar, '\W+', '', 'g')) as national_provider_id,
            lower(regexp_replace(provider_business_name, '\W+', '', 'g')) as provider_name,
            appeal_start_date as status_open_date,
            decision_issued_date as status_closed_date,
            appeal_disposition as status_closed_action,
            appeal_number as lvl1_appeal_number,
            null as lvl2_appeal_number,
            null as lvl3_appeal_number,
            lower(regexp_replace(ac_qio_name::varchar, '\W+', '', 'g')) as reviewer_name,
            'MAC' as reviewer_type,
            null as location,
            'level 1' as level
        from
            lvl1_appeals
        ) union (
        select
            lower(regexp_replace(control_number::varchar, '\W+', '', 'g')) as original_claim_id,
            coalesce(item_original_amount_claim_sum, 0.0) as amount_billed,
            0.00 as amount_paid,
            0.00 as amount_controversy,
            hic_number::varchar as appellant_id,
            appeal_appellant_type as appellant_type,
            medicare_type as appellant_medicare_type,
            appeal_category as appellant_appeal_category,
            rac_flag as appellant_rac,
            lower(regexp_replace(npi::varchar, '\W+', '', 'g')) as national_provider_id,
            lower(regexp_replace(provider_business_name, '\W+', '', 'g')) as provider_name,
            appeal_start_date as status_open_date,
            appeal_end_date as status_closed_date,
            appeal_disposition as status_closed_action,
            null as lvl1_appeal_number,
            appeal_number as lvl2_appeal_number,
            null as lvl3_appeal_number,
            lower(regexp_replace(ac_name::varchar, '\W+', '', 'g')) as reviewer_name,
            'QIC' as reviewer_type,
            mas_organization_name as location,
            'level 2' as level
        from
            lvl2_appeals
        ) union (
        select
            lower(regexp_replace(control_number::varchar, '\W+', '', 'g')) as original_claim_id,
            coalesce(item_original_amount_claim_sum, 0.0) as amount_billed,
            0.00 as amount_paid,
            0.00 as amount_controversy,
            hic_number::varchar as appellant_id,
            appeal_appellant_type as appellant_type,
            medicare_type as appellant_medicare_type,
            appeal_category as appellant_appeal_category,
            rac_flag as appellant_rac,
            lower(regexp_replace(npi::varchar, '\W+', '', 'g')) as national_provider_id,
            lower(regexp_replace(provider_business_name, '\W+', '', 'g')) as provider_name,
            appeal_start_date as status_open_date,
            appeal_end_date as status_closed_date,
            appeal_disposition as status_closed_action,
            null as lvl1_appeal_number,
            lvl2_appeal_number,
            null as lvl3_appeal_number,
            lower(regexp_replace(ac_name::varchar, '\W+', '', 'g')) as reviewer_name,
            'QIC' as reviewer_type,
            lvl1_organization_name as location,
            'level 2' as level
        from
            lvl3_appeals_lvl2_related
        ) union (
        select
            lower(regexp_replace(claim_number::varchar, '\W+', '', 'g')) as original_claim_id,
            0.00 as amount_billed,
            0.00 as amount_paid,
            0.00 as amount_controversy,
            appellant_name::varchar as appellant_id,
            appellant_type as appellant_type,
            medicare_type as appellant_medicare_type,
            appeal_category as appellant_appeal_category,
            null as appellant_rac,
            lower(regexp_replace(npi::varchar, '\W+', '', 'g')) as national_provider_id,
            lower(regexp_replace(provider_name, '\W+', '', 'g')) as provider_name,
            dt_comp_rqst_recd as status_open_date,
            null as status_closed_date,
            null as status_closed_action,
            null as lvl1_appeal_number,
            null as lvl2_appeal_number,
            reconsider_number as lvl3_appeal_number,
            lower(regexp_replace(adj_team_name::varchar, '\W+', '', 'g')) as reviewer_name,
            'ALJ' as reviewer_type,
            field_office as location,
            'level 3' as level
        from
            lvl3_appeals
        ) union (
        select
            lower(regexp_replace(control_number::varchar, '\W+', '', 'g')) as original_claim_id,
            coalesce(item_original_amount, 0.0) as amount_billed,
            0.00 as amount_paid,
            0.00 as amount_controversy,
            hic_number::varchar as appellant_id,
            requester_type as appellant_type,
            medicare_part as appellant_medicare_type,
            appeal_category as appellant_appeal_category,
            null as appellant_rac,
            lower(regexp_replace(npi::varchar, '\W+', '', 'g')) as national_provider_id,
            lower(regexp_replace(provider_business_name, '\W+', '', 'g')) as provider_name,
            complete_request_received_date as status_open_date,
            decision_letter_mailed_date as status_closed_date,
            appeal_disposition as status_closed_action,
            null as lvl1_appeal_number,
            null as lvl2_appeal_number,
            lvl3_appeal_number,
            lower(regexp_replace(employee_full_name::varchar, '\W+', '', 'g')) as reviewer_name,
            'ALJ' as reviewer_type,
            null as location,
            'level 3' as level
        from
            lvl4_appeals_lvl3_related
    )) as data
    where
        data.original_claim_id not like '%+%' and
        data.appellant_id is not null and
        data.national_provider_id is not null;
