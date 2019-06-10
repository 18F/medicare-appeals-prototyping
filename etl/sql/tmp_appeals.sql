drop table if exists tmp_appeals;

create table if not exists
    tmp_appeals
as
    select
        uuid_generate_v4() as id,
        null::uuid as holistic_appeal_id,
        data.*
    from
    ((
        select
            distinct on (lvl4_docket_number)
            lvl4_docket_number as original_appeal_id,
            lower(medicare_part::varchar) as medicare_part,
            lower(service_category::varchar) as service_category,
            lvl4_appeal_received_date as status_open_date,
            null::date as status_closed_date,
            lvl4_appeal_status as status_closed_action,
            null as reviewer_name,
            'DAB' as reviewer_type,
            null as location,
            'level 4' as level,
            'lvl4_appeals' as table_name
        from
            lvl4_appeals
    ) union (
        select
            distinct on (reconsider_number)
            reconsider_number as original_appeal_id,
            lower(medicare_type::varchar) as medicare_part,
            lower(appeal_category::varchar) as service_category,
            dt_comp_rqst_recd as status_open_date,
            null::date as status_closed_date,
            workflow_state as status_closed_action,
            lower(regexp_replace(adj_team_name::varchar, '\W+', '', 'g')) as reviewer_name,
            'ALJ' as reviewer_type,
            field_office as location,
            'level 3' as level,
            'lvl3_appeals' as table_name
        from
            lvl3_appeals
    ) union (
        select
            distinct on (regexp_split_to_table(lvl3_appeal_number::text, ',\s+'))
            regexp_split_to_table(lvl3_appeal_number::text, ',\s+') as original_appeal_id,
            lower(medicare_part::varchar) as medicare_part,
            lower(service_category::varchar) as service_category,
            null as status_open_date,
            lv3_decision_letter_mail_date as status_closed_date,
            lvl3_appeal_disposition as status_closed_action,
            null as reviewer_name,
            'DAB' as reviewer_type,
            null as location,
            'level 3' as level,
            'lvl4_appeals' as table_name
        from
            lvl4_appeals
    ) union (
        select
            distinct on (lvl2_appeal_number)
            lvl2_appeal_number as original_appeal_id,
            lower(medicare_type::varchar) as medicare_part,
            lower(appeal_category::varchar) as service_category,
            lvl2_appeal_start_date as status_open_date,
            lvl2_appeal_end_date as status_closed_date,
            lvl2_appeal_disposition as status_closed_action,
            lower(regexp_replace(lvl2_organization_name::varchar, '\W+', '', 'g')) as reviewer_name,
            lvl2_organization_name as reviewer_type,
            null as location,
            'level 2' as level,
            'lvl4_appeals_lvl2_related' as table_name
        from
            lvl4_appeals_lvl2_related
    ) union (
        select
            distinct on (lvl1_appeal_number)
            lvl1_appeal_number as original_appeal_id,
            lower(medicare_type::varchar) as medicare_part,
            lower(appeal_category::varchar) as service_category,
            lvl1_appeal_start_date as status_open_date,
            lvl1_appeal_end_date as status_closed_date,
            lvl1_appeal_disposition as status_closed_action,
            lower(regexp_replace(lvl1_organization_name::varchar, '\W+', '', 'g')) as reviewer_name,
            lvl1_organization_name as reviewer_type,
            null as location,
            'level 1' as level,
            'lvl4_appeals_lvl1_related' as table_name
        from
            lvl4_appeals_lvl1_related
    ) union (
        select
            distinct on (lvl1_appeal_number)
            lvl1_appeal_number as original_appeal_id,
            lower(medicare_type::varchar) as medicare_part,
            lower(appeal_category::varchar) as service_category,
            lvl1_appeal_start_date as status_open_date,
            lvl1_appeal_end_date as status_closed_date,
            lvl1_appeal_disposition as status_closed_action,
            lower(regexp_replace(lvl1_organization_name::varchar, '\W+', '', 'g')) as reviewer_name,
            lvl1_organization_name as reviewer_type,
            null as location,
            'level 1' as level,
            'lvl3_appeals_lvl1_related' as table_name
        from
            lvl3_appeals_lvl1_related
    ) union (
        select
            distinct on (lvl1_appeal_number)
            lvl1_appeal_number as original_appeal_id,
            lower(medicare_type::varchar) as medicare_part,
            lower(appeal_category::varchar) as service_category,
            lvl1_appeal_start_date as status_open_date,
            lvl1_appeal_end_date as status_closed_date,
            appeal_disposition as status_closed_action,
            lower(regexp_replace(mac_organization_name::varchar, '\W+', '', 'g')) as reviewer_name,
            mac_organization_name as reviewer_type,
            null as location,
            'level 1' as level,
            'lvl2_appeals_lvl1_related' as table_name
        from
            lvl2_appeals_lvl1_related
    )) as data;
